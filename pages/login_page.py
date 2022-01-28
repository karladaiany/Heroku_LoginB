from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    _username_input = {'by': By.ID, 'value': 'username'}
    _password_input = {'by': By.ID, 'value': 'password'}
    _submit_button = {'by': By.CSS_SELECTOR, 'value': 'button.radius'}
    _failure_message = {'by': By.CSS_SELECTOR, 'value': '.flash.error'}
    _success_message = {'by': By.CSS_SELECTOR, 'value': '.flash.success'}
    _login_form = {'by': By.ID, 'value': 'login'}

    # ações possíveis na página

    # método de inicialização
    def __init__(self, driver):
        # inicializa o Selenium
        self.driver = driver
        #  abre a página que será testada
        self._visitar('http://the-internet.herokuapp.com/login')
        # verificar se o elemento formulário de login está visível
        assert self._esta_visivel(self._login_form)

    # método que irá realizar o login COM usuário e senha fornecidos
    def com_(self, username, password):
        # forma convencional
        # self.driver.find_element(By.ID, 'username').send_keys('tomsmith')

        # forma em Page Objects
        # Ação              Onde           Texto/Valor
        # Ex: Digitar       Elemento           |
        #        |              |              |
        #        V              V              V
        self._digitar(self._username_input, username)

        # digitar a senha
        self._digitar(self._password_input, password)

        # clicar no botão de Login
        self._clicar(self._submit_button)

    # função para validar se é exibida a mensagem de sucesso
    def success_message_present(self):
        return self._esta_visivel(self._success_message, 5)

    # função para validar se é exibida a mensagem de falha, em razão do usuário
    def failure_message_present(self):
        return self._esta_visivel(self._failure_message, 5)
