import allure
from data import ADDRESS_FROM, ADDRESS_TO, TARIFFS
from pages.main_page import MainPage
from pages.route_page import RoutePage
from pages.order_page import OrderPage
import pytest

@allure.title('Тестовые сценарии блока заказа такси')
class TestOrderPage:

    @allure.title('Открывается форма заказа со всеми 6 тарифами по ТЗ, один из них активный')
    def test_order_form_six_tariffs_with_one_active_present_success(self,driver):
        main_page = MainPage(driver)
        main_page.enter_route(ADDRESS_FROM, ADDRESS_TO)
        route_page = RoutePage(driver)
        route_page.route_page_loaded()
        route_page.route_switch_fast()
        route_page.taxi_order_button_click()
        order_page = OrderPage(driver)
        assert order_page.order_page_loaded() and order_page.tariff_titles_match() and order_page.count_of_active_tariffs() == 1


    @allure.title('При наведении на иконку i в правом верхнем углу каждого тарифа отображается всплывающее окно с описанием тарифа, описание тарифа соответствует ТЗ')
    @pytest.mark.xfail(reason="BUG: описания тарифов Сонный и Разговорчивый не совпадают с ТЗ")
    @pytest.mark.parametrize("tariff_name", TARIFFS.keys())
    def test_tariffs_descriptions_success(self, driver, tariff_name):
        main_page = MainPage(driver)
        main_page.enter_route(ADDRESS_FROM, ADDRESS_TO)
        route_page = RoutePage(driver)
        route_page.route_page_loaded()
        route_page.route_switch_fast()
        route_page.taxi_order_button_click()
        order_page = OrderPage(driver)
        order_page.order_page_loaded()
        tariff_description = order_page.get_tariff_information_by_name(tariff_name)

        assert tariff_description == TARIFFS[tariff_name]


    @allure.title('Под тарифами отображается блок с полями Телефон, Способ оплаты, Комментарий водителю, Требования к заказу Заказ тарифа Такси')
    def test_block_with_phone_payment_comment_requirements_present_success(self, driver):
        main_page = MainPage(driver)
        main_page.enter_route(ADDRESS_FROM, ADDRESS_TO)
        route_page = RoutePage(driver)
        route_page.route_page_loaded()
        route_page.route_switch_fast()
        route_page.taxi_order_button_click()
        order_page = OrderPage(driver)
        order_page.order_page_loaded()
        assert order_page.order_block()

    @allure.title('Выбираем тариф Рабочий, включаем чекбокс Столик для ноутбука, нажимаем кнопку Ввести номер и заказать - Появляется окно ожидания машины ')
    def test_change_route_to_working_select_notebook_table_press_order_taxi_search_window_appears_success(self, driver):
        main_page = MainPage(driver)
        main_page.enter_route(ADDRESS_FROM, ADDRESS_TO)
        route_page = RoutePage(driver)
        route_page.route_page_loaded()
        route_page.route_switch_fast()
        route_page.taxi_order_button_click()
        order_page = OrderPage(driver)
        order_page.order_page_loaded()
        order_page.open_requirements_block()
        order_page.click_notebook_checkbox()
        order_page.click_enter_number_and_order_button()
        assert order_page.taxi_search_window()

    @allure.title('Дождаться окончания таймера поиска машины - Отображается окно совершенного заказа')
    def test_wait_for_taxi_search_completion_order_complete_window_is_shown_success(self, driver):
        main_page = MainPage(driver)
        main_page.enter_route(ADDRESS_FROM, ADDRESS_TO)
        route_page = RoutePage(driver)
        route_page.route_page_loaded()
        route_page.route_switch_fast()
        route_page.taxi_order_button_click()
        order_page = OrderPage(driver)
        order_page.order_page_loaded()
        order_page.click_enter_number_and_order_button()
        assert order_page.order_details_block()

    @allure.title('Нажать кнопку Детали в блоке Еще про поездку - Указана стоимость, которая была при выборе тарифа')
    def test_order_details_shown_same_price_as_before_order_success(self, driver):
        main_page = MainPage(driver)
        main_page.enter_route(ADDRESS_FROM, ADDRESS_TO)
        route_page = RoutePage(driver)
        route_page.route_page_loaded()
        route_page.route_switch_fast()
        route_page.taxi_order_button_click()
        order_page = OrderPage(driver)
        order_page.order_page_loaded()
        order_price = order_page.get_order_price()
        order_page.click_enter_number_and_order_button()
        order_page.order_details_block()
        order_page.click_order_details_button()

        assert order_page.order_price_equal(order_price)

    @allure.title('Нажать кнопку Отмена - Окно закрывается')
    def test_order_window_closes_success(self, driver):
        main_page = MainPage(driver)
        main_page.enter_route(ADDRESS_FROM, ADDRESS_TO)
        route_page = RoutePage(driver)
        route_page.route_page_loaded()
        route_page.route_switch_fast()
        route_page.taxi_order_button_click()
        order_page = OrderPage(driver)
        order_page.order_page_loaded()
        order_page.click_enter_number_and_order_button()
        order_page.order_details_block()
        order_page.click_cancel_button()
        assert order_page.order_details_block_not_present()