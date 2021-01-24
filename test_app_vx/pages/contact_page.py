from test_app_vx.pages.add_member_page import AddMemberPage
from test_app_vx.pages.base_page import BasePage


class ContactPage(BasePage):
    __add_member_text = '添加成员'

    def click__add_member(self):
        """
        点击添加成员，进入到添加成员页面
        :return:
        """
        self.scroll_find_and_click(self.__add_member_text)
        return AddMemberPage(self.driver)
