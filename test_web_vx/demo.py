import pytest


class TestDemo:
    # def setup_class(self):
    #     print('类前置')
    #
    # def teardown_class(self):
    #     print('类后置')
    #
    # def setup(self):
    #     print('方法前置')
    #
    # def teardown(self):
    #     print('方法后置')
    @pytest.mark.run(order=3)
    def test01(self):
        print('test01')

    @pytest.mark.run(order=2)
    @pytest.mark.skip()
    def test02(self):
        print('test02')

    @pytest.mark.run(order=1)
    def test03(self):
        print('test03')
