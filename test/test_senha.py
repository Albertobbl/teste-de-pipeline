from gerador_senhas.senha import gerar_senha


def test_tamanho_da_senha():
    senha = gerar_senha(16)

    assert len(senha) == 16


def test_retorna_string():
    senha = gerar_senha()

    assert isinstance(senha, str)


def test_senha_vazia():
    senha = gerar_senha(0)

    assert senha == ""