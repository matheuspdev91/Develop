import requests

payload = {
    "model": "qwen3:latest",
    "messages": [
        {
            "role": "user",
            "content": "Responda apenas: OK"
        }
    ],
    "stream": False,
}

response = requests.post(
    "http://127.0.0.1:11434/api/chat",
    json=payload,
    timeout=120,
)

print(response.status_code)
print(response.json())