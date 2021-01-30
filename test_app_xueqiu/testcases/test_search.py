from test_app_xueqiu.pages.app import App


class TestSearch:
    def setup_class(self):
        self.app = App()
        self.app.start()

    def test_search(self):
        self.app.goto_main().goto_market().goto_search().search()

    def teardown(self):
        self.app.stop()
