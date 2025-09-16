import requests
import json

data = {
    "client": "Nu",
    "product": "Verificación de antecedentes",
    "language": "GoLang",
    "framework": "Gin",
    "auth_method": "Oauth",
}

resp = requests.post(
    "https://sebasxeon.app.n8n.cloud/webhook-test/dfd2c398-9217-4f67-99e8-f9ebebf95d3e",
    json=data,
)
response_data = resp.json()

filename = "test_data.json"

try:
    with open(filename, 'w') as f:
        json.dump(response_data, f, indent=4)
    print(f"Data successfully saved to {filename}")
except IOError as e:
    print(f"Error saving data to file: {e}")