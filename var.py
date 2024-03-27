import requests
import sys
import os
import json
from output_format import create_item

API_KEY = os.environ.get("api_key")
API_URL = os.environ.get("api_url")
MODEL = os.environ.get("model")
query = sys.argv[1]
format = "蛇形式"


prompt = os.environ.get("prompt")
prompt = prompt.replace("{format}", format)
prompt = prompt.replace("{query}", query)


headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json',
}

data = {
    "messages": [
        {
            "role": "system",
            "content": prompt
        },
    ],
    "model": MODEL
}

response = requests.post(
    API_URL,
    headers=headers,
    json=data
)
result_str = response.json()["choices"][0]["message"]["content"]
result_str_format = create_item(result_str, format)
result_json_str = {"items": result_str_format}
result_json = json.dumps(result_json_str, ensure_ascii=False)

# print(result_str)
print(result_json)
