from appium.webdriver.common.mobileby import MobileBy

from test_app_vx.pages.base_page import BasePage
from test_app_xueqiu.pages.search_page import SearchPage


class MarketPage(BasePage):
    __search_button = (MobileBy.ID, "com.xueqiu.android:id/action_search")

    def goto_search(self):
        self.find_and_click(*self.__search_button)
        return SearchPage(self.driver)
