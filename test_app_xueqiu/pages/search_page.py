from appium.webdriver.common.mobileby import MobileBy

from test_app_vx.pages.base_page import BasePage


class SearchPage(BasePage):
    __kw = (MobileBy.ID, "com.xueqiu.android:id/search_input_text")

    def search(self):
        return self.find_and_send(*self.__kw, 'alibaba')
