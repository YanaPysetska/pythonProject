import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import time
class TestCustomerCreation(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.wait = WebDriverWait(cls.driver, 10)
        cls.driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager/addCust")

    def test_customer_creation(self):
        f_name = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[ng-model="fName"]')))
        l_name = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[ng-model="lName"]')))
        p_code = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[ng-model="postCd"]')))

        f_name.send_keys('Test')
        l_name.send_keys("TestL1")
        p_code.send_keys("36000")

        button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]')))
        button.click()

        alert = Alert(self.driver)
        alert_text = alert.text

        expected_alert_text = "Customer added successfully with customer id :6"
        self.assertEqual(alert_text, expected_alert_text, f"Expected: {expected_alert_text}, Actual: {alert_text}")

        alert.accept()

    def test_customer_search(self):
        customers_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@ng-click="showCust()"]')))
        customers_button.click()

        search_input = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[ng-model="searchCustomer"]')))
        search_input.clear()
        search_input.send_keys("Test")
        time.sleep(2)

        delete_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@ng-click, "deleteCust")]')))
        delete_button.click()
        time.sleep(2)

        record_locator = (By.XPATH, '//table[@class="table table-bordered table-striped"]//td[contains(text(), "Test")]')
        self.wait.until(EC.invisibility_of_element_located(record_locator))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
