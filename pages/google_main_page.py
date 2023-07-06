import allure
from selene.support.shared import browser
from selene import be, have
from random import randint


class GoogleMainPage:
    url = "https://google.com"
    SEARCH_INPUT = "[name='q'][type='search']"
    SEARCH_INPUT_CROSS = "[role='button'][jsname='pkjasb']"
    SEARCH_RESULTS = "#search"
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
    SEARCH_INPUT_LIST_ITEM = ".//li"
    SEARCH_INPUT_LIST_ITEM_TEXT = ".//*[contains(@class, 'wM6W7d')]/*"
    HIGHLIGHTED_SEARCH_ITEM_CLASS_NAME = "sbhl"

    @allure.step("Открыть главную страницу Google")
    def open(self):
        browser.open(self.url)
        return self

    @allure.step("Кликнуть в поле поиска")
    def click_to_search_input(self):
        browser.element(self.SEARCH_INPUT).click()
        return self

    @allure.step("Ввести текст в поле поиска")
    def fill_search_input(self, text: str):
        browser.element(self.SEARCH_INPUT).type(text)
        return self

    @allure.step("Кликнуть в крестик в поле поиска")
    def clear_search_input(self):
        browser.element(self.SEARCH_INPUT_CROSS).click()
        return self

    @allure.step("Поле ввода пустое")
    def search_input_is_empty(self):
        browser.element(self.SEARCH_INPUT).should(be.blank)
        return self

    @allure.step("Поле ввода не пустое")
    def search_input_is_not_empty(self):
        browser.element(self.SEARCH_INPUT).should(be.not_.blank)
        return self

    @allure.step("Поле ввода содержит нужный текст")
    def search_input_have_correct_text(self, text: str):
        browser.element(self.SEARCH_INPUT).should(have.text(text))
        return self

    @allure.step("Крестик в поле поиска виден")
    def search_input_has_cross(self):
        browser.element(self.SEARCH_INPUT_CROSS).should(be.visible)
        return self

    @allure.step("Крестик в поле поиска не виден")
    def search_input_has_no_cross(self):
        browser.element(self.SEARCH_INPUT_CROSS).should(be.not_.visible)
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

    @allure.step("Кликнуть на любую подсказку")
    def click_to_any_suggest_list_item(self):
        suggest_list = browser.element(self.SEARCH_INPUT_SUGGEST_LIST)
        suggest_list_items = suggest_list.all(self.SEARCH_INPUT_LIST_ITEM)
        item_index = randint(0, len(suggest_list_items) - 1)
        suggest_list_item = suggest_list_items[item_index]
        suggest_list_item_text = suggest_list_item.locate().text
        suggest_list_item.click()
        return suggest_list_item_text

    @allure.step("Навести мышь на любую подсказку")
    def hover_to_any_suggest_list_item(self):
        suggest_list = browser.element(self.SEARCH_INPUT_SUGGEST_LIST)
        suggest_list_items = suggest_list.all(self.SEARCH_INPUT_LIST_ITEM)
        item_index = randint(0, len(suggest_list_items) - 1)
        suggest_list_item = suggest_list_items[item_index]
        suggest_list_item.hover()
        return suggest_list_item

    @allure.step("Осуществить поиск по текстовому запросу")
    def make_search(self, text: str):
        self.fill_search_input(text=text)
        browser.element(self.SEARCH_INPUT).press_enter()
        return self

    @allure.step("Видны результаты поиска")
    def search_results_are_visible(self):
        browser.element(self.SEARCH_RESULTS).should(be.visible)
        return self

    @allure.step("Элемент подсказки подсвечен")
    def list_item_is_highlighted(self, list_item):
        list_item.should(have.css_class(self.HIGHLIGHTED_SEARCH_ITEM_CLASS_NAME))
        return self

    @allure.step("Подсвечен ровно один элемент подсказки")
    def single_list_item_is_highlighted_only(self):
        suggest_list = browser.element(self.SEARCH_INPUT_SUGGEST_LIST)
        suggest_list.all(self.SEARCH_INPUT_LIST_ITEM) \
            .by(have.css_class(self.HIGHLIGHTED_SEARCH_ITEM_CLASS_NAME)) \
            .should(have.size(1))
        return self

    def click_to_suggest_list_item_with_text(self, item_text):
        pass

    def search_input_history_item_is_visible(self, item_text):
        pass

    def delete_search_input_history_item(self, item_text):
        pass
