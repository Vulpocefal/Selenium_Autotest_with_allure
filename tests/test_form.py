import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    # Selenium Manager will auto-download the appropriate driver
    options = Options()
    options.add_argument("--headless")  # run without UI
    options.add_argument("--no-sandbox")  # required in many CI environments
    options.add_argument("--disable-dev-shm-usage")  # overcome limited /dev/shm size on Linux

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@allure.epic("Авторизация на тестовом сайте")
@allure.title("Авторизация с валидными данными")
@allure.description("Имитация действий пользователя с помощью Selenium")
def test_successful_login(driver):
    with allure.step("Открытие страницы авторизации тестового сайта"):
        driver.get("https://the-internet.herokuapp.com/login")

    with allure.step("Ввод валидного логина"):
        text_input = driver.find_element(By.ID, 'username')
        text_input.clear()
        text_input.send_keys('tomsmith')

    with allure.step("Ввод валидного пароля"):
        text_input = driver.find_element(By.ID, 'password')
        text_input.clear()
        text_input.send_keys('SuperSecretPassword!')

    with allure.step("Нажатие на кнопку для авторизации"):
        submit_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        submit_button.click()

    with allure.step("Вывод сообщения об успешной авторизации"):
        success_message = driver.find_element(By.CSS_SELECTOR, 'div.flash.success')
        assert "You logged into a secure area!" in success_message.text

@allure.epic("Авторизация на тестовом сайте")
@allure.title("Авторизация с невалидными данными")
@allure.description("Имитация действий пользователя с помощью Selenium")
def test_unsuccessful_login(driver):
    with allure.step("Открытие страницы авторизации тестового сайта"):
        driver.get("https://the-internet.herokuapp.com/login")

    with allure.step("Ввод невалидного логина"):
        text_input = driver.find_element(By.ID, 'username')
        text_input.clear()
        text_input.send_keys('username')

    with allure.step("Ввод невалидного пароля"):
        text_input = driver.find_element(By.ID, 'password')
        text_input.clear()
        text_input.send_keys('password')

    with allure.step("Нажатие на кнопку для авторизации"):
        submit_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        submit_button.click()

    with allure.step("Вывод сообщения о неуспешной авторизации"):
        unsuccess_message = driver.find_element(By.CSS_SELECTOR, 'div.flash.error')
        assert "Your username is invalid!" in unsuccess_message.text

