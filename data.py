import requests
import pandas as pd
url = "https://api.apilayer.com/exchangerates_data/latest"

payload = {}
headers= {
  "apikey": "DRmMSMiitBshSEaGXg22KN9mqYnLEEhJ"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.text
df = pd.read_json(result)
df = df.drop(columns=["success", "timestamp", "base", "date"])
df.to_csv('data.txt')