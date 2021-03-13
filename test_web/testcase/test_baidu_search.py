from selenium.webdriver.common.by import By
from test_web.pages.base_page import BasePage


class TestBaiDuSearch:
    __login_button = (By.CSS_SELECTOR, "#u1 > a")
    __search_input = (By.CSS_SELECTOR, "input#kw")
    __submit_button = (By.CSS_SELECTOR, "input#su123")

    def setup_class(self):
        self.bp = BasePage('chrome')
        self.bp.get("http://www.baidu.com")
        self.bp.max_window()

    def test_search(self):
        self.bp.find(self.__login_button).click()
        # self.bp.find(self.__search_input).send_keys('selenium')
        print(self.bp.find(self.__submit_button).get_attribute('value'))

    def teardown_class(self):
        self.bp.quit()
