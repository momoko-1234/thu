annual_spend = 82000.0

if annual_spend >= 100000.0:
    tier = "Platinum"
    discount_rate = 0.15
elif annual_spend >= 50000.0:
    tier = "Gold"
    discount_rate = 0.10
else:
    tier = "Standard"
    discount_rate = 0.0
print(f"Customer Tier: {tier}")

daily_sales = [4200.0, 5100.0, 3900.0, 6200.0]
total_revenue = 0.0
for sale in daily_sales:
    total_revenue += sale
average_sales = total_revenue / len(daily_sales)
print("Total Revenue:", total_revenue)
print("Average Daily Sales:", average_sales)

client = {
"company_name": "Apex Logistics",
"credit_limit_USD": 75000.0,
"outstanding_balance_USD": 23400.0,
}
available_credit = (
    client["credit_limit_USD"]
    - client["outstanding_balance_USD"]
)
print(client["company_name"], available_credit)