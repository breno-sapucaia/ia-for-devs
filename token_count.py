import tiktoken

model = "gpt-4"
coder = tiktoken.encoding_for_model(model)


token_list = coder.encode("Olá, como você está?")

print("Lista de tokens: ", token_list)
print("Quantidade de tokens: ", len(token_list))
print(f"Custo para o modelo {model} é de ${(len(token_list)/1000) * 0.03}")


model = "gpt-4o-mini"
coder = tiktoken.encoding_for_model(model)

token_list = coder.encode("Olá, como você está?")

print("Lista de tokens: ", token_list)
print("Quantidade de tokens: ", len(token_list))
print(f"Custo para o modelo {model} é de ${(len(token_list)/1000) * 0.0015}")


model = "gpt-4o"
coder = tiktoken.encoding_for_model(model)

token_list = coder.encode("Olá, como você está?")

print("Lista de tokens: ", token_list)
print("Quantidade de tokens: ", len(token_list))
print(f"Custo para o modelo {model} é de ${(len(token_list)/1000) * 0.03}")

