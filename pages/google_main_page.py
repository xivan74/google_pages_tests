import allure
from selene.support.shared import browser
from selene import be, have


class GoogleMainPage:
    url = "https://google.com"
    search_input_locator = "[name=q]"
    search_input_cross_locator = "[role='button'][jsname='pkjasb']"

    def open(self):
        browser.open(self.url)

    @allure.step("Click to search input")
    def click_to_search_input(self):
        browser.element(self.search_input_locator).click()

    @allure.step("Fill search input with text")
    def fill_search_input(self, text):
        browser.element(self.search_input_locator).type(text)

    @allure.step("Click to search input cross")
    def clear_search_input(self):
        browser.element(self.search_input_cross_locator).click()

    @allure.step("Search input is empty")
    def search_input_is_empty(self):
        return browser.element(self.search_input_locator).matching(be.blank)

    @allure.step("Search input is not empty")
    def search_input_is_not_empty(self):
        return browser.element(self.search_input_locator).matching(be.not_.blank)

    @allure.step("Search input cross is visible")
    def search_input_have_cross(self):
        return browser.element(self.search_input_cross_locator).matching(be.visible)

    @allure.step("Search input cross is not visible")
    def search_input_have_not_cross(self):
        return browser.element(self.search_input_cross_locator).matching(be.not_.visible)

    def search_input_history_list_is_visible(self):
        pass

    def search_input_history_item_is_visible(self, item_text):
        pass

    def delete_search_input_history_item(self, item_text):
        pass

