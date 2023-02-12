import unittest
from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver

class MyTestCase(unittest.TestCase):
    def setUp(self):
        desired_caps = {
            "platformName": "Android",
            "deviceName": "emulator-5554",
            "appPackage": "com.saucelabs.mydemoapp.rn",
            "appActivity": ".MainActivity"
        }
        # Start the Appium client
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)


    def tearDown(self):
        self.driver.quit()

    def test1(self):
        # Find an element and interact with it
        el = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "open menu")
        # Check if element is displayed
        self.assertTrue(el.is_displayed())
        el.click()


# https://codecouple.pl/2016/02/27/python-specjalna-zmienna-__name__/
if __name__ == '__main__':
    unittest.main()
