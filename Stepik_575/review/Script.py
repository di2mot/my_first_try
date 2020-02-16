from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration1.html"

browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element_by_css_selector("[placeholder='Input your first name']")
input1.send_keys("Ivan")
input2 = browser.find_element_by_css_selector("[placeholder='Input your last name']")
input2.send_keys("Petrov")
input3 = browser.find_element_by_css_selector("[placeholder='Input your email']")
input3.send_keys("Smolensk")
input4 = browser.find_element_by_css_selector("[placeholder='Input your phone:']")
input4.send_keys("Russia")
input5 = browser.find_element_by_css_selector("[placeholder='Input your address:']")
input5.send_keys("alex@mail.ru")
button = browser.find_element_by_css_selector("button.btn")
button.click()

# успеваем скопировать код за 30 секунд
time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()