from selenium import webdriver
import unittest

import time


link = 'https://suninjuly.github.io/registration2.html'

# Селекторы
value1 = 'div.first_block > div.form-group.first_class > input.form-control.first'
value2 = 'div.first_block > div.form-group.second_class > input.form-control.second'
value3 = 'div.first_block > div.form-group.third_class > input.form-control.third'
value_button = 'button.btn.btn-default'

# Вводмый текст
input_name = 'name'

# Текст с которым сравниваем
test_text = 'Congratulations! You have successfully registered!'

class TestSite(unittest.TestCase):
    def test_site(self):
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element_by_css_selector(value1)
        input1.send_keys(input_name)
        input2 = browser.find_element_by_css_selector(value2)
        input2.send_keys(input_name)
        input3 = browser.find_element_by_css_selector(value3)
        input3.send_keys(input_name)

        button = browser.find_element_by_css_selector(value_button)
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(test_text, welcome_text, 'Fatal ERRORE')
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(1)
        # закрываем браузер после всех манипуляций
        browser.quit()

if __name__ == "__main__":
    unittest.main()