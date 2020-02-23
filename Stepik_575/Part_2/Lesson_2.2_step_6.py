from selenium import webdriver
import time
import math

link = "https://SunInJuly.github.io/execute_script.html"

selector_1 = 'input_value'
selector_2 = 'answer'
selector_3 = '[for="robotCheckbox"]'
selector_4 = '[for="robotsRule"]'
selector_5 = 'button'

'''
    Открыть страницу http://SunInJuly.github.io/execute_script.html.
    Считать значение для переменной x.
    Посчитать математическую функцию от x.
    Проскроллить страницу вниз.
    Ввести ответ в текстовое поле.
    Выбрать checkbox "I'm the robot".
    Переключить radiobutton "Robots rule!".
    Нажать на кнопку "Submit".
    
    ln(abs(12*sin(x))), where x = 99?
'''

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    #стандартная инициализация
    browser = webdriver.Chrome()
    browser.get(link)
    browser.execute_script("window.scrollBy(0, 200);")

    # получаю текст который используется в формуле
    calc_x = browser.find_element_by_id(selector_1)
    answer = calc(calc_x.text)

    # вставляю текст в форму
    input_answer = browser.find_element_by_id(selector_2)
    input_answer.send_keys(answer)

    # выбираю параметр
    check_robot = browser.find_element_by_css_selector(selector_3)
    check_robot.click()

    # выбираю параметр
    check_robot_1 = browser.find_element_by_css_selector(selector_4)
    check_robot_1.click()

    # клик по кнопке
    button = browser.find_element_by_css_selector(selector_5)
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()