import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest

@allure.title("Тестирование the-internet.herokuapp.com")
@allure.description("test_AB_Testing and test_Add_Remove_Elements")
class TestWebsite:
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.wait = WebDriverWait(cls.driver, 10)
        cls.driver.get("http://the-internet.herokuapp.com/")

    def test_AB_Testing(self):
        AB_Testing = self.driver.find_elements(By.XPATH, '//*[@id="content"]/ul/li[1]/a')
        index_to_click = 0
        AB_Testing[index_to_click].click()
        time.sleep(2)

        current_url = self.driver.current_url
        expected_url = "http://the-internet.herokuapp.com/abtest"
        assert current_url == expected_url, f"Expected URL: {expected_url}, Actual URL: {current_url}"

    def test_Add_Remove_Elements(self):
        self.driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
        add_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="content"]/div/button')))
        add_button.click()

        delete_button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".added-manually")))
        delete_button.click()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

if __name__ == '__main__':
    import pytest
    pytest.main()
