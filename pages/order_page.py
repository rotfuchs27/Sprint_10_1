import allure
from locators.order_page_locators import OrderPageLocators
from data import TARIFFS
from pages.base_page import BasePage

class OrderPage(BasePage):

    @allure.step('Проверка открытия страницы заказа')
    def order_page_loaded(self):
        conditions = [
            self.find_visible_element(OrderPageLocators.ORDER_BLOCK)
        ]
        return all(conditions)

    @allure.step('Проверка названий тарифов')
    def tariff_titles_match(self):
        elements = self.find_visible_elements(OrderPageLocators.TARIFF_TITLES)
        return all([element.text in TARIFFS.keys() for element in elements])

    @allure.step('Проверка числа активных тарифов')
    def count_of_active_tariffs(self):
        return len(self.find_visible_elements(OrderPageLocators.TARIFF_ACTIVE))

    @allure.step('Получение информации по тарифу')
    def get_tariff_information_by_name(self, tariff_name):
        elements = self.find_visible_elements(OrderPageLocators.TARIFF_TITLES)
        for element in elements:
            if element.text == tariff_name:
                element.click()
                break

        self.move_to_element(OrderPageLocators.TARIFF_INFO_BUTTON)
        return self.get_text(OrderPageLocators.ACTIVE_TARIFF_DESCRIPTION)


    @allure.step('Проверка отображения блока с полями Телефон, Способ оплаты, Комментарий водителю, Требования к заказу')
    def order_block(self):
        conditions = [
            self.find_visible_element(OrderPageLocators.PHONE),
            self.find_visible_element(OrderPageLocators.PAYMENT_METHOD),
            self.find_visible_element(OrderPageLocators.COMMENT),
            self.find_visible_element(OrderPageLocators.REQUIREMENTS)
        ]
        return all(conditions)

    @allure.step('Разворачивание блока рекомендаций')
    def open_requirements_block(self):
        self.scroll_to_element(OrderPageLocators.REQUIREMENTS)
        self.click_element(OrderPageLocators.REQUIREMENTS)


    @allure.step('Выбор тумблера ноутбука')
    def click_notebook_checkbox(self):
        self.click_element(OrderPageLocators.NOTEBOOK_TOGGLE)

    @allure.step('Нажатие кнопку Ввести номер и заказать')
    def click_enter_number_and_order_button(self):
        self.click_element(OrderPageLocators.ENTER_NUMBER_AND_ORDER_BUTTON)

    @allure.step('Появление окна поиска машины')
    def taxi_search_window(self):
        return self.find_visible_element(OrderPageLocators.ORDER_WINDOW)

    @allure.step('Ожидание 30 секунд')
    def wait_29_seconds(self):
        self.driver.execute_async_script("""
            var callback = arguments[arguments.length - 1];
            setTimeout(function() { 
                callback(true); 
            }, 29000);
        """)

    @allure.step('Проверка отображения окна заказа')
    def order_details_block(self):
        self.wait_29_seconds()
        conditions = [
            self.find_visible_element(OrderPageLocators.ORDER_WINDOW),
            self.find_visible_element(OrderPageLocators.DRIVER_PICTURE),
            self.find_visible_element(OrderPageLocators.DETAILS_BUTTON),
            self.find_visible_element(OrderPageLocators.CANCEL_BUTTON)
        ]
        return all(conditions)

    @allure.step('Получение цены заказа')
    def get_order_price(self):
        return self.get_text(OrderPageLocators.WORK_TARIFF_PRICE)

    @allure.step('Нажатие кнопки Детали')
    def click_order_details_button(self):
        self.click_element(OrderPageLocators.DETAILS_BUTTON)

    @allure.step('Сравнение цены заказа в деталях с заявленной')
    def order_price_equal(self, order_price):
        details_price = self.get_text(OrderPageLocators.DETAILS_PRICE)
        details_price_number = details_price.replace('Стоимость - ', '').replace('₽', '')
        return details_price_number == order_price.replace(' ₽', '')

    @allure.step('Нажатие кнопки Отменить')
    def click_cancel_button(self):
        self.click_element(OrderPageLocators.CANCEL_BUTTON)

    @allure.title('Проверка закрытия окна заказа')
    def order_details_block_not_present(self):
        return self.wait_for_invisibility(OrderPageLocators.CANCEL_BUTTON)


