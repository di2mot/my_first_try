from selenium import webdriver
import time
from config_Lesson_1_6_step_6 import *

try:
    browser = webdriver.Chrome()
    browser.get(link)

    elements = browser.find_elements_by_tag_name(value)
    print(len(elements))
    for element in elements:
        element.send_keys(input_name)


    # input1 = browser.find_element_by_name(value1)
    # input1.send_keys(imput_name)
    #
    # input2 = browser.find_element_by_name(value2)
    # input2.send_keys(imput_name)
    #
    # input3 = browser.find_element_by_name(value3)
    # input3.send_keys(imput_name)
    #
    # input3 = browser.find_elements_by(value4)
    # input3.send_keys(imput_name)
    #
    # input4 = browser.find_elements_by(value5)
    # input4.send_keys(imput_name)


    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
