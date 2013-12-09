from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait


from selenium.webdriver.chrome import webdriver as web_driver_module


class CustomWebDriver(web_driver_module.WebDriver):
    """Our own WebDriver with some helpers added"""

    def find_css(self, css_selector):
        """Shortcut to find elements by CSS. Returns either a list or singleton"""
        elems = self.find_elements_by_css_selector(css_selector)
        found = len(elems)
        if found == 1:
            return elems[0]
        elif not elems:
            raise NoSuchElementException(css_selector)
        return elems

    def wait_for_css(self, css_selector, timeout=7):
        """ Shortcut for WebDriverWait"""
        try:
            return WebDriverWait(self, timeout).until(lambda driver: driver.find_css(css_selector))
        except:
            self.quit()

    def wait(self, timeout=30):
        try:
            return WebDriverWait(self, timeout)
        except:
            self.quit()