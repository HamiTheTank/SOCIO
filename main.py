from variables import *
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

userName = "alihanozbayrak1"
accessKey = "yYzukxkJ3sAqxT1pyW7B"

#BROWSERSTACK
desired_caps = {
    "build": "Python Android",
    "device": "Samsung Galaxy S8 Plus",
    "app": "bs://4104b2db89253878ab5d1b11efb6cb8b67727608"
}

driver = webdriver.Remote("http://" + userName + ":" + accessKey + "@hub-cloud.browserstack.com/wd/hub", desired_caps)

search_element = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Search Wikipedia"))
)
search_element.click()

search_input = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((MobileBy.ID, "org.wikipedia.alpha:id/search_src_text"))
)
search_input.send_keys("BrowserStack")
time.sleep(5)

search_results = driver.find_elements_by_class_name("android.widget.TextView")
assert (len(search_results) > 0)

driver.quit()