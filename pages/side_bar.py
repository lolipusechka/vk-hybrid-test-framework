from selenium.webdriver.common.by import By

from src.core.base.base_form import BaseForm
from src.core.element.button import Button
from src.core.element.label import Label


class SideBar(BaseForm):
    __uniq_element = Label(By.XPATH, "//li[@id='l_pr']", "Unique element")
    __btn_my_profile = Button(By.XPATH, "//li[@id='l_pr']", "My Profile")

    def __init__(self):
        super().__init__(self.__uniq_element, "Side Bar")

    def click_ob_btn_my_profile(self):
        self.__btn_my_profile.wait_for_clickable()
        self.__btn_my_profile.click_element()
