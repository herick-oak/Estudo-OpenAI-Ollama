from openai import OpenAI

client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

conversations = [{"role": "system", "content": "You'll speak like yoda in all of yours answers"}]

def generate(text):
    global conversations
    conversations.append({"role": "user", "content": text})
    c = client.chat.completions.create(model="model-indetifier", messages=conversations,temperature=0.7)
    response = c.choices[0].message
    conversations.append({"role": response.role, "content": response.content})
    return response.content

while True:
    user_input = str(input("You: "))
    if user_input.lower() == "exit":
        break
    response = generate(user_input)
    print(f"Assistante: {response}")