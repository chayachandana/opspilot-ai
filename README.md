# ⚡ OpsPilot AI

> An AI-powered Forward Deployed Engineer for small businesses — built for the Agents League Hackathon 2026.

[![Agents League 2026](https://img.shields.io/badge/Agents%20League-2026-blue)](https://agentsleague.devpost.com)
[![Track](https://img.shields.io/badge/Track-Enterprise%20Agents-purple)]()
[![Microsoft Foundry IQ](https://img.shields.io/badge/Microsoft-Foundry%20IQ-0078D4)]()

## 🚩 The Problem

Small businesses have data everywhere:
- Shopify sales numbers
- Zendesk support tickets
- Inventory spreadsheets

But nobody knows:
- Why did sales drop this week?
- Which products need reordering?
- Which customers are unhappy?

They can't afford a data analyst. They don't have time to connect the dots manually.

## 💡 The Solution

**OpsPilot AI acts as a Forward Deployed AI Engineer for small businesses.**

Ask it a business question in plain English. It automatically pulls from all your data sources, reasons across them, and gives you specific recommendations with numbers — in seconds.

## 🎯 Live Example

**You ask:**
```
Why did sales drop this week?
```

**OpsPilot answers:**
> Sales dropped 18.2% because the Lavender Diffuser (SKU-1142) hit zero stock on June 8, causing 23 unfulfilled orders. Zendesk out-of-stock complaints spiked from 8 to 29 tickets (+262%). Recommended: reorder 58 units immediately, notify waitlisted customers, and pause low-ROAS ads.

## 🧠 How It Works

```
User Question
     ↓
FastAPI Backend
     ↓
Azure AI Foundry Agent (GPT-4.1-mini)
     ↓
Automatic Tool Calling
  ├── 🛍️  Shopify Sales Tool
  ├── 🎫  Zendesk Tickets Tool
  └── 📦  Inventory Status Tool
     ↓
Reasoned Analysis + Recommended Actions
```

## 💡 Microsoft IQ Integration

Built on **Foundry IQ** using:
- Azure AI Foundry Agent Service
- GPT-4.1-mini with multi-tool calling
- Automatic agent orchestration across data sources
- Tool calling with real-time data retrieval

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Agent | Azure AI Foundry (Foundry IQ) |
| Model | GPT-4.1-mini |
| Backend | Python + FastAPI |
| Frontend | HTML / CSS / JS |
| Auth | Azure DefaultAzureCredential |

## 🚀 How to Run

1. Clone the repo:
```bash
git clone https://github.com/chayachandana/opspilot-ai.git
cd opspilot-ai
```

2. Install dependencies:
```bash
pip install azure-ai-agents azure-ai-projects azure-identity fastapi uvicorn python-dotenv
```

3. Create a `.env` file:
```
PROJECT_ENDPOINT=your_azure_foundry_endpoint
MODEL_DEPLOYMENT_NAME=gpt-4.1-mini
```

4. Run the app:
```bash
uvicorn main:app --reload
```

5. Open your browser at `http://localhost:8000`

## 💬 Demo Questions

- "Why did sales drop this week?"
- "Which products need to be reordered?"
- "What are customers complaining about?"

## 🏆 What Makes This Different

Most AI tools give generic answers. OpsPilot:
- **Reasons across multiple data sources** in a single query
- **Cites its sources** — every conclusion backed by data
- **Gives specific numbers** — not "sales dropped" but "sales dropped 18.2%"
- **Recommends exact actions** — not "reorder stock" but "reorder 58 units of SKU-1142"

## 👤 Built By

**Chaya Chandana**
[GitHub](https://github.com/chayachandana) · [LinkedIn](https://www.linkedin.com/in/chayachandana/)

---
*Built for Agents League Hackathon 2026 — Enterprise Agents Track*