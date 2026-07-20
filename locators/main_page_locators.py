from selenium.webdriver.common.by import By

class MainPageLocators:
    INPUT_FROM = By.ID, "from"
    INPUT_TO = By.ID, "to"
    ROUTE_FROM_TO = By.XPATH, ".//ymaps[contains(@id, 'id_')]"
    ROUTE_PIN_A = (By.XPATH, "//ymaps[contains(@class,'route-pin__label-a')]")
    ROUTE_PIN_B = (By.XPATH, "//ymaps[contains(@class,'route-pin__label-b')]")