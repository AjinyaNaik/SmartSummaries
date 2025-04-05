import requests

# API Setup
url = "https://ai.bluehive.com/api/v1/completion"
headers = {
    "Authorization": "Bearer BHSK-sandbox-MCqmIkRAwMit0MEOxoaSaEzfUa6KYC4cbXamMXCs",
    "Content-Type": "application/json"
}

# System Message to define chatbot personality
system_message = "You are a helpful chatbot named Will."

print("💬 Chat with Will (type 'exit' to quit)")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("👋 Goodbye!")
        break

    payload = {
        "prompt": user_input,
        "systemMessage": system_message
    }

    try:
        response = requests.post(url, headers=headers, json=payload)

        if response.status_code == 200:
            data = response.json()
            reply = data["choices"][0]["message"]["content"]
            print("Will:", reply)
        else:
            print(f" API Error [{response.status_code}]:", response.text)

    except Exception as e:
        print("Error during request:", str(e))
