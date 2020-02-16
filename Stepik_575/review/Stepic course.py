from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    name = browser.find_element_by_css_selector("div.first_block input.form-control.first")
    name.send_keys("John")
    surname = browser.find_element_by_css_selector("div.first_block input.form-control.second")
    surname.send_keys("Doe")
    mail = browser.find_element_by_css_selector("div.first_block input.form-control.third")
    mail.send_keys("banana@banana.com")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:

    time.sleep(5)

    browser.quit()