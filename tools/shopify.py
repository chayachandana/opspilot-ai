import json

def get_shopify_sales():
    with open("data/shopify.json") as f:
        data = json.load(f)
    
    weeks = data["weekly_sales"]
    this_week = weeks[-1]
    last_week = weeks[-2]
    
    revenue_change = ((this_week["revenue"] - last_week["revenue"]) 
                      / last_week["revenue"] * 100)
    
    declining = []
    for p in data["products"]:
        change = p["orders_this_week"] - p["orders_last_week"]
        declining.append({
            "product": p["name"],
            "sku": p["sku"],
            "order_change": change,
            "orders_this_week": p["orders_this_week"]
        })
    declining.sort(key=lambda x: x["order_change"])
    
    return {
        "revenue_this_week": this_week["revenue"],
        "revenue_last_week": last_week["revenue"],
        "revenue_change_pct": round(revenue_change, 1),
        "orders_this_week": this_week["orders"],
        "orders_last_week": last_week["orders"],
        "most_declined_products": declining[:2]
    }