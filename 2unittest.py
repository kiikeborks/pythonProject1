import unittest
from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver


class MyTestCase(unittest.TestCase):

    def setUp(self):
        desired_caps = {
            "deviceName": "emulator-5554",
            "platformName": "Android",
            "automationName": "UiAutomator2",
            "appPackage": "com.android.chrome",
            "appActivity": "com.google.android.apps.chrome.Main"
        }
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        self.driver.get("https://demo.opencart.com/")
        self.driver.implicitly_wait(20)

    def testDisplayedPage(self):
        if len(self.driver.find_elements(AppiumBy.ID, "com.android.chrome:id/terms_accept")) > 0:
            self.driver.find_element(AppiumBy.ID, "com.android.chrome:id/terms_accept").click()
            self.driver.find_element(AppiumBy.ID, "com.android.chrome:id/negative_button").click()

        self.driver.find_element(AppiumBy.XPATH, "//*[@resource-id='menu']/android.widget.Button")


if __name__ == '__main__':
    unittest.main()