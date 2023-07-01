from selene.support.shared import browser
from selene import be, have


class GoogleMainPage:
    url = "https://google.com"
    search_input_locator = "[name=q]"
    search_input_cross_locator = "[role='button'][jsname='pkjasb']"

    def open(self):
        browser.open(self.url)

    def click_to_search_input(self):
        browser.element(self.search_input_locator).click()

    def fill_search_input(self, text):
        browser.element(self.search_input_locator).type(text)

    def clear_search_input(self):
        browser.element(self.search_input_cross_locator).click()

    def search_input_is_empty(self):
        return browser.element(self.search_input_locator).matching(be.blank)

    def search_input_have_cross(self):
        return browser.element(self.search_input_cross_locator).matching(be.visible)

    def search_input_history_list_is_visible(self):
        pass

    def search_input_history_item_is_visible(self, item_text):
        pass

    def delete_search_input_history_item(self, item_text):
        pass

