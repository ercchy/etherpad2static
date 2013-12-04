from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

#determine the WebDriver module. default to Firefox

from selenium.webdriver.chrome import webdriver as web_driver_module


class CustomWebDriver(web_driver_module.WebDriver):
    """Our own WebDriver with some helpers added"""

    def find_css(self, css_selector):
        """Shortcut to find elements by CSS. Returns either a list or singleton"""
        elems = self.find_elements_by_css_selector(css_selector)
        found = len(elems)
        print 'found %s elements (%s)' % (found, css_selector)
        if found == 1:
            return elems[0]
        elif not elems:
            return None #raise NoSuchElementException(css_selector)
        return elems

    def wait_for_css(self, css_selector, timeout=10):
        """ Shortcut for WebDriverWait"""
        try:
            return WebDriverWait(self, timeout).until(lambda driver: driver.find_css(css_selector))
        except:
            self.quit()


def get_file_list():
    f = open('pads.txt')
    lines = [line.strip('\n') for line in f]
    f.close()
    return lines


def list_urls():
    urls = []
    for url in get_file_list():
        urls.append('http://pad.p2pu.org/p/{0}'.format(url))

    return urls


def run_test():

    #url_list = list_urls()

    driver = CustomWebDriver()
    driver.implicitly_wait(30)
    driver.get('http://pad.p2pu.org/p/*contentparty')

    body = driver.wait_for_css('.readwrite')
    print body.__dict__
    pane = driver.find_css('#importexportlink')
    print pane.__dict__
    pane.click()
    driver.wait_for_css('#exporthtml')

    elem = driver.find_css('#exporthtmla')
    print elem.__dict__

    driver.execute_script('$("#exporthtmla").delay(10).click();')
    #elem.click()

    driver.close()


def main():

    run_test()

if __name__ == '__main__':
    main()
