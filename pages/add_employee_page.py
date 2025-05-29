from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddEmployeePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)  # ⬅ Increased to 30 seconds

    def add_employee(self, first_name, middle_name, last_name):
        # Wait for each input field to be visible and then interact
        first_name_field = self.wait.until(
            EC.visibility_of_element_located((By.NAME, "firstName"))
        )
        middle_name_field = self.wait.until(
            EC.visibility_of_element_located((By.NAME, "middleName"))
        )
        last_name_field = self.wait.until(
            EC.visibility_of_element_located((By.NAME, "lastName"))
        )

        # Send input values
        first_name_field.send_keys(first_name)
        middle_name_field.send_keys(middle_name)
        last_name_field.send_keys(last_name)

        # Wait for Save button to be clickable and click
        save_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        )
        save_button.click()
