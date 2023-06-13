import requests

url = "http://127.0.0.1:3000/create"  # Replace with your desired URL

# Payload for the POST request
payload = {
    "key1": "value1",
    "key2": "value2"
}

try:
    response = requests.post(url, json=payload)
    response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
    print("Request succeeded. Response:")
    print(response.text)
except requests.exceptions.RequestException as e:
    print("Request failed:", e)
