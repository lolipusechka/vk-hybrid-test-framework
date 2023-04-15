from selenium.webdriver.common.by import By

from src.core.base.base_form import BaseForm
from src.core.element.button import Button
from src.core.element.text_box import Textbox


class LoginPage(BaseForm):
    __input_login = Textbox(By.XPATH, "//input[@id='index_email']", "Login")
    __login_btn = Button(By.XPATH, "//button[contains(@class, 'VkIdForm__signInButton')]/span", "Login Button")

    def __init__(self):
        super().__init__(self.__input_login, "Login Page")

    def sing_in(self, login: str):
        self.__input_login.is_visible()
        self.__input_login.send_text(login)
        self.__login_btn.click_element()
