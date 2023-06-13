# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

sbis_ru = 'https://sbis.ru/'
tensor_ru = 'https://tensor.ru/'
about = 'https://tensor.ru/about'

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--enable-javascript")

driver = webdriver.Chrome()
action_chains = ActionChains(driver)


class Test1:

    def test_task_1(self):

        try:
            driver.get(sbis_ru)
            sleep(2)
            contacts = driver.find_element(By.PARTIAL_LINK_TEXT, 'Контакты')
            contacts.click()
            sleep(2)

            tensor_logo = driver.find_element(By.CLASS_NAME, 'sbisru-Contacts__logo-tensor')
            tensor_logo.click()
            driver.switch_to.window(driver.window_handles[1])
            sleep(2)

            power_of_people = driver.find_element(By.XPATH, '//*[contains(text(), "Сила в людях")]')
            assert power_of_people.is_displayed()
            about_lnk = driver.find_elements(By.CLASS_NAME, 'tensor_ru-Index__link')[1]
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'auto', block: 'center'});", about_lnk)
            sleep(2)
            assert about_lnk.is_displayed()
            about_lnk.click()
            sleep(2)

            assert driver.current_url == about
        finally:
            driver.quit()
