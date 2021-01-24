import pytest
import yaml
import allure


def get_data(file: str, key=None) -> list:
    try:
        with open(file, encoding='utf-8') as f_obj:
            value = yaml.safe_load(f_obj)
            para_data = value.get(key, '键不存在')
            if para_data in ['键不存在']:
                raise Exception
            else:
                return para_data
    except Exception as e:
        print('请检查文件路径')


@allure.feature('测试计算的类')
@pytest.mark.usefixtures('my_fixture')
class TestCalculator:
    @allure.story('测试加法的用例')
    @allure.title('测试{a} + {b} = {expected}')
    @pytest.mark.run(order=0)
    @pytest.mark.parametrize('a, b, expected', get_data('data.yml', 'add_data'))
    def test_add(self, a, b, expected, get_cal):
        """测试两个数相加"""
        with allure.step('第一步，获取计算类的对象'):
            cal = get_cal
        with allure.step('第二步，断言两个数相加是否等于第三个数'):
            assert cal.add(a, b) == expected

    @allure.story('测试减法的用例')
    @allure.title('测试{a} - {b} = {expected}')
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize(('a', 'b', 'expected'), get_data('data.yml', 'sub_data'))
    def test_sub(self, a, b, expected, get_cal):
        """测试两个数相减"""
        with allure.step('第一步，获取计算类的对象'):
            cal = get_cal
        with allure.step('第二步，断言两个数相减是否等于第三个数'):
            assert cal.sub(a, b) == expected

    @allure.story('测试除法的用例')
    @allure.title('测试{a} / {b} = {expected}')
    @pytest.mark.run(order=3)
    @pytest.mark.parametrize('a, b, expected', get_data('data.yml', 'div_data'))
    def test_div(self, a, b, expected, get_cal):
        """测试两个数相除"""
        with allure.step('第一步，获取计算类的对象'):
            cal = get_cal
        with allure.step('第二步，断言两个数相除是否等于第三个数'):
            assert cal.div(a, b) == expected

    @allure.story('测试乘法的用例')
    @allure.title('测试{a} * {b} = {expected}')
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("a, b, expected", get_data('data.yml', 'mul_data'))
    def test_mul(self, a, b, expected, get_cal):
        """测试两个数相乘"""
        with allure.step('第一步，获取计算类的对象'):
            cal = get_cal
        with allure.step('第二步，断言两个数相乘是否等于第三个数'):
            assert cal.mul(a, b) == expected
