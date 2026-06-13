import os
import json
import time
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from dotenv import load_dotenv
from azure.ai.agents import AgentsClient
from azure.ai.agents.models import FunctionTool, ToolSet
from azure.identity import DefaultAzureCredential

from tools.shopify import get_shopify_sales
from tools.zendesk import get_zendesk_tickets
from tools.inventory import get_inventory_status

load_dotenv()

app = FastAPI()

class Question(BaseModel):
    question: str

def shopify_sales_tool() -> str:
    """Get Shopify sales summary comparing this week vs last week."""
    return json.dumps(get_shopify_sales())

def zendesk_tickets_tool() -> str:
    """Get Zendesk support ticket trends and spikes this week."""
    return json.dumps(get_zendesk_tickets())

def inventory_status_tool() -> str:
    """Get current inventory levels and out-of-stock alerts."""
    return json.dumps(get_inventory_status())

user_functions = {shopify_sales_tool, zendesk_tickets_tool, inventory_status_tool}

@app.post("/ask")
async def ask(body: Question):
    client = AgentsClient(
        endpoint=os.environ["PROJECT_ENDPOINT"],
        credential=DefaultAzureCredential()
    )

    functions = FunctionTool(functions=user_functions)
    toolset = ToolSet()
    toolset.add(functions)

    agent = client.create_agent(
        model=os.environ["MODEL_DEPLOYMENT_NAME"],
        name="OpsPilot AI",
        instructions="""You are OpsPilot AI, an operations analyst for small businesses.
You have access to Shopify sales data, Zendesk support tickets, and inventory levels.
When asked a business question, call ALL THREE tools first, then reason across the 
results and give a specific, actionable answer with numbers.
Always cite which data source supports each conclusion.
End every response with a 'Recommended Actions' section.""",
        toolset=toolset
    )

    thread = client.threads.create()
    client.messages.create(
        thread_id=thread.id,
        role="user",
        content=body.question
    )

    run = client.runs.create(
        thread_id=thread.id,
        agent_id=agent.id
    )

    while run.status in ["queued", "in_progress", "requires_action"]:
        time.sleep(1)
        run = client.runs.get(thread_id=thread.id, run_id=run.id)

        if run.status == "requires_action":
            tool_calls = run.required_action.submit_tool_outputs.tool_calls
            tool_outputs = []

            for tc in tool_calls:
                name = tc.function.name
                if name == "shopify_sales_tool":
                    output = shopify_sales_tool()
                elif name == "zendesk_tickets_tool":
                    output = zendesk_tickets_tool()
                elif name == "inventory_status_tool":
                    output = inventory_status_tool()
                else:
                    output = json.dumps({"error": "unknown tool"})

                tool_outputs.append({
                    "tool_call_id": tc.id,
                    "output": output
                })

            client.runs.submit_tool_outputs(
                thread_id=thread.id,
                run_id=run.id,
                tool_outputs=tool_outputs
            )

    response_text = ""
    messages = client.messages.list(thread_id=thread.id)
    for msg in messages:
        if msg.role == "assistant":
            for block in msg.content:
                if hasattr(block, "text"):
                    response_text = block.text.value
            break

    client.delete_agent(agent.id)
    return {"answer": response_text}

@app.get("/")
async def root():
    with open("frontend/index.html") as f:
        return HTMLResponse(f.read())