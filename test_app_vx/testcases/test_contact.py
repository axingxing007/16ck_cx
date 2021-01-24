from test_app_vx.pages.app import App


class TestContact:
    def setup_class(self):
        self.app = App()
        self.app.start()

    def teardown_class(self):
        self.app.stop()

    def test_add_contact(self):
        """
        1、点击通讯录；2、点击添加成员；
        3、点击手动添加；4、输入必要信息，点击保存；5、断言
        :return:
        """
        result = self.app.goto_main().goto_add_member_page(). \
            click__add_member().click_manually_add_member(). \
            add_contact()

        assert result[0] == '添加成功', '断言弹窗的文本是否等于添加成功'
        assert result[1] == '手动输入添加', '断言保存成功是否在添加成员页面'
