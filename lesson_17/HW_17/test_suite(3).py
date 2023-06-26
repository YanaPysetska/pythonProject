import allure
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest

@allure.title("Тестирование uitestingplayground.com")
@allure.description("test_text_input and test_LoadDelayext")
class TestUITAP:
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.wait = WebDriverWait(cls.driver, 10)
        cls.driver.get("http://uitestingplayground.com/home")

    def return_to_home(self):
        self.driver.get("http://uitestingplayground.com/home")

    def test_text_input(self):
        link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Text Input")))
        link.click()

        text = self.wait.until(EC.presence_of_element_located((By.ID, 'newButtonName')))
        text.send_keys('Test')
        time.sleep(2)

        button = self.wait.until(EC.element_to_be_clickable((By.ID, 'updatingButton')))
        button.click()
        time.sleep(2)

        updated_button = self.wait.until(EC.presence_of_element_located((By.ID, 'newButtonName')))
        button_name = updated_button.get_attribute("value")

        expected_button_name = 'Test'
        assert button_name == expected_button_name, f"Expected: {expected_button_name}, Actual: {button_name}"

        self.return_to_home()

    def test_LoadDelayext(self):
        load_delay_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Load Delay")))
        load_delay_link.click()

        button_here = WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".btn")))
        button_here.click()
        time.sleep(2)

        assert button_here.is_displayed(), "Кнопка не появилась"
        self.return_to_home()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

if __name__ == '__main__':
    import pytest
    pytest.main()
