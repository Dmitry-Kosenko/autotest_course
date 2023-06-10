# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты.
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре.
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста
import random
import string
from time import sleep

from selenium import webdriver
from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait as Wait

login, password = 'kosenko_at', 'kosenko_at1234'
user_name = 'Косенко Авто'
random_text = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(1, 50)))

online = 'https://fix-online.sbis.ru/'
contacts_url = 'https://fix-online.sbis.ru/page/dialogs'

driver = webdriver.Chrome()
action_chains = ActionChains(driver)
ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)


def click_on_elm(by: By.ID, val: str):
    Wait(driver, 10, ignored_exceptions=ignored_exceptions).until(ec.element_to_be_clickable((
        by, val
    ))).click()


class Test2:

    def test_task_2(self):
        try:
            driver.get(online)
            sleep(.3)

            driver.find_element(By.NAME, 'Login').send_keys(login, Keys.ENTER)
            sleep(.3)
            driver.find_element(By.NAME, 'Password').send_keys(password + Keys.ENTER)
            Wait(driver, 10).until(ec.url_to_be(online))
            assert driver.current_url == online, 'Неверный url в адресной строке'

            click_on_elm(By.NAME, 'item-contacts')
            click_on_elm(By.NAME, 'headTitle')

            assert driver.current_url == contacts_url, 'Неверный url в адресной строке'

            click_on_elm(By.CLASS_NAME, 'sabyPage-MainLayout__addButton')

            # sleep(2)
            def presence_of_two_elements(drv):
                elements = drv.find_elements(By.CSS_SELECTOR,
                                             '[class="controls-Field js-controls-Field controls-InputBase__nativeField '
                                             'controls-Search__nativeField_caretEmpty '
                                             'controls-Search__nativeField_caretEmpty_theme_default   '
                                             'controls-InputBase__nativeField_hideCustomPlaceholder"]')
                if len(elements) == 2:
                    return elements
                else:
                    return False

            find_inp = Wait(driver, 10, ignored_exceptions=ignored_exceptions).until(presence_of_two_elements)[0]

            find_inp.send_keys(user_name)
            click_on_elm(By.CSS_SELECTOR, f'[data-qa="msg-addressee-selector__plain-list-view"] [title="{user_name}"]')

            Wait(driver, 10, ignored_exceptions=ignored_exceptions).until(ec.element_to_be_clickable((
                By.CLASS_NAME, 'textEditor_Viewer__Paragraph'))).send_keys(random_text, Keys.CONTROL + Keys.ENTER)

            message = Wait(driver, 10, ignored_exceptions=ignored_exceptions).until(ec.element_to_be_clickable((
                By.XPATH, f'//p[contains(text(), "{random_text}")]')))

            action_chains.move_to_element(message).perform()

            click_on_elm(By.XPATH, '//div[@class="controls-itemActionsV__wrapper"]//i[contains(@class, "icon-Erase")]')
            sleep(.2)

            assert len(
                driver.find_elements(By.XPATH, f'//p[contains(text(), "{random_text}")]')) == 0, 'Сообщение не удалено'
            sleep(3)
        finally:
            driver.quit()
