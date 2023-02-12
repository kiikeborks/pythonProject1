import unittest

from appium.webdriver import webdriver
from appium.webdriver.common.appiumby import AppiumBy

from appium1.py import driver


class MyTestCase(unittest.TestCase):

    valid_name = "NAME"
    valid_surname = "Saurname"
    telephone = "123456789"
    invalid_email = "123456789123456789@123456789.123"
    valid_passwoed = "T3st3rzY"

    def setUp(self):
        desired_caps = {
            "platformName": "Android",
            "deviceName": "emulator-5554",
            "appPackage": "com.wizzair.WizzAirApp",
            "appActivity": "com.wizzair.app.MainActivityV2",
            "automationName": "UiAutomator2"
        }

        # Start the Appium client
        self.driver = webdriver.Remote("https://localhost:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(20)

    def tearDown(self):
        self.driver.quit()

        # TC: ID001
        # 1. Kliknij "ZALOGUJ SIĘ"
        # 2. Kliknij "REJESTRACJA"
        # 3. Wpisz imię
        # 4. Wpisz nazwisko
        # 5. Wybierz płeć
        # 6. Wprowadź nr telefonu
        # 7. Wprowadź niepoprawny e-mail
        # 8. Wprowadź hasło
        # 9. Wprowadź kraj
        # 10. Zaakceptuj politykę prywatności i kliknij rejestruj
        # Oczekiwany rezultat:
        # Rejestracja nie powodzi się
        # Użytkownik dostaje informację, że wprowadzony e-mail jest niepoprawny


    def testID001_registerNewUserWithWrongEmailTest(self):
        # 01. Jeśli się pojawi -> nie pozwalaj na dostęp do lokalizacji
        if len(self.driver.find.element(AppiumBy.ID, "com.android.permissioncontroller:id/permission_deny_and_dont_ask_again_button")) > 0:
            self.driver.find_element(AppiumBy.ID, "com.android.permissioncontroller:id/permission_deny_and_dont_ask_again_button").click()
            self.driver.find_element(AppiumBy.ID, "com.wizzair.WizzAirApp:id/privacy_policy_allow").click()
            self.driver.implicitly_wait(20)


        # 1. Kliknij "ZALOGUJ SIĘ"
        zaloguj_btn = self.driver.find_element(AppiumBy.ACCESSABILITY_ID, "login button")
        zaloguj_btn.click()
        # 2. Kliknij "REJESTRACJA"
        rejestracja_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "registry button")
        rejestracja_btn.click()
        # 3. Wpisz imię
        imie_field = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "name input")
        imie_field.send_keys(self.valid_name)
        # 4. Wpisz nazwisko
        nazwisko_field = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "surname input")
        nazwisko_field.send_keys(self.valid_surname)
        # 5. Wybierz płeć
        gender_toggle_switch = self.driver.find_element(AppiumBy.ID, "gender")
        gender_toggle_switch.click()
        # 6. Wprowadź nr telefonu
        telephone_field = self.driver.find_element(AppiumBy.ID, "")


if __name__ == '__main__':
    unittest.main()
