import pytest
import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_appium.pages.test_step import TestData


class TestSearch:
    def setup(self):
        caps = {}
        # 排序invalid argument
        caps['chromeOptions'] = {'w3c': False}
        # caps['showChromedriverLog'] = True
        caps["platformName"] = "android"
        caps["deviceName"] = "cx"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["autoGrantPermissions"] = "true"
        caps['autoAcceptAlerts'] = 'true'
        # 连接真机的唯一设备号
        caps['udid'] = 'emulator-5554'
        # 配置chromedriver的目录
        caps['chromedriverExecutableDir'] = r"D:\appium_chrome_driver"
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(15)

        def loaded(driver):
            if len(self.driver.find_elements(MobileBy.XPATH, '//*[@text="同意"]')) >= 1:
                self.driver.find_element(MobileBy.XPATH, '//*[@text="同意"]').click()
                return True
            else:
                return False

        WebDriverWait(self.driver, 15).until(loaded)

    # 参数化
    @pytest.mark.parametrize('keyword, expected_price', [['pdd', 10], ['alibaba', 100]])
    def test_search(self, keyword, expected_price):
        el2 = self.driver.find_element(MobileBy.ID, "home_search")
        el2.click()
        el3 = self.driver.find_element(MobileBy.ID, "search_input_text")
        el3.send_keys(keyword)
        self.driver.find_element(MobileBy.ID, 'name').click()
        ele = self.driver.find_element(MobileBy.ID, 'current_price')
        pytest.assume(float(ele.text) > expected_price)
        # ele = self.driver.find_element(MobileBy.ID, "search_input_text")
        # print(ele.get_attribute('text'))
        # print(ele.get_attribute('class'))
        # print(ele.get_attribute('package'))
        # print(ele.get_attribute('bounds'))

    # 数据驱动
    @pytest.mark.parametrize('keyword, expected_price', yaml.safe_load(open('search.yml', 'r')))
    def test_search_from_yaml(self, keyword, expected_price):
        el2 = self.driver.find_element(MobileBy.ID, "home_search")
        el2.click()
        el3 = self.driver.find_element(MobileBy.ID, "search_input_text")
        el3.send_keys(keyword)
        self.driver.find_element(MobileBy.ID, 'name').click()
        ele = self.driver.find_element(MobileBy.ID, 'current_price')
        pytest.assume(float(ele.text) > expected_price)

    # 测试步骤驱动
    def test_search_from_steps(self):
        TestData('data.yaml').run(self.driver)

    # 测试webview
    def test_webview01(self):
        """测试混合app两个h5之间的跳转"""
        ele = self.driver.find_element(MobileBy.XPATH, "//*[@text='交易']")
        ele.click()
        contexts1 = self.driver.contexts
        print(contexts1)
        for i in contexts1:
            if "webview" in i.lower():
                print(i)
                # 跳转到h5页面
                self.driver._switch_to.context(i)
                # windows1 = set(self.driver.window_handles)
                # 点击A股开户
                self.driver.find_element(MobileBy.XPATH, "//h1[text()='A股开户']").click()
                print('点击A股开户成功')
                list1 = []
                for window in self.driver.window_handles:
                    self.driver._switch_to.window(window)
                    if self.driver.title == "平安证券 极速开户":
                        list1.append(window)
                # windows2 = set(self.driver.window_handles)
                # set1 = windows2 - windows1
                self.driver._switch_to.window(list1[0])
                print(f'当前窗口的标题是：{self.driver.title}')
                print(f'当前窗口的编号为：{self.driver.current_window_handle}')
                WebDriverWait(self.driver, 10).until(
                    expected_conditions.visibility_of_element_located(
                        (By.ID, "phone-number")
                    )
                )
                # 输入手机号码
                ele = self.driver.find_element(By.CSS_SELECTOR, "#phone-number")
                ele.send_keys('18652992812')

    def test_webview02(self):
        ele = self.driver.find_element(MobileBy.XPATH, "//*[@text='交易']")
        ele.click()
        # 点击A股开户
        self.driver.find_element(MobileBy.XPATH, "//*[@text='A股开户']").click()
        contexts3 = self.driver.contexts
        print(self.driver.contexts)
        for k in contexts3:
            if 'webview' in k.lower():
                print(k)
                # 跳转到h5页面
                self.driver.switch_to.context(k)
                print(f'进入平安证券：{self.driver.current_context}')
                # 显示等待
                WebDriverWait(self.driver, 20).until(
                    expected_conditions.visibility_of_element_located(
                        (By.ID, "phone-number")
                    )
                )
                # 输入手机号码
                ele = self.driver.find_element(By.CSS_SELECTOR, "#phone-number")
                ele.send_keys('18652992812')

    def test01(self):
        pass

    def teardown(self):
        self.driver.quit()
