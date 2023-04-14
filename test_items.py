from selenium import webdriver
from selenium.webdriver.common.by import By
import time
def test_add_to_cart_button_exist(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    # Жду и принимаю сообщение об использывании языка
    time.sleep(30)

    add_to_cart_button = len(browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket"))
    assert add_to_cart_button > 0, "Añadir al carrito"