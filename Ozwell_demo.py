import requests

# Function to read the API key from a file
def get_api_key():
    try:
        with open(".env", "r") as file:
            # Assuming the file contains the API key in a line like 'API_KEY=your_key'
            return file.read().strip().split("=")[1]
    except Exception as e:
        print(f"Error reading the API key: {e}")
        return None

# API Setup
url = "https://ai.bluehive.com/api/v1/completion"
api_key = get_api_key()

# Make sure the API key is loaded correctly
if api_key is None:
    print("API Key not found. Exiting.")
    exit(1)

headers = {
    "Authorization": f"Bearer {api_key}",
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
            print(f"API Error [{response.status_code}]:", response.text)

    except Exception as e:
        print("Error during request:", str(e))
