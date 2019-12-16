from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = Chrome()
driver.get("http://www.theTestingWorld.com")
#driver.find_element_by_name("fld_username").send_keys("Hello")

act = ActionChains(driver)
# act.click().perform()

# act.click(driver.find_element_by_xpath("//label[@for='tab2']")).perform()

# Context Click (Right Click)
# act.context_click().perform()

# Double Click
# act.double_click().perform()
# act.double_click(driver.find_element_by_xpath("//label[@for='tab2']")).perform()

# click on the menue and click in the opened page
act.move_to_element(driver.find_element_by_xpath("//span[contains(text(),'TUTORIAL')]")).perform()