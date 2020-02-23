from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

#link = 'http://suninjuly.github.io/selects1.html'
link = 'http://suninjuly.github.io/selects2.html'
selector_1 = 'num1'
selector_2 = 'num2'
selector_5 = 'button'

'''

    Открыть страницу http://suninjuly.github.io/selects1.html
    Посчитать сумму заданных чисел
    Выбрать в выпадающем списке значение равное расчитанной сумме
    Нажать кнопку "Submit"

'''


try:
    #стандартная инициализация
    browser = webdriver.Chrome()
    browser.get(link)

    # получаю цифры и складываю их
    num_1 = browser.find_element_by_id(selector_1)
    num_2 = browser.find_element_by_id(selector_2)
    answer = str(int(num_1.text) + int(num_2.text))

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(answer)  # ищем элемент с текстом unswer


    # клик по кнопке
    button = browser.find_element_by_css_selector(selector_5)
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
