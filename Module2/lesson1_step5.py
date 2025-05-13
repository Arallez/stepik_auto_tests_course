# MODUL 2. LESSON 1. TASK 5

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def compute_value(x):
    """Вычисляет значение натурального логарифма модуля 12 синуса x"""
    return str(math.log(abs(12 * math.sin(int(x)))))


# Используем контекстный менеджер для автоматического закрытия браузера
with webdriver.Chrome() as browser:
    # Открываем целевую страницу
    browser.get("https://suninjuly.github.io/math.html")

    # Шаг 2: Получаем значение X со страницы
    x_value = browser.find_element(By.CSS_SELECTOR, "#input_value").text

    # Шаг 3-4: Вычисляем результат и вводим в текстовое поле
    browser.find_element(By.ID, "answer").send_keys(compute_value(x_value))

    # Шаг 5: Отмечаем чекбокс (используем класс элемента)
    browser.find_element(By.CLASS_NAME, "form-check-input").click()

    # Шаг 6: Выбираем радиобатон через XPath по тексту метки
    browser.find_element(By.XPATH, "//label[contains(.,'Robots rule')]/preceding-sibling::input").click()

    # Шаг 7: Нажимаем кнопку отправки формы
    browser.find_element(By.TAG_NAME, "button").click()

    # Даем время для визуальной проверки результата
    time.sleep(10)