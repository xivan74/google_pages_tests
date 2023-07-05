import allure
from selene.support.shared import browser
from selene import be, have
from random import randint


class GoogleMainPage:
    url = "https://google.com"
    SEARCH_INPUT_LOCATOR = "[name='q'][type='search']"
    SEARCH_INPUT_CROSS_LOCATOR = "[role='button'][jsname='pkjasb']"
    # Встречается 3 вида выпадающих списков. У каждого из них своя специфика.
    # Список с подсказками. Появляется, когда что-то введено в строку поиска. В этом списке может быть рекламная строка
    SEARCH_INPUT_SUGGEST_LIST = "//ul[@role='listbox'][@jsname='bw4e9b'][.//*[contains(@class, 'sb43')" \
                                "and contains(@class, 'sbic')]]"
    # Список с историей предыдущих поисков. Виден, когда ничего не введено, и имеется история поиска
    SEARCH_INPUT_HISTORY_LIST = "//ul[@role='listbox'][@jsname='bw4e9b'][.//*[contains(@class, 'sb27')" \
                                "and contains(@class, 'sbic')]]"
    # Список "Популярные запросы". Виден, когда ничего не введено, и истории поиска нет (не во всех языках интерфейса)
    SEARCH_INPUT_RECOMMENDATIONS_LIST = "//ul[@role='listbox'][@jsname='bw4e9b'][.//*[contains(@class, 'sb33')" \
                                        "and contains(@class, 'sbic')]]"
    SEARCH_INPUT_LIST_ITEM = "//ul[@role='listbox'][@jsname='bw4e9b']//li"
    SEARCH_INPUT_LIST_ITEM_TEXT = ".//*[contains(@class, 'wM6W7d')]/*"

    @allure.step("Открытие главной страницы Google")
    def open(self):
        browser.open(self.url)
        return self

    @allure.step("Клик в поле поиска")
    def click_to_search_input(self):
        browser.element(self.SEARCH_INPUT_LOCATOR).click()
        return self

    @allure.step("Ввод текста в поле поиска")
    def fill_search_input(self, text: str):
        browser.element(self.SEARCH_INPUT_LOCATOR).type(text)
        return self

    @allure.step("Клик в крестик в поле поиска")
    def clear_search_input(self):
        browser.element(self.SEARCH_INPUT_CROSS_LOCATOR).click()
        return self

    @allure.step("Поле ввода пустое")
    def search_input_is_empty(self):
        browser.element(self.SEARCH_INPUT_LOCATOR).should(be.blank)
        return self

    @allure.step("Поле ввода не пустое")
    def search_input_is_not_empty(self):
        browser.element(self.SEARCH_INPUT_LOCATOR).should(be.not_.blank)
        return self

    @allure.step("Поле ввода содержит нужный текст")
    def search_input_have_correct_text(self, text: str):
        browser.element(self.SEARCH_INPUT_LOCATOR).should(have.text(text))
        return self

    @allure.step("Крестик в поле поиска виден")
    def search_input_has_cross(self):
        browser.element(self.SEARCH_INPUT_CROSS_LOCATOR).should(be.visible)
        return self

    @allure.step("Крестик в поле поиска не виден")
    def search_input_has_no_cross(self):
        browser.element(self.SEARCH_INPUT_CROSS_LOCATOR).should(be.not_.visible)
        return self

    @allure.step("Список подсказок виден")
    def search_input_suggest_list_is_visible(self):
        browser.element(self.SEARCH_INPUT_SUGGEST_LIST).should(be.visible)
        return self

    @allure.step("Список подсказок не виден")
    def search_input_suggest_list_not_visible(self):
        browser.element(self.SEARCH_INPUT_SUGGEST_LIST).should(be.not_.visible)
        return self

    @allure.step("Список истории виден")
    def search_input_history_list_is_visible(self):
        browser.element(self.SEARCH_INPUT_HISTORY_LIST).should(be.visible)
        return self

    @allure.step("Список истории не виден")
    def search_input_history_list_not_visible(self):
        browser.element(self.SEARCH_INPUT_HISTORY_LIST).should(be.not_.visible)
        return self

    @allure.step("Список рекоммендаций виден")
    def search_input_recommendations_list_is_visible(self):
        browser.element(self.SEARCH_INPUT_RECOMMENDATIONS_LIST).should(be.visible)
        return self

    @allure.step("Список рекоммендаций не виден")
    def search_input_recommendations_list_not_visible(self):
        browser.element(self.SEARCH_INPUT_RECOMMENDATIONS_LIST).should(be.not_.visible)
        return self

    @allure.step("Клик на случайную подсказку")
    def click_to_any_suggest_list_item(self):
        suggest_list = browser.element(self.SEARCH_INPUT_SUGGEST_LIST)
        suggest_list_items = suggest_list.all(self.SEARCH_INPUT_LIST_ITEM)
        item_index = randint(0, len(suggest_list_items))
        suggest_list_item = suggest_list_items[item_index]
        suggest_list_item_text = suggest_list_item.locate().text
        suggest_list_item.click()
        return suggest_list_item_text

    def click_to_suggest_list_item_with_text(self, item_text):
        pass

    def search_input_history_item_is_visible(self, item_text):
        pass

    def delete_search_input_history_item(self, item_text):
        pass
