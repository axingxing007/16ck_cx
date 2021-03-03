from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestApiDemo:
    def setup_class(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "cx"
        caps["appPackage"] = "io.appium.android.apis"
        caps["appActivity"] = ".ApiDemos "
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def test_toast(self):
        # 点击Views
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID, 'Views').click()
        # 使用android滑动方法
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector().'
                                 'scrollable(true).instance(0)).''scrollIntoView(new UiSelector().'
                                 'text("Popup Menu").instance(0));'
                                 ).click()
        # 点击Make a Popup!
        self.driver.find_element(MobileBy.XPATH, "//*[@text='Make a Popup!']").click()
        # 点击Search
        self.driver.find_element(MobileBy.XPATH, "//*[@text='Search']").click()
        # 打印toast信息
        print(self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text)

    def teardown_class(self):
        self.driver.quit()
