import variables
import common

#BrowserStack
userName = "alihanozbayrak1"
accessKey = "yYzukxkJ3sAqxT1pyW7B"
myEvent = "ETT Conference 2019"



#common.SETUP_LOCAL()
common.SETUP_BrowserStack()

common.Valid_Login()
common.Search_Event(myEvent)
common.goto_MyEvents()
common.event_isVisible(myEvent)

common.QUIT()