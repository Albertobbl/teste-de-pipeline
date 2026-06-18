import random
import string


def gerar_senha(
        tamanho=12,
        usar_maiusculas=True,
        usar_numeros=True,
        usar_simbolos=True
):
    caracteres = string.ascii_lowercase

    if usar_maiusculas:
        caracteres += string.ascii_uppercase

    if usar_numeros:
        caracteres += string.digits

    if usar_simbolos:
        caracteres += string.punctuation

    if not caracteres:
        raise ValueError("Nenhum conjunto de caracteres disponível.")

    senha = ''.join(
        random.choice(caracteres)
        for _ in range(tamanho)
    )

    return senha