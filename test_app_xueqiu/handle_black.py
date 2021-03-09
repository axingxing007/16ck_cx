from functools import wraps
from appium.webdriver.common.mobileby import MobileBy

from test_app_vx.pages.base_page import BasePage


class BlackList(BasePage):
    def __init__(self):
        self.black_list = [(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/iv_close']")]


def black_wrapper(func):
    @wraps(func)
    def run(*args, **kwargs):
        print('----------', args, kwargs)
        self_1 = args[0]  # 此处表示函数find的第一个参数，为self
        self_1.driver.implictly_wait(1)  # 提高查找速度
        try:
            return func(*args, **kwargs)
        except Exception as e:
            # 遍历黑名单的元素进行处理
            for black in BlackList().black_list:
                elements = self_1.finds(*black)
                if len(elements) > 0:
                    elements[0].click()
                    self_1.driver.implictly_wait(10)
                    return func(*args, **kwargs)  # 处理了黑名单元素重新进行查找
            raise e

    return run
