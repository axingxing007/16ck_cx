from appium.webdriver.common.mobileby import MobileBy
from test_app_vx.pages.base_page import BasePage
from test_app_vx.pages.save_member_page import SaveMemberPage


class AddMemberPage(BasePage):
    __manually_add_button = (MobileBy.XPATH, "//*[@text='手动输入添加']")

    def click_manually_add_member(self):
        """
        点击手动输入添加元素，进入手动添加页面
        """
        self.find_and_click(*self.__manually_add_button)
        return SaveMemberPage(self.driver)
