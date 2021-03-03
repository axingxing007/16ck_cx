from appium import webdriver
from appium.webdriver.extensions.android.gsm import GsmCallActions


class TestSearch:
    def setup_class(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "cx"
        caps["appPackage"] = "io.appium.android.apis"
        caps["appActivity"] = ".ApiDemos "
        caps["autoGrantPermissions"] = "true"
        caps['autoAcceptAlerts'] = 'true'
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def test_search(self):
        el2 = self.driver.find_element_by_id("com.xueqiu.android:id/home_search")
        el2.click()
        el3 = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
        el3.send_keys("alibaba")

    def test_gsm_call(self):
        print(self.driver.get_performance_data_types())

    def teardown_class(self):
        self.driver.quit()
