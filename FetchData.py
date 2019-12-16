from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select

driver = Chrome()
driver.get("http://www.theTestingWorld.com/testings")

# Maximize browser
driver.maximize_window()

print("Title of page is " + driver.title)

# Fetch URL of Page
print(driver.current_url)

# Fetch complete page HTMl
#print(driver.page_source)

# Fetching element text
print(driver.find_element_by_class_name("displayPopup").text)

#fetching attribute value of element
print(driver.find_element_by_xpath("//input[@type='submit']").get_attribute("value"))

# Fetch data from drop and down
obj = Select(driver.find_element_by_name("sex"))
obj.select_by_visible_text("Male")

# Fetch Selected option
print(obj.first_selected_option.text)

for op in obj.options:
    print(op.text)



