import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step('Переход по урлу')
    def go_to_url(self, url):
        self.driver.get(url)

    @allure.step('Найти элемент на странице')
    def find_visible_element(self, locator):
        try:
            element = self.wait_for_visibility(locator)
            return element
        except:
            return None

    @allure.step('Найти все элементы по локатору')
    def find_visible_elements(self, locator):
        self.wait.until(expected_conditions.presence_of_all_elements_located(locator))
        elements = self.driver.find_elements(*locator)
        return elements

    @allure.step(title='Ожидание отображения элемента')
    def wait_for_visibility(self, locator):
        return self.wait.until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Ожидание отображения всех элементов')
    def wait_for_visibility_all_elements(self, locator):
        self.wait.until(expected_conditions.visibility_of_all_elements_located(locator))

    @allure.step('Ввод текста в элемент')
    def send_text(self, locator, text):
        element = self.find_visible_element(locator)
        element.send_keys(text)

    @allure.step('Получение текста элемента')
    def get_text(self, locator):
        return self.find_visible_element(locator).text

    @allure.step('Клик по элементу')
    def click_element(self, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(locator))
        self.find_visible_element(locator).click()

    @allure.step('Наведение курсора на элемент')
    def move_to_element(self, locator):
        element = self.find_visible_element(locator)
        if element:
            ActionChains(self.driver).move_to_element(element).perform()

    @allure.step('Ожидание скрытия элемента')
    def wait_for_invisibility(self, locator):
        return self.wait.until(expected_conditions.invisibility_of_element_located(locator))

    @allure.step('Перемотать страницу к элементу')
    def scroll_to_element(self, locator):
        element = self.find_visible_element(locator)
        if element:
            try:
                actions = ActionChains(self.driver)
                actions.move_to_element(element).perform()
            except:
                self.driver.execute_script("arguments[0].scrollIntoView();", element)

