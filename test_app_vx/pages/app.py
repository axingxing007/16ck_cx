from appium import webdriver

from test_app_vx.pages.base_page import BasePage
from test_app_vx.pages.main_page import MainPage


class App(BasePage):
    def start(self):
        if self.driver is None:
            caps = dict()
            caps["platformName"] = "android"
            caps["deviceName"] = "mumu"
            caps["appPackage"] = "com.tencent.wework"
            caps["appActivity"] = ".launch.LaunchSplashActivity"
            # caps["autoAcceptAlerts"] = True
            # caps["automationName"] = 'UiAutomator2'
            # caps["autoGrantPermissions"] = True
            # caps["ensureWebviewsHavePages"] = True
            # 设置页面等待空闲状态的时间
            caps['settings[waitForIdleTimeout]'] = 0
            caps["noReset"] = True  # 不清空缓存，即保持登录
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        else:
            self.driver.launch_app()
        self.driver.implicitly_wait(10)

    def restart(self):
        """
        重启app
        :return:
        """
        self.driver.close_app()
        self.driver.launch_app()

    def stop(self):
        self.driver.quit()

    def goto_main(self):
        """
        进入企业微信主页面
        :return:
        """
        return MainPage(self.driver)
