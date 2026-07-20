import allure
from locators.main_page_locators import MainPageLocators
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage
from data import BASE_URL

class MainPage(BasePage):

    @allure.step('Переход на главную страницу')
    def open_main_page(self):
        self.go_to_url(BASE_URL)

    @allure.step('Проверка открытия главной страницы')
    def main_page_loaded(self):
        conditions = [
            self.find_visible_element(MainPageLocators.INPUT_FROM),
            self.find_visible_element(MainPageLocators.INPUT_TO)
        ]
        return all(conditions)

    @allure.step('Проверка отображения на карте линии машрута')
    def wait_route_visible(self):
        self.wait_for_visibility_all_elements(MainPageLocators.ROUTE_FROM_TO)


    @allure.step('Проверка отображения на карте двух точек машрута')
    def wait_pins_visible(self):
        try:
            self.find_visible_element(MainPageLocators.ROUTE_PIN_A)
            self.find_visible_element(MainPageLocators.ROUTE_PIN_B)
            return True
        except TimeoutException:
            return False

    @allure.step('Проверка отрисовки маршрута')
    def enter_route(self, address_from: str, address_to: str):
        self.open_main_page()
        self.main_page_loaded()
        self.find_visible_element(MainPageLocators.INPUT_FROM)
        self.send_text(MainPageLocators.INPUT_FROM, address_from)
        self.find_visible_element(MainPageLocators.INPUT_TO)
        self.send_text(MainPageLocators.INPUT_TO, address_to)
        self.wait_route_visible()

