from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

from test_web.pages.handle_find_exception import handle_exception


class BasePage:
    def __init__(self, driver: str):
        if driver.lower() == 'chrome':
            self.driver = webdriver.Chrome()
        elif driver.lower() == 'firefox':
            self.driver = webdriver.Firefox()
        elif driver.lower() == 'ie':
            self.driver = webdriver.Ie()
        else:
            raise Exception('check browser name')
        self.driver.implicitly_wait(10)

    @handle_exception
    def find(self, by, value=None):
        if value is None:
            ele = self.driver.find_element(*by)
            return ele
        else:
            ele = self.driver.find_element(by, value)
            return ele

    def finds(self, by, value=None):
        if value is None:
            elements = self.driver.find_elements(*by)
            return elements
        else:
            elements = self.driver.find_elements(by, value)
            return elements

    def get_page_source(self):
        return self.driver.page_source

    def get(self, url):
        self.driver.get(url)

    def max_window(self):
        self.driver.maximize_window()

    def quit(self):
        self.driver.quit()
