from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
print(api_key)
client = OpenAI(api_key=api_key)


response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "Listar apenas os nomes dos produdos, sem considerar descrição"
        },
        {
            "role": "user",
            "content": "Liste 3 produtos sustentáveis"
        }
    ],
    model="gpt-4"
)

print(response.choices[0].message.content)
