# Перейти на  https://sbis.ru/
# В Footer'e найти "Скачать СБИС"
# Перейти по ней.
# Скачать СБИС Плагин для вашей ОС в папку с данным тестом
# Убедиться, что плагин скачался.
# Вывести на печать размер скачанного файла в мегабайтах
# Для сдачи задания пришлите код и запись с экрана прохождения теста
import os
from pathlib import Path
from time import sleep
from urllib import request

from selenium import webdriver
from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait as Wait

driver = webdriver.Chrome()
sbis_ru = 'https://sbis.ru/'
ignored_exceptions = (NoSuchElementException, StaleElementReferenceException)


class Test3:

    def test_task_with_star(self):
        try:
            driver.get(sbis_ru)
            sleep(1)
            download_sbis = driver.find_element(By.XPATH, '//a[contains(text(), "Скачать СБИС")]')
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'auto', block: 'center'});", download_sbis)
            download_sbis.click()
            sleep(1)

            driver.find_element(By.CSS_SELECTOR, '[data-id="plugin"]').click()
            sleep(1)
            download_lnk = Wait(driver, 10, ignored_exceptions=ignored_exceptions).until(ec.element_to_be_clickable((
                By.XPATH, '//a[contains(@href, "setup-web.exe")]'
            )))
            url = download_lnk.get_attribute('href')
            filename = Path(url).name
            request.urlretrieve(url, filename)

            assert os.path.exists(filename), f'Файл {filename} не скачан!'
        finally:
            driver.quit()
