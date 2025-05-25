import allure
from pages.base_page import BasePage
from locators.dzen_page_locators import DzenPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class DzenPage(BasePage):

    @allure.step('Проверка отображения кнопки "Главная" на странице Дзен')
    def check_element_main_button(self):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(DzenPageLocators.MAIN_BUTTON_DZEN))

