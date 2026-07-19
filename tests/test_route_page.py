import allure
import pytest
from pages.main_page import MainPage
from pages.route_page import RoutePage
from data import ADDRESS_FROM, ADDRESS_TO, SAME_FROM_TO_TEXT, SAME_FROM_TO_DURATION

@allure.title('Тестовые сценарии страницы заказа')

class TestRoutePage:

    @allure.title('При вводе двух разных предустановленных адресов в поля "Откуда" и "Куда" под выбором адресов отображается блок с выбором маршрута')
    @pytest.mark.parametrize('address_from, address_to',
                             [
                                 (ADDRESS_FROM, ADDRESS_TO),
                                 (ADDRESS_TO, ADDRESS_FROM),
                             ]
                             )
    def test_route_page_from_to_different_route_block_present_success(self,address_from, address_to, driver):
        main_page = MainPage(driver)
        main_page.enter_route(address_from, address_to)
        route_page = RoutePage(driver)
        assert route_page.route_page_loaded()


    @allure.title('При вводе одинакового адреса в поля "Откуда" и "Куда" под выбором адресов отображается блок с выбором маршрута с текстом "Авто Бесплатно В пути 0 мин."')
    @pytest.mark.parametrize('address_from, address_to',
                             [
                                 (ADDRESS_FROM, ADDRESS_FROM),
                                 (ADDRESS_TO, ADDRESS_TO),
                             ]
                             )
    def test_route_page_from_to_same_route_block_present_free_ride_success(self, address_from, address_to, driver):
        main_page = MainPage(driver)
        main_page.enter_route(address_from, address_to)
        route_page = RoutePage(driver)
        assert route_page.is_results_equal(expected_text=SAME_FROM_TO_TEXT,
                                                     expected_duration=SAME_FROM_TO_DURATION)


    @allure.title('При переключении между видами маршрута (Оптимальный\Быстрый) происходит смена активного таба и пересчет времени и стоимости маршрута')
    @pytest.mark.xfail(reason="BUG: время при смене маршрута не меняется")
    def test_route_page_change_route_fast_to_optimal_success(self, driver):
        main_page = MainPage(driver)
        main_page.enter_route(ADDRESS_FROM, ADDRESS_TO)
        route_page = RoutePage(driver)
        route_page.route_page_loaded()
        price_fast = route_page.route_result_price()
        duration_fast = route_page.route_result_duration()
        route_page.route_switch_optimal()
        price_optimal = route_page.route_result_price()
        duration_optimal = route_page.route_result_duration()
        assert price_fast != price_optimal and duration_fast != duration_optimal


    @allure.title('При переключении на вид маршрута Свой происходит смена активного таба и становятся активны типы передвижения (Машина, Пешком, Такси, Велосипед, Самокат, Драйв)')
    def test_route_page_change_route_to_personal_all_transport_types_became_active_success(self, driver):
        main_page = MainPage(driver)
        main_page.enter_route(ADDRESS_FROM, ADDRESS_TO)
        route_page = RoutePage(driver)
        route_page.route_page_loaded()
        route_page.route_switch_personal()
        assert route_page.get_enabled_transport_types()


    @allure.title('При выборе вида маршрута Быстрый активна кнопка Вызвать такси')
    def test_route_page_change_route_to_fast_order_taxi_button_available_success(self, driver):
        main_page = MainPage(driver)
        main_page.enter_route(ADDRESS_FROM, ADDRESS_TO)
        route_page = RoutePage(driver)
        route_page.route_page_loaded()
        route_page.route_switch_fast()
        assert route_page.taxi_order_button_check()


    @allure.title('При выборе вида маршрута Свой, типа передвижения Драйв активна кнопка Забронировать')
    def test_route_page_change_route_to_personal_and_drive_booking_button_available_success(self, driver):
        main_page = MainPage(driver)
        main_page.enter_route(ADDRESS_FROM, ADDRESS_TO)
        route_page = RoutePage(driver)
        route_page.route_page_loaded()
        route_page.route_switch_personal()
        route_page.transport_switch_drive()
        assert route_page.taxi_book_button_check()