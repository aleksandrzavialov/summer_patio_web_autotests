from summerpatio_web_autotests.model.components.order import Order
from summerpatio_web_autotests.model.pages.cart import Cart
from summerpatio_web_autotests.model.pages.main_page import MainPage
from summerpatio_web_autotests.model.pages.delivery_tab import DeliveryTab
from summerpatio_web_autotests.model.pages.info_tab import InfoTab
from summerpatio_web_autotests.model.pages.menu_page import MenuPage

main_page = MainPage()
delivery_tab = DeliveryTab()
info_tab = InfoTab()
menu_page = MenuPage()
cart = Cart()
new_order = Order()

meat_dish_1 = ('мясо #1', 'Мясо', '250 г', '340 ₽')
soup_dish_2 = ('cуп #2', 'Супы', '270 г', '300 ₽')
fish_dish_3 = ('рыба #3', 'Рыба', '250 г', '320 ₽')
