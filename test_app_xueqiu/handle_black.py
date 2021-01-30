from functools import wraps
from appium.webdriver.common.mobileby import MobileBy


class BlackList:
    def __init__(self):
        self.black_list = [(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/iv_close']")]


def black_wrapper(func):
    @wraps(func)
    def run(*args, **kwargs):
        self_1 = args[0]  # 此处表示函数find的第一个参数，为self
        try:
            return func(*args, **kwargs)
        except Exception as e:
            # 遍历黑名单的元素进行处理
            for black in BlackList().black_list:
                elements = self_1.finds(*black)
                if len(elements) > 0:
                    elements[0].click()
                    return func(*args, **kwargs)  # 处理了黑名单元素重新进行查找
            raise e

    return run
