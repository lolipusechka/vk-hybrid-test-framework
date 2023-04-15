import logging as log

from src.core.driver.driver import Driver


class Browser:
    original_window = Driver.get_instance().current_window_handle

    @staticmethod
    def switch_to_new_window_tab():
        if len(Driver.get_instance().window_handles) > 1:
            log.getLogger().info("Switch to the new windows/tab")
            for window_handle in Driver.get_instance().window_handles:
                if window_handle != Browser.original_window:
                    Driver.get_instance().switch_to.window(window_handle)
                    break
        else:
            log.getLogger().error("There is no new window/tab")

    @staticmethod
    def close_tab_or_window_and_switch_to_original_window():
        log.getLogger().info("Close new tab and switch to the original window/tab")
        Driver.get_instance().close()
        Driver.get_instance().switch_to.window(Browser.original_window)

    @staticmethod
    def switch_to_original_window():
        log.getLogger().info("Switch to the original window/tab")
        Driver.get_instance().switch_to.window(Browser.original_window)

    @staticmethod
    def switch_to_frame(iframe):
        log.getLogger().info("Switch to the frame")
        Driver.get_instance().switch_to.frame(iframe)

    @staticmethod
    def switch_to_default_content():
        log.getLogger().info("Switch to default content")
        Driver.get_instance().switch_to.default_content()

    @staticmethod
    def go_back():
        log.getLogger().info("Go back")
        Driver.get_instance().back()

    @staticmethod
    def go_forward():
        log.getLogger().info("Go forward")
        Driver.get_instance().forward()

    @staticmethod
    def refresh_page():
        log.getLogger().info("Go forward")
        Driver.get_instance().refresh()

    @staticmethod
    def go_to(url: str):
        log.getLogger().info(f"Go to {url}")
        Driver.get_instance().get(url)

    @staticmethod
    def get_current_url() -> str:
        return Driver.get_instance().current_url

    @staticmethod
    def switch_to_alert():
        return Driver.get_instance().switch_to.alert

    @staticmethod
    def scroll_to_element(web_element, name):
        log.getLogger().info(f"Scroll to element '{name}'")
        Driver.get_instance().execute_script("arguments[0].scrollIntoView(true);", web_element)
