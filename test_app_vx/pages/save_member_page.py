from appium.webdriver.common.mobileby import MobileBy

from test_app_vx.pages.base_page import BasePage


class SaveMemberPage(BasePage):
    __name_ele = (MobileBy.XPATH, "//*[contains(@text, '姓名')]/../*[@text='必填']")
    __sex_select_ele = (MobileBy.XPATH, "//*[contains(@text, '性别')]/../*[@class='android.widget.RelativeLayout']")
    __sex_toast_ele = (MobileBy.XPATH, "//*[@text='女']/../..")
    __mobile_ele = (MobileBy.XPATH, "//*[@text='手机号']")
    __save_ele = (MobileBy.XPATH, "//*[@text='保存']")
    __manually_add_button = (MobileBy.XPATH, "//*[@text='手动输入添加']")
    __name = 'cx'
    __phone_num = '18652992822'

    def add_contact(self):
        """
        添加姓名、性别、手机号/邮箱
        :return:
        """
        # 输入姓名
        self.find_and_send(*self.__name_ele, self.__name)
        # 选择性别
        self.find_and_click(*self.__sex_select_ele)
        self.wait_for(*self.__sex_toast_ele)
        self.find_and_click(*self.__sex_toast_ele)
        # 输入手机号
        self.find_and_send(*self.__mobile_ele, self.__phone_num)
        # 点击保存按钮
        self.find_and_click(*self.__save_ele)
        # 获取添加成功的toast信息，和显示的页面
        return self.get_toast_text(), self.assert_result()

    def assert_result(self):
        text = self.get_ele_text(*self.__manually_add_button)
        return text
