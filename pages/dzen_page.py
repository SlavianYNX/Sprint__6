import allure
from pages.base_page import BasePage
from locators.dzen_page_locators import DzenPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class DzenPage(BasePage):

    @allure.step('Проверка отображения кнопки "Главная" на странице Дзен')
    def check_element_main_button(self):
        return self.find_and_wait_locator(DzenPageLocators.MAIN_BUTTON_DZEN)

    @allure.step('Проверка отображения логотипа "Дзен"')
    def check_element_logo_dzen(self):
        return self.find_and_wait_locator(DzenPageLocators.LOGO_DZEN)



