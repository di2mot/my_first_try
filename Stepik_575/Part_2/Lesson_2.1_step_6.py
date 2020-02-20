from selenium import webdriver
import time

link = 'https://suninjuly.github.io/math.html'

try:
    #стандартная инициализация
    browser = webdriver.Chrome()
    browser.get(link)

    people_radio = browser.find_element_by_id("robotCheckbox")

    people_checked = people_radio.get_attribute("type")
    print("value of people radio: ", people_checked)
    # assert people_checked is not None, "People radio is not selected by default"

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()
