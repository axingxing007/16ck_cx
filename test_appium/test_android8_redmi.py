import os
import time

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestRedMi:
    def setup(self):
        caps = {}
        # 支持X5内核应用的自动化配置
        # caps["recreateChromeDriverSessions"] = True
        caps['platformName'] = 'android'
        caps['deviceName'] = 'cx'
        caps['appPackage'] = 'com.tencent.mm'
        caps['appActivity'] = '.ui.LauncherUI'
        caps['noReset'] = True
        # caps['recreateChromeDriverSessions'] = True
        # caps["browserName"] = ""
        # caps['newCommandTimeout'] = 0
        caps['chromedriverExecutableDir'] = r"D:\appium_chrome_driver"
        # 小程序的进程名称
        caps['chromeOptions'] = {'androidProcess': 'com.tencent.mm:appbrand0'}
        # caps['adbPort'] = 5039
        caps['unicodeKeyboard'] = True  # 支持输入中文
        caps['resetKeyboard'] = True
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
        self.driver.implicitly_wait(15)

    def test_wechat(self):
        # 显式等待为了进入到微信主界面，一定要有!!!
        WebDriverWait(self.driver, 30).until(
            expected_conditions.visibility_of_element_located(
                (MobileBy.XPATH, "//*[@text='通讯录']")
            )
        )
        print(self.driver.contexts)
        search_button = self.driver.find_element(MobileBy.ID, "he6")
        search_button.click()
        # 输入框
        send = self.driver.find_element(MobileBy.ID, "bxz")
        send.send_keys('雪球')
        # 点击带出来的小程序，点击第一个
        self.driver.find_element(MobileBy.ID, "ir3").click()
        contexts = self.driver.contexts
        print(contexts)
        list_1 = []
        # 遍历上下文
        for context in contexts:
            if 'appbrand0' in context.lower():
                print(context)
                list_1.append(context)
        print('遍历成功', list_1[0])
        # 跳转到小程序h5页面
        self.driver._switch_to.context(list_1[0])
        print(f'当前页面的上下文为：{self.driver.context}')
        # 遍历窗口
        windows1 = self.driver.window_handles
        print(windows1)
        # 跳转到搜索股票的H5页面
        for window in windows1:
            self.driver._switch_to.window(window)
            if "上证指数 " in self.driver.page_source:
                self.driver._switch_to.window(window)
                print(f'当前的窗口为：{window}')

        # 显式等待添加按钮
        WebDriverWait(self.driver, 15).until(
            expected_conditions.element_to_be_clickable(
                (MobileBy.XPATH, "//*[@class='_a data-v-5667385e']//div")
            )
        )
        # 点击添加按钮
        self.driver.find_element(MobileBy.XPATH, "//*[@class='_a data-v-5667385e']//div").click()
        print(self.driver.window_handles)
        time.sleep(5)
        try:
            WebDriverWait(self.driver, 20).until(lambda x: len(self.driver.window_handles) >= 2)
        except Exception as e:
            print(e)
        windows2 = self.driver.window_handles
        print(f'windows2：{windows2}，窗口的数目是：{len(windows2)}')
        list_2 = []
        for i in windows2:
            self.driver._switch_to.window(i)
            with open('aa.txt', 'w', encoding='utf-8') as f_obj:
                f_obj.write(self.driver.page_source + '\n\n\n')
            if "热搜股票" in self.driver.page_source:
                list_2.append(i)
                self.driver._switch_to.window(i)
                print(f'当前的窗口为：{i}', self.driver.context, list_2[0])
        self.driver._switch_to.context('NATIVE_APP')
        # ele.send_keys('alibaba')  # 小程序中不支持元素的send_keys方法
        ActionChains(self.driver).send_keys('alibaba').perform()
        self.driver._switch_to.context('WEBVIEW_com.tencent.mm:appbrand0')
        self.driver._switch_to.window(list_2[0])
        time.sleep(5)
        print(f'股票页面的上下文为：{self.driver.context}，当前窗口的句柄为：{self.driver.current_window_handle}')
        # print(self.driver.page_source)
        self.driver.find_element(MobileBy.XPATH, "//wx-view[@data-eventid='3-0']/wx-view[1]")
        self.driver.find_element(MobileBy.XPATH, "//wx-view[@data-eventid='3-0']/wx-view[1]").click()
        time.sleep(5)
        # 截图
        file_name = time.strftime("%Y-%m-%d-%H-%M-%S-%p") + '.png'
        file_path = os.path.dirname(__file__) + '/picture_dir/' + file_name
        self.driver.save_screenshot(file_path)

    def teardown(self):
        pass
        # self.driver.terminate_app('com.tencent.mm')
        # self.driver.quit()
