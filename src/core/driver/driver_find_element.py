from src.core.driver.driver import Driver


def find_element(by, locator):
    return Driver.get_instance().find_element(by, locator)


def find_elements(by, locator):
    return Driver.get_instance().find_elements(by, locator)
