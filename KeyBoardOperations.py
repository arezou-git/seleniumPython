from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = Chrome()
driver.get("http://www.theTestingWorld.com/testings")
driver.find_element_by_name("fld_username").send_keys("Hello")

act = ActionChains(driver)
#act.send_keys(Keys.TAB).perform()
act.send_keys(Keys.CONTROL).send_keys("a").perform()

