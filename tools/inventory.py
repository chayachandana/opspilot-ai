import json

def get_inventory_status():
    with open("data/inventory.json") as f:
        data = json.load(f)
    
    alerts = []
    for p in data["products"]:
        if p["status"] == "OUT OF STOCK":
            alerts.append({
                "product": p["name"],
                "sku": p["sku"],
                "stock": p["stock"],
                "status": p["status"],
                "units_sold_30d": p["units_sold_30d"],
                "suggested_reorder": round(p["units_sold_30d"] / 30 * 14)
            })
        elif p["stock"] <= p["reorder_point"]:
            alerts.append({
                "product": p["name"],
                "sku": p["sku"],
                "stock": p["stock"],
                "status": "LOW STOCK",
                "units_sold_30d": p["units_sold_30d"],
                "suggested_reorder": round(p["units_sold_30d"] / 30 * 14)
            })
    
    return {
        "total_products": len(data["products"]),
        "alerts": alerts,
        "all_products": data["products"]
    }