from selenium.webdriver.common.by import By
import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_guest_should_see_button_basket(browser):
    browser.get(link)
    time.sleep(30)  # ставлю 30, как указано в условии задания, но можно и меньше

    elements = browser.find_elements(By.CSS_SELECTOR, '.btn-add-to-basket')

    # проверяем, что данный элемент есть на странице
    assert len(elements) > 0, 'button not found'
