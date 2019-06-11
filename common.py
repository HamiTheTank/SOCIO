import variables
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.common.exceptions import NoSuchElementException
import time



def SETUP_LOCAL():
    variables.driver = webdriver.Remote("http://localhost:4723/wd/hub", variables.desired_caps_local)
    print("[OK] Setup successful")

def SETUP_BrowserStack():
    variables.driver = webdriver.Remote(
    command_executor='http://alihanozbayrak1:yYzukxkJ3sAqxT1pyW7B@hub.browserstack.com:80/wd/hub', desired_capabilities=variables.desired_caps_BrowserStack)
    #variables.driver.set_page_load_timeout(10)
    variables.driver.implicitly_wait(100)
    print("[OK] Setup successful")



def Valid_Login():

    driver = variables.driver

    login_btn = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable((MobileBy.ID, variables.login_btn_ID))
    )
    login_btn.click()

    email_input = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((MobileBy.XPATH, variables.email_input_xpath))
    )
    email_input.send_keys(variables.login_email)
    #driver.hide_keyboard()


    next_btn1 = driver.find_element_by_xpath(variables.next_btn01_xpath)
    next_btn1.click()

    next_btn2 = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((MobileBy.XPATH, variables.next_btn02_xpath))
    )

    #pwd_box = driver.find_elements_by_class_name("android.widget.EditText")
    pwd_box = driver.find_elements_by_id("com.atsocio.socio:id/text_input_edit_text")
    pwd_box[1].send_keys(variables.login_password)
    #driver.hide_keyboard()

    #next_btn2 = driver.find_element_by_xpath(variables.next_btn02_xpath)
    next_btn2.click()

    search_btn = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((MobileBy.ID, variables.SearchEvent_btn_ID))
    )

    assert (search_btn.get_attribute('displayed') == "true"), "Login Failed"

    print("[OK] Login Successful")



def Search_Event(search_term):

    driver = variables.driver

    search_btn = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((MobileBy.ID, variables.SearchEvent_btn_ID))
    )
    search_btn.click()

    search_bar = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((MobileBy.ID, variables.SearchEvent_bar_ID))
    )
    search_bar.click()
    search_bar.send_keys(search_term)

    driver.press_keycode(66)

    #TODO: check search result count > 0

    search_result = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((MobileBy.XPATH, variables.result02_xpath))
    )
    #search_result.click()

    print("[OK] Searching event successful")



def Join_Event():

    driver = variables.driver

    join_btn = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((MobileBy.XPATH, variables.join_btn_xpath))
    )
    join_btn.click()



def goto_MyEvents():

    driver = variables.driver

    driver.back()
    driver.back()

    myEvents_tab = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, variables.MyEvents_tab_ACCESSIBILITY_ID))
    )
    myEvents_tab.click()



    events_list = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((MobileBy.ID, variables.MyEvents_list_ID))
    )

    touch_actions = TouchActions(driver)
    #Next event
    touch_actions.flick_element(events_list, -100, 0, 80).perform()
    #Next event
    touch_actions.flick_element(events_list, -100, 0, 80).perform()



def event_isVisible(eventName):

    driver = variables.driver

    event_item = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((MobileBy.ID, variables.MyEvents_list_ID))
    )

    assert (event_item.get_attribute('displayed') == "true"), "Event not displayed"

    event_title = driver.find_element_by_id("com.atsocio.socio:id/text_event_name").text

    assert (event_title == eventName), "[ERROR] Event not found!"

    print("[OK] Event found")



def QUIT():
    variables.driver.quit()
    print("Done.")
