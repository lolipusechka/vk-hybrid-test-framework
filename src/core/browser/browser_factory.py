import selenium.webdriver.chrome.webdriver
import selenium.webdriver.firefox.webdriver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from src.utils.json_parser import get_config

config = get_config("general.json")


class Factory:
    @staticmethod
    def get_browser():
        browsers = {
            "chrome": Chrome,
            "firefox": Firefox
        }
        return browsers[config["browser"]]


class Chrome:
    @staticmethod
    def create_driver() -> selenium.webdriver.chrome.webdriver.WebDriver:
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=Chrome.__get_options())
        return driver

    @staticmethod
    def __get_options() -> ChromeOptions:
        options = ChromeOptions()
        options.page_load_strategy = config["page_load_strategy"]
        options.headless = config["headless"]
        options.add_argument(f"--window-size={config['window_size']['width']},{config['window_size']['height']}")
        return options


class Firefox:
    @staticmethod
    def create_driver() -> selenium.webdriver.firefox.webdriver.WebDriver:
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=Firefox.__get_options())
        return driver

    @staticmethod
    def __get_options():
        options = FirefoxOptions()
        options.page_load_strategy = config["page_load_strategy"]
        options.headless = config["headless"]
        options.add_argument(f"--width={config['window_size']['width']}")
        options.add_argument(f"--height={config['window_size']['height']}")
        return options
