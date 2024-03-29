import requests
import sys
import os
import json
from output_format import create_items

def main():
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

    result_items = create_items(result_str, MODEL)

    result_json_str = {"items": result_items}
    result_json = json.dumps(result_json_str, ensure_ascii=False)

    # 输出为Alfred item
    print(result_json)

if __name__=="__main__":
    main()