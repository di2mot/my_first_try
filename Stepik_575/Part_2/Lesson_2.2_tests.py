from selenium import webdriver

text = 'Hello'
browser = webdriver.Chrome()
# link = "https://SunInJuly.github.io/execute_script.html"
# browser.get(link)
#
# button = browser.find_element_by_tag_name("button")
# browser.execute_script("return arguments[0].scrollIntoView(true);", button)
# button.click()
# assert True
#
# # browser = webdriver.Chrome()
browser.execute_script("alert('Robots at work');")

confirm = browser.switch_to.alert
print(confirm.text.split(': ')[-1])
confirm.accept()