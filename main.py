from gerador_senhas.senha import gerar_senha

tamanho = int(input("Tamanho da senha: "))

senha = gerar_senha(tamanho)

print(f"Senha gerada: {senha}")