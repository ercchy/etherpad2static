from webdriver import CustomWebDriver


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
