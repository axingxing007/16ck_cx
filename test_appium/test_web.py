from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestSearch:
    def setup(self):
        caps = {}
        caps['chromeOptions'] = {'w3c': False}
        caps["platformName"] = "android"
        # caps["deviceName"] = "cx"
        # 设置浏览器名称
        caps['browserName'] = 'chrome'
        # 配置chromedriver的目录
        caps['chromedriverExecutableDir'] = r"D:\appium_chrome_driver"
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def test_search(self):
        self.driver.get('https://testerhome.com/')
        # print(self.driver.contexts)
        # self.driver._switch_to.context('CHROMIUM')
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(
                (MobileBy.XPATH, '//*[@id="mobile-search-form"]/input')
            )
        )
        self.driver.find_element(By.XPATH, '//*[@id="mobile-search-form"]/input').send_keys('appium')

    def teardown(self):
        self.driver.quit()
