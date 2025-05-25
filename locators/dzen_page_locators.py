from selenium.webdriver.common.by import By


class DzenPageLocators:
    MAIN_BUTTON_DZEN = (By.XPATH, ".//div[2]/span[text()='Главная']")
    LOGO_DZEN = (By.XPATH, ".//a[@class='dzen-layout--desktop-base-header__logoLink-2h']")