import logging as log
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support import expected_conditions

from src.core.browser.browser import Browser
from src.core.driver.driver_waits import explicit_wait


class Alert:
    @staticmethod
    def alert_accept():
        log.getLogger().info("Accept an alert")
        explicit_wait().until(expected_conditions.alert_is_present()).accept()

    @staticmethod
    def get_text_from_alert() -> str:
        log.getLogger().info("Get text from an alert")
        return explicit_wait().until(expected_conditions.alert_is_present()).text

    @staticmethod
    def alert_send_keys(text: str):
        log.getLogger().info(f"Send text '{text}' to an alert")
        explicit_wait().until(expected_conditions.alert_is_present()).send_keys(text)

    @staticmethod
    def is_alert_display() -> bool:
        log.getLogger().info("Check the visibility of an alert")
        is_true = True
        try:
            Alert.__switch_to_alert()
        except NoAlertPresentException:
            is_true = False
        return is_true

    @staticmethod
    def __switch_to_alert():
        log.getLogger().info("Switch to an alert")
        return Browser.switch_to_alert()
