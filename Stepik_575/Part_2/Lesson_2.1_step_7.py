from selenium import webdriver
import time
import math

link = 'https://suninjuly.github.io/get_attribute.html'
selector_1 = 'treasure'
selector_2 = 'answer'
selector_3 = 'robotCheckbox'
selector_4 = 'robotsRule'
selector_5 = 'button'

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    #стандартная инициализация
    browser = webdriver.Chrome()
    browser.get(link)

    # получаю текст который используется в формуле
    calc_x = browser.find_element_by_id(selector_1)
    answer = calc(calc_x.get_attribute('valuex'))

    # вставляю текст в форму
    input_answer = browser.find_element_by_id(selector_2)
    input_answer.send_keys(answer)

    # выбираю параметр
    check_robot = browser.find_element_by_id(selector_3)
    check_robot.click()

    # выбираю параметр
    check_robot_1 = browser.find_element_by_id(selector_4)
    check_robot_1.click()

    # клик по кнопке
    button = browser.find_element_by_css_selector(selector_5)
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
