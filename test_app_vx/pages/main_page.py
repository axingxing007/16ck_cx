from appium.webdriver.common.mobileby import MobileBy

from test_app_vx.pages.base_page import BasePage
from test_app_vx.pages.bench_page import BenchPage
from test_app_vx.pages.contact_page import ContactPage


class MainPage(BasePage):
    __contact_button = (MobileBy.XPATH, "//*[@text='通讯录']")
    __bench_button = (MobileBy.XPATH, "//*[@text='工作台']")

    def goto_add_member_page(self):
        """点击底部的通讯录按钮，进入到通讯录页面"""
        self.find_and_click(*self.__contact_button)
        return ContactPage(self.driver)

    def goto_bench(self):
        """
        点击底部的工作台按钮，进入到工作台页面
        :return:
        """
        self.find_and_click(*self.__bench_button)
        return BenchPage(self.driver)
