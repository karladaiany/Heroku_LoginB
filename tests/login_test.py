import pytest
from pages import login_page


# um padrão para o PyTest executar no início e no final dos testes
@pytest.fixture
def login(driver):  # após criação do conftest, deixou de receber a request para receber a função driver
    return login_page.LoginPage(driver)  # após criação do conftest, deixa de ser loginPage e instanciamos a classe
    # LoginPage e passando a função driver, que é o nosso Selenium turbinado


def testar_login_com_sucesso(login):
    # Faça o login com este usuário e senha
    login.com_('tomsmith', 'SuperSecretPassword!')
    # Validar o resultado = mensagem de sucesso
    assert login.vejo_mensagem_de_sucesso()


def testar_login_com_usuario_invalido(login):
    login.com_('juca', 'SuperSecretPassword!')
    assert login.vejo_mensagem_de_falha()


def testar_login_com_senha_invalida(login):
    login.com_('tomsmith', 'xpto1234')
    assert login.vejo_mensagem_de_falha()
