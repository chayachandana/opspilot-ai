import json

def get_zendesk_tickets():
    with open("data/zendesk.json") as f:
        data = json.load(f)
    
    total_change = ((data["total_tickets"]["this_week"] - 
                     data["total_tickets"]["last_week"]) / 
                     data["total_tickets"]["last_week"] * 100)
    
    spikes = []
    for cat in data["categories"]:
        if cat["count_this_week"] > cat["count_last_week"]:
            spikes.append({
                "type": cat["type"],
                "this_week": cat["count_this_week"],
                "last_week": cat["count_last_week"]
            })
    
    return {
        "total_tickets_this_week": data["total_tickets"]["this_week"],
        "total_tickets_last_week": data["total_tickets"]["last_week"],
        "total_change_pct": round(total_change, 1),
        "spiking_categories": spikes,
        "sample_tickets": data["sample_tickets"][:3]
    }