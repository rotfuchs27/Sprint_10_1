from selenium.webdriver.common.by import By


class RoutePageLocators:
    ROUTE_BLOCK = By.XPATH, ".//div[contains(@class, 'type-picker shown')]"
    RESULT_TEXT = By.XPATH, ".//div[@class='results-text']/div[@class='text']"
    RESULT_DURATION = By.XPATH, ".//div[@class='results-text']/div[@class='duration']"
    ROUTE_MODE_OPTIMAL = By.XPATH, ".//div[@class='modes-container']/div[text()='Оптимальный']"
    ROUTE_MODE_PERSONAL = By.XPATH, ".//div[@class='modes-container']/div[text()='Свой']"
    ROUTE_MODE_FAST = By.XPATH, ".//div[@class='modes-container']/div[text()='Быстрый']"
    TRANSPORT_TYPES_ENABLED = By.XPATH, ".//div[@class='types-container']/div[not(contains(@class, 'disabled'))]"
    ORDER_TAXI_BUTTON = By.XPATH, ".//button[text()='Вызвать такси']"
    TRANSPORT_TYPE_DRIVE = By.XPATH, ".//div[@class='types-container']/div[contains(@class, 'type drive')]"
    BOOK_BUTTON = By.XPATH, ".//button[text()='Забронировать']"