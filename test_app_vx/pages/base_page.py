import time

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, by, locator):
        """
        通过MobileBy类来查找单个元素，这个类继承By
        :return: 返回值的类型为WebElement
        """
        ele = self.driver.find_element(by, locator)
        return ele

    def finds(self, by, locator):
        """
        通过MobileBy类来查找多个元素
        :return: 返回值类型为list
        """
        ele_list = self.driver.find_elements(by, locator)
        return ele_list

    def find_and_click(self, by, locator):
        ele = self.find(by, locator)
        ele.click()

    def get_ele_text(self, by, locator):
        ele = self.find(by, locator)
        return ele.text

    def scroll_find(self, text):
        """
        滑动查找元素，适合app
        :param text: 参数text传入元素的文本值
        :return: 返回值的类型为WebElement
        """
        ele = self.driver.find_element(
            MobileBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().'
            'scrollable(true).instance(0)).''scrollIntoView(new UiSelector().'
            f'text("{text}").instance(0));')
        return ele

    def scroll_find_and_click(self, text):
        """
        1、先获取滑到查找到的元素；2、对查找到的元素进行点击操作
        :param text:
        :return:
        """
        ele = self.scroll_find(text)
        ele.click()

    def find_and_send(self, by, locator, content):
        """
        1、先获取查找到的元素；2、对获取元素的输入框进行清空操作；3、输入内容
        :param content: 输入的内容
        :return: 获取输入的值
        """
        ele = self.find(by, locator)
        ele.clear()
        ele.send_keys(content)

    def wait_for(self, by, locator):
        """显式等待，找到元素捕获异常信息"""

        def method(driver):
            if len(self.finds(by, locator)) > 0:
                return True
            else:
                return False

        try:
            WebDriverWait(self.driver, 10).until(method=method)
        except Exception as e:
            print(e)

    def get_toast_text(self):
        """元素的value是固定写法"""
        result = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        return result

    def swipe_find(self, by, locator, timeout=300):
        """上滑查找元素，滑动距离为1/2，参数timeout表示滑超时的时间，默认5分钟"""
        # 获取屏幕的size，返回值类型为dict
        size = self.driver.get_window_size()
        x1 = size['width'] * 0.5
        y1 = size['height'] * 0.75
        y2 = size['height'] * 0.25
        self.driver.implicitly_wait(1)
        # 找到所有元素
        eles = self.finds(by, locator)
        # 不停滑动，直到找到为止， 通过参数timeout控制查找的时间
        end_time = time.time() + timeout
        while len(eles) == 0:
            # 滑动
            self.driver.swipe(x1, y1, x1, y2, duration=500)
            eles = self.finds(by, locator)
            if time.time() > end_time:
                raise TimeoutException
            if len(eles) > 0:
                break
        self.driver.implicitly_wait(10)
        return eles[0]

    def swipe_find_and_click(self, by, locator):
        """
        滑动查找并进行点击操作
        :return:
        """
        self.swipe_find(by, locator).click()
