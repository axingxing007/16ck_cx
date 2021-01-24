from test_app_vx.pages.app import App


class TestDa:
    __name = "外出打卡成功"

    def setup_class(self):
        self.app = App()
        self.app.start()

    def teardown_class(self):
        self.app.stop()

    def test_outer_daka(self):
        """1、跳转到main页面；2、点击底部区域的工作台；
           3、点击打卡icon,进入到打卡页面
           4、点击外出打卡，点击打卡按钮
           5、断言是否打卡成功
        """
        result = self.app.goto_main().goto_bench(). \
            click_daka_icon().click_outer_daka_button()
        assert result == self.__name
