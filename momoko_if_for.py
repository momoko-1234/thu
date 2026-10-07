daily_sales = [4200.0, 5100.0, 3900.0, 6200.0, 7800.0, 8400.0, 4900.0]

for sale in daily_sales:
    if sale <= 3000:
        print("Bad")
    elif sale <= 5000:
        print("Normal")
    else:
        print("Good")

clients = [
    {"id": "CUST-101", "name": "Lily", "segment": "Retail", "spend": 145000.0, "risk": 15},
    {"id": "CUST-102", "name": "John", "segment": "Technology", "spend": 82000.0, "risk": 22},
    {"id": "CUST-103", "name": "Kate", "segment": "Healthcare", "spend": 31000.0, "risk": 38},
    {"id": "CUST-104", "name": "Mike", "segment": "Finance", "spend": 215000.0, "risk": 12},
    {"id": "CUST-105", "name": "Judy", "segment": "Manufacturing", "spend": 64000.0, "risk": 45}
]

for c in clients:
# Tiering logic based on annual purchase volume
    if c["spend"] >= 100000.0 and c["risk"] < 30:
        c["tier"] = "Platinum"
        c["credit_limit"] = c["spend"] * 0.40
    elif c["spend"] >= 50000.0 and c["risk"] < 50:
        c["tier"] = "Gold"
        c["credit_limit"] = c["spend"] * 0.25
    else:
        c["tier"] = "Standard"
        c["credit_limit"] = c["spend"] * 0.10

    print(f"Client {c['id']}: ({c['segment']}): Name= {c['name']}  Tier={c['tier']} | Credit Limit=${c['credit_limit']:,.2f}")