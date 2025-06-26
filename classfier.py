from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
model = "gpt-4"


def classify_product(product_name, categories):
    prompt_system = f"""
            Você é um categorizador de produtos.
            Você deve assumir as categorias presentes na lista abaixo.

            # Lista de Categorias Válidas
            {categories.split(",")}
            # Formato da Saída
            Produto: Nome do Produto
            Categoria: apresente a categoria do produto

            # Exemplo de Saída
            Produto: Escova elétrica com recarga solar
            Categoria: Eletrônicos Verdes
        """

    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": prompt_system
            },
            {
                "role": "user",
                "content": product_name
            }
        ],
        model=model,
        temperature=0,
        max_tokens=200,
    )
    return response.choices[0].message.content


valid_categories = input("Digite as categorias separadas por vírgula: ")


while True:
    nome_produto = input("Digite o nome de um produto: ")
    response = classify_product(nome_produto, valid_categories)
    print(response)
