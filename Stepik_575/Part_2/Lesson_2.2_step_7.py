from selenium import webdriver
import time
import os

link = 'https://suninjuly.github.io/file_input.html'

selector_1 = '[name="firstname"]'
selector_2 = '[name="lastname"]'
selector_3 = '[name="email"]'
selector_id = 'file'
selector_5 = 'button'

input_name = 'name'
'''
    Открыть страницу http://suninjuly.github.io/file_input.html
    Заполнить текстовые поля: имя, фамилия, email
    Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
    Нажать кнопку "Submit"
'''

try:
    browser = webdriver.Chrome()
    browser.get(link)

    #  вводим ткст в формы ввода текста (да, тавтология)
    input1 = browser.find_element_by_css_selector(selector_1)
    input1.send_keys(input_name)
    input2 = browser.find_element_by_css_selector(selector_2)
    input2.send_keys(input_name)
    input3 = browser.find_element_by_css_selector(selector_3)
    input3.send_keys(input_name)

    # получаем путь к директории текущего исполняемого файла
    current_dir = os.path.abspath(os.path.dirname(__file__))

    # добавляем к этому пути имя файла
    file_path = os.path.join(current_dir, 'file.txt')

    # собсна отправляем файлик
    send_file = browser.find_element_by_id(selector_id)
    send_file.send_keys(file_path)

    button = browser.find_element_by_css_selector(selector_5)
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
