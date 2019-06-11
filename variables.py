#============= GLOBAL ==========================================
driver = None
desired_caps_local = {
    "platformName": "Android",
    "deviceName": "emulator-5556",
    "app": "D:\\SOCIO\\socio_app.apk"
}

desired_caps_BrowserStack = {
    "browserName": "android",
    "device": "Samsung Galaxy S8",
    "realMobile": "true",
    "os_version": "7.0",
    "name": "SOCIO_Assignment_VT",
    "app": "bs://070640ee2df6069341b86be35645ff326d5c7538",
    "unicodeKeyboard": "True",
    "resetKeyboard": "True",
    "newCommandTimeout": "90"
}

#============= LOGIN ===========================================
login_email = "squeezoure@gmail.com"
login_password = "hireme"
login_btn_ID = "com.atsocio.socio:id/button_sign_in"
email_input_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.EditText"
next_btn01_resourceID = "com.atsocio.socio:id/button_next"
next_btn01_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.Button"
next_btn02_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout[2]/android.widget.Button"
pwd_box_xpath = "//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.EditText"

#============= DASHBOARD =======================================
SearchEvent_btn_ID = "com.atsocio.socio:id/button_search_event"
SearchEvent_bar_ID = "com.atsocio.socio:id/search_src_text"
MyEvents_tab_ACCESSIBILITY_ID = "MY EVENTS"
MyEvents_list_ID = "com.atsocio.socio:id/recycler_event_list"

result02_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.widget.ImageView"
join_btn_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ImageView"
