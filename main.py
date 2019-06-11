import variables
import common


#common.SETUP_LOCAL()
common.SETUP_BrowserStack()

common.Valid_Login()
common.Search_Event(variables.myEvent_Name)
common.goto_MyEvents()
common.event_isVisible(variables.myEvent_Name)

common.QUIT()