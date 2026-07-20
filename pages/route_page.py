import allure
from locators.route_page_locators import RoutePageLocators
from pages.base_page import BasePage


class RoutePage(BasePage):

    @allure.step('Проверка открытия страницы маршрута')
    def route_page_loaded(self):
        conditions = [
            self.find_visible_element(RoutePageLocators.ROUTE_BLOCK)
        ]
        return all(conditions)

    @allure.step('Сравнение текстового сообщения результата с ожидаемым текстом')
    def is_results_equal(self, expected_text, expected_duration):
        conditions = [
            self.get_text(RoutePageLocators.RESULT_TEXT) == expected_text,
            self.get_text(RoutePageLocators.RESULT_DURATION) == expected_duration
        ]
        return all(conditions)

    @allure.step('Получение цены тарифа')
    def route_result_price(self):
        return self.get_text(RoutePageLocators.RESULT_TEXT)

    @allure.step('Получение продолжительности поездки')
    def route_result_duration(self):
        return self.get_text(RoutePageLocators.RESULT_DURATION)

    @allure.step('Переключение на тариф Оптимальный')
    def route_switch_optimal(self):
        self.click_element(RoutePageLocators.ROUTE_MODE_OPTIMAL)

    @allure.step('Переключение на тариф Свой')
    def route_switch_personal(self):
        self.click_element(RoutePageLocators.ROUTE_MODE_PERSONAL)

    @allure.step('Переключение на Драйв')
    def transport_switch_drive(self):
        self.click_element(RoutePageLocators.TRANSPORT_TYPE_DRIVE)

    @allure.step('Переключение на тариф Быстрый')
    def route_switch_fast(self):
        self.click_element(RoutePageLocators.ROUTE_MODE_FAST)

    @allure.step('Проверка активности всех типов передвижения')
    def get_enabled_transport_types(self):
        return self.find_visible_elements(RoutePageLocators.TRANSPORT_TYPES_ENABLED)

    @allure.step('Проверка активности кнопки Вызвать такси')
    def taxi_order_button_check(self):
        return self.find_visible_element(RoutePageLocators.ORDER_TAXI_BUTTON)

    @allure.step('Нажатие кнопки Вызвать такси')
    def taxi_order_button_click(self):
        self.click_element(RoutePageLocators.ORDER_TAXI_BUTTON)

    @allure.step('Проверка активности кнопки Забронировать')
    def taxi_book_button_check(self):
        return self.find_visible_element(RoutePageLocators.BOOK_BUTTON)



