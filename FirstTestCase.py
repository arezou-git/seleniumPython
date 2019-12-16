from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium.webdriver.support.select import Select


# Creating object from chrom class
# after creating object, the constructor in the class
# should open the browser
# but for selenium we need and exe file which is an interface
# between the testcase and browser, but I didnt use that here
# it seems in new version there is no need for that

#driver = Chrome()

# for firefox we need to open firefox driver which is call
#gekodriver

path = "C:\\geckodriver.exe"
driver = Firefox(executable_path=path)

driver.get("http://www.thetestingworld.com/testings")

# Maximize browser
driver.maximize_window()

# Enter data to the textbox
driver.find_element_by_name("fld_username").send_keys("helloworld")
driver.find_element_by_name("fld_email").send_keys("arezou.madani@gmail.com")
driver.find_element_by_name("fld_password").send_keys("helloworld")
driver.find_element_by_xpath("//input[@name='fld_cpassword']").send_keys("ABCD")

# if we write new value for one of the above element, new value
# will append to the perviuse value. for example after executing
#below line, value of the username will be helloworldABCD
driver.find_element_by_name("fld_username").send_keys("ABCD")

# cleare existing text of the text box
#driver.find_element_by_name("fld_username").clear()

# working on radio button
driver.find_element_by_xpath("//input[@value='home']").click()

# Work on drop down
obj = Select(driver.find_element_by_name("sex"))
# obj.select_by_index(1)
# obj.select_by_value("2")
obj.select_by_visible_text("Male")


# working on check box
driver.find_element_by_xpath("//input[@type='checkbox']").click()

# working on button
#driver.find_element_by_xpath("//input[@type='submit']").click()

# work on link
#driver.find_elements_by_link_text("Read Detail").click()

#driver.close()