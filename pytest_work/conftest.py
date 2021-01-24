from typing import List

import pytest

from pytest_work.calculator import Calculator


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    # item表示每个测试用例，解决用例名称中文显示问题
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')


@pytest.fixture(scope='module')
def my_fixture():
    print('开始计算')
    yield None
    print('结束计算')


@pytest.fixture()
def get_cal():
    cal = Calculator()
    yield cal
