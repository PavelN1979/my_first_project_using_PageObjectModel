from .pages.base_page import BasePage
from .pages.product_page import LoginPage


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

def test_guest_add_product_to_cart(browser):
    page = LoginPage(browser, link)   
    page.open()
    page.add_product_to_cart() # добавляем продукт в корзину
    page.solve_quiz_and_get_code() # вычисляем формулу
    page.added_product_by_name_product() #  проверка названия товара добаляемого в корзину  с названием товара в корзине
    page.cost_of_the_ordered_goods() # проверка стоимость товара в корзине со стоимостью добавленного товара
    
    

