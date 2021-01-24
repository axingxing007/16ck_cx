from appium.webdriver.common.mobileby import MobileBy
from test_app_vx.pages.base_page import BasePage
from test_app_vx.pages.daka_page import Daka


class BenchPage(BasePage):
    __daka_icon = (MobileBy.XPATH, "//*[@text='打卡']")

    def click_daka_icon(self):
        """
        点击打卡的icon，进入到打卡页面
        :return:
        """
        self.swipe_find_and_click(*self.__daka_icon)
        return Daka(self.driver)
