from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"
selector_1 = 'input_value'
selector_2 = 'answer'

'''

    Открыть страницу http://suninjuly.github.io/alert_accept.html
    Нажать на кнопку
    Принять confirm
    На новой странице решить капчу для роботов, чтобы получить число с ответом
'''
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    #стандартная инициализация
    browser = webdriver.Chrome()
    browser.get(link)

    #Тыкам на кнопку
    button = browser.find_element_by_css_selector('button')
    button.click()

    # Подтверждаем алерт
    confirm = browser.switch_to.alert
    confirm.accept()

    # ТАщим "х" и тыкаем его в уравнение
    calc_x = browser.find_element_by_id(selector_1)
    answer = calc(calc_x.text)

    # вставляю текст в форму
    input_answer = browser.find_element_by_id(selector_2)
    input_answer.send_keys(answer)

    #Тыкам на кнопку
    button = browser.find_element_by_css_selector('button')
    button.click()

    # Подтверждаем алерт
    confirm = browser.switch_to.alert
    print(confirm.text.split(': ')[-1])
    confirm.accept()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()