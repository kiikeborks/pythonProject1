from appium import webdriver

# Set up desired capabilities
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "appPackage": "pl.lot.mobile",
    "appActivity": "pl.lot.mobile.MainActivity"
}

# Start the Appium client
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

# Find an element and interact with it
el = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Close")
# Check if element is displayed
#el.is_displayed()
el.click()

# Close the Appium client
#driver.quit()
