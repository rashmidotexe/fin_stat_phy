import requests
import pandas as pd

# Assuming an API endpoint for the financial data
url = "https://api.financialdata.com/order_flow"
response = requests.get(url)
data = response.json()

# Convert to pandas DataFrame for easier manipulation
order_flow_data = pd.DataFrame(data)
order_flow_data.to_csv("data/order_flow_data.csv")
