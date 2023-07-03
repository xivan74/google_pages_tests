import allure
from selene.support.shared import browser
from selene import be, have


class GoogleMainPage:
    url = "https://google.com"
    search_input_locator = "[name=q]"
    search_input_cross_locator = "[role='button'][jsname='pkjasb']"

    @allure.step("Открытие главной страницы Google")
    def open(self):
        browser.open(self.url)
        return self

    @allure.step("Клик в поле поиска")
    def click_to_search_input(self):
        browser.element(self.search_input_locator).click()
        return self

    @allure.step("Ввод текста в поле поиска")
    def fill_search_input(self, text):
        browser.element(self.search_input_locator).type(text)
        return self

    @allure.step("Клик в крестик в поле поиска")
    def clear_search_input(self):
        browser.element(self.search_input_cross_locator).click()
        return self

    @allure.step("Поле ввода пустое")
    def search_input_is_empty(self):
        browser.element(self.search_input_locator).should(be.blank)
        return self

    @allure.step("Поле ввода не пустое")
    def search_input_is_not_empty(self):
        browser.element(self.search_input_locator).should(be.not_.blank)
        return self

    @allure.step("Крестик в поле поиска виден")
    def search_input_has_cross(self):
        browser.element(self.search_input_cross_locator).should(be.visible)
        return self

    @allure.step("Крестик в поле поиска не виден")
    def search_input_has_no_cross(self):
        browser.element(self.search_input_cross_locator).should(be.not_.visible)
        return self

    def search_input_history_list_is_visible(self):
        pass

    def search_input_history_item_is_visible(self, item_text):
        pass

    def delete_search_input_history_item(self, item_text):
        pass

