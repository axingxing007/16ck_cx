from appium.webdriver.common.mobileby import MobileBy

from test_app_vx.pages.base_page import BasePage


class Daka(BasePage):
    __work_daka = (MobileBy.XPATH, "//*[@text='上下班打卡']")
    __outer_daka = (MobileBy.XPATH, "//*[@text='外出打卡']")
    __daba_button = (MobileBy.XPATH, "//*[contains(@text, '次外出')]")
    __success_daka = (MobileBy.XPATH, "//*[@text='外出打卡成功']")

    def click_work_daka_buttom(self):
        """点击上下班打卡tab，进入上下班打卡页面"""
        pass

    def click_outer_daka_button(self):
        """1、点击外出打卡tab；2、点击打卡按钮"""
        self.find_and_click(*self.__outer_daka)
        self.find_and_click(*self.__daba_button)
        self.wait_for(*self.__success_daka)
        return self.get_ele_text(*self.__success_daka)
