import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class TestData:
    def __init__(self, file):
        self.file = file
        with open(self.file, 'r', encoding='utf-8') as f:
            self.steps = yaml.safe_load(f)

    def run(self, driver: WebDriver):
        ele = None
        for step in self.steps:
            print(step)
            if isinstance(step, dict):
                if 'id' in step.keys():
                    ele = driver.find_element(MobileBy.ID, step['id'])
                    print(ele.__class__.__name__)
                elif 'xpath' in step.keys():
                    ele = driver.find_element(MobileBy.XPATH, step['xpath'])
                if 'input' in step.keys():
                    ele.send_keys(step['input'])
                else:
                    ele.click()
                if 'get' in step.keys():
                    ele.get_attribute(step['get'])
