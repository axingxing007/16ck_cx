from appium.webdriver.common.mobileby import MobileBy

from test_app_vx.pages.base_page import BasePage
from test_app_xueqiu.pages.market_page import MarketPage


class MainPage(BasePage):
    __login_button = (MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/post_status']")
    __market_button = (MobileBy.XPATH, "//*[@resource-id='android:id/tabs']//*[@text='行情']")

    def goto_market(self):
        """点击底部的行情tab，进入到行情页面"""
        self.find_and_click(*self.__login_button)
        self.find_and_click(*self.__market_button)
        return MarketPage(self.driver)
