import logging
from functools import wraps
from selenium.webdriver.common.by import By


class BlackHandleException:
    """
    专门处理查找元素异常的类
    思路：增加异常处理流程，当异常出现时完成异常处理并再次重复原有步骤
    具体实现方式：使用递归处理技术 + 异常捕获技术 + python装饰器
    """
    logging.basicConfig(level=logging.DEBUG)
    # 此列表专门用于添加黑名单元素，元素的类型为元组
    black_list = [(By.CSS_SELECTOR, 'a.close-btn')]
    error_count = 0  # 类变量，初始化为0


def handle_exception(func):
    logging.basicConfig(level=logging.INFO)

    @wraps(func)
    def magic(*args, **kwargs):
        logging.basicConfig(level=logging.DEBUG)
        from test_web.pages.base_page import BasePage
        # 获取BasePage类的对象
        _self: BasePage = args[0]
        try:
            result = func(*args, **kwargs)
            # 清空错误次数
            BlackHandleException.error_count = 0
            return result
        except Exception as e:
            BlackHandleException.error_count += 1
            # 如果错误次数大于黑名单中元素的个数，则退出异常处理机制
            if BlackHandleException.error_count > len(BlackHandleException.black_list):
                logging.info(f'异常的次数为：{BlackHandleException.error_count}')
                raise e
            # 对黑名单列表进行遍历
            for element in BlackHandleException.black_list:
                _self.driver.implicitly_wait(2)
                logging.info(element)
                elements = _self.finds(element)
                if len(elements) > 0:
                    elements[0].click()
                    _self.driver.implicitly_wait(10)
                    return magic(*args, **kwargs)
            logging.warning('black list no one found')
            raise e

    return magic
