import time


def test_add_to_basket_button_is_present(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)


    time.sleep(30)

    add_button = browser.find_element_by_css_selector(
        "button.btn-add-to-basket"
    )
    assert add_button, "Кнопка добавления в корзину не найдена"