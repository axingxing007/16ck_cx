import pytest
import unittest


@pytest.fixture()
def data(request):
    return request.param


@pytest.mark.parametrize('data', ('cx', 'hq'), indirect=True)
def test07(data):
    print(data)


@pytest.fixture(scope='session')
def test():
    print('先登录')
    yield
    print('退出登录')


@pytest.fixture(scope='session')
def say():
    print('open browser')


@pytest.mark.skip(reason='不想执行')
def test03(test):
    print('----> test03')


@pytest.mark.run(order=1)
@pytest.mark.skipif(condition=False, reason='跳过')
def test04():
    print('----> test04')


@pytest.mark.flaky(reruns=2, reruns_delay=2)
@pytest.mark.last
# @pytest.mark.xfail
def test05():
    assert 3 > 2


@pytest.mark.parametrize('var3, var4', [[3, 4], [5, 6]])
@pytest.mark.parametrize("var1, var2", [[1, 2], [7, 8]])
def test06(var1, var2, var3, var4):
    print(var1, var2, var3, var4)


@pytest.mark.parametrize('var1, var2', [[1, 2], [3, 4], [5, 5]])
def test07(var1, var2):
    assert var1 == var2, '断言两个值是否相等'


def test08():
    pytest.assume(1 == 3)
    pytest.assume(1 == 2)
    pytest.assume(3 == 3)


@pytest.mark.parametrize('var1, var2, expected', [[
    1, 2, 3], [4, 5, 9], pytest.param(8, 9, 18, marks=pytest.mark.xfail),
    pytest.param(9, 6, 15, marks=pytest.mark.skipif)
])
def test09(var1, var2, expected):
    assert var1 + var2 == expected


@pytest.mark.usefixtures('test')
class TestDemo:
    def test01(self):
        print('test01')

    def test02(self):
        print('test02')


class Test(unittest.TestCase):
    pass


# 增加可读性
data_1 = [
    (1, 2, 3),
    (4, 5, 9)
]
data_2 = [
    (3, 3, 3),
    (4, 4, 4)
]
# ids(多少组数据，就要有多少个id，然后组成一个id的列表)
ids = ["a:{0} + b:{1} = expect:{2}".format(a, b, expect) for a, b, expect in data_2]  # 推导式生成列表


@pytest.mark.parametrize('a, b, expect', data_1, ids=ids)
class TestParametrize:
    def test_parametrize_1(self, a, b, expect):
        print('测试函数1测试数据为{}-{}'.format(a, b))
        assert a + b == expect

    def test_parametrize_2(self, a, b, expect):
        print('测试函数2数据为{}-{}'.format(a, b))
        assert a + b == expect


@pytest.fixture(scope='module')
def input_user(request):
    user = request.param
    print(f'登录的账号是：{user}')
    return user


@pytest.fixture(scope='module')
def input_pwd(request):
    pwd = request.param
    print(f'登录的密码是：{pwd}')
    return pwd


data_3 = ['cx', 'hq']
data_4 = ['123', '456']


@pytest.mark.parametrize('input_user', data_3, indirect=True)
@pytest.mark.parametrize('input_pwd', data_4, indirect=True)
def test11(input_user, input_pwd):
    print(f'fixture返回的内容为：{input_user, input_pwd}')
