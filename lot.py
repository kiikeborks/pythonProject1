import unittest
from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver
class LotAppTestCase(unittest.TestCase):

    invalid_email = "123456789123456789@123456789.123"
    valid_password = "T3st3rzY"

    def setUp(self):
        desired_caps = {
            "platformName": "Android",
            "deviceName": "emulator-5554",
            "appPackage": "pl.lot.mobile",
            "appActivity": "pl.lot.mobile.MainActivity",
            "automationName": "UiAutomator2"
        }

        # Start the Appium client
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        #self.driver.implicity_wait(20)

    def tearDown(self):
        self.driver.quit()

        # TC: ID001
        # 1. Kliknij X, aby zamknąć powitanie
        # 2. Kliknij "Don't allow", aby nie zazwolić na dostęp do lokalizacji
        # 3. Kliknij "Next"
        # 4. Zaakceptuj politykę prywatności
        # 5. Kliknij "Create an account"
        # 6. Wprowadź niepoprawny e-mail
        # 7. Wprowadź hasło
        # 8. Zaakceptuj wszystkie warunki
        # 9. Kliknij "Create your account"
        # Oczekiwany rezultat:
        # Rejestracja nie powodzi się
        # Użytkownik dostaje informację, że coś poszło nie tak i należy spróbować ponownie

    def testID001_registerNewUserWithWrongEmailTest(self):
        # 1. Close the welcoming
        close_btn = self.driver.find_element(AppiumBy.XPATH, "//*[@content-desc='Close']")
        close_btn.click()
        # 2. Don't allot to access to localisation
        dont_allow_btn = self.driver.find_element(AppiumBy.ID, "com.android.permissioncontroller:id/permission_deny_button")
        dont_allow_btn.click()
        self.driver.implicitly_wait(7)
        # 3. Click "Next"
        next_btn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='Next']")
        next_btn.click()
        # 4. Accept privacy policy
        agree_btn = self.driver.find_element(AppiumBy.ID, "pl.lot.mobile:id/btn_accept_cookies")
        agree_btn.click()
        # 5. Create an account
        create_btn = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Create an account")
        create_btn.click()
        # 6. Provide invalid e-mail address
        email_field = self.driver.find_element(AppiumBy.XPATH, "//*[@text='E-mail']")
        email_field.click()
        email_field.send_keys(self.invalid_email)
        # 7. Provide valid password
        password_field = self.driver.find_element(AppiumBy.XPATH, "//*[@text='Password']")
        password_field.click()
        password_field.send_keys(self.valid_password)
        # 8. Accept conditions
        conditions_btn = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Select all']/android.widget.CheckBox")
        conditions_btn.click()
        # 9. Create your account
        createyouraccount_btn = self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc='Create your account']")
        createyouraccount_btn.click()
        self.driver.implicitly_wait(5)
        # Assert Final Result
        element = self.driver.find_element(AppiumBy.XPATH, "//android.view.View[@content-desc='Oops, something went wrong. Please, try again.']")
        self.assertTrue(element.is_displayed(), "Oops, something went wrong. Please, try again.")

if __name__=='__main__':
    unittest.main()