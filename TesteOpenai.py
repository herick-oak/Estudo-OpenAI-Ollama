#Teste da Biblioteca da Openai para usar LLM e Criar ChatBots
from openai import OpenAI

# Conecta no servidor local do Ollama
client = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio"  # pode ser qualquer string, o Ollama não valida
)

# Faz uma chamada de chat
response = client.chat.completions.create(
    model="llama-3.2-1b-instruct",  # nome do modelo que você puxou no Ollama (ex: "llama2", "mistral", "gemma")
    messages=[
        {"role": "system", "content": "Você é um assistente útil."},
        {"role": "user", "content": "Explique buracos negros em termos simples."}
    ],
    max_tokens=500
)

print(response.choices[0].message.content)