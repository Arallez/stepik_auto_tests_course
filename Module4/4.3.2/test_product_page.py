import pytest
from pages.product_page import ProductPage


@pytest.mark.parametrize('promo', ["newYear"])
def test_guest_can_add_product_to_basket(browser, promo):
    # Arrange
    link = f"http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo={promo}"
    page = ProductPage(browser, link)
    page.open()

    # Act
    page.add_to_basket()

    # Assert
    page.should_be_product_name_in_message()
    page.should_be_basket_total_match_price()