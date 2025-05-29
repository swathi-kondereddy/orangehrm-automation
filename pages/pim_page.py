from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PIMPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def go_to_add_employee(self):
        pim_menu = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='PIM']")))
        pim_menu.click()

        add_employee_menu = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Add Employee")))
        add_employee_menu.click()

    def add_employee(self, first_name, middle_name, last_name):
        self.wait.until(EC.visibility_of_element_located((By.NAME, "firstName"))).send_keys(first_name)
        self.driver.find_element(By.NAME, "middleName").send_keys(middle_name)
        self.driver.find_element(By.NAME, "lastName").send_keys(last_name)
        self.driver.find_element(By.XPATH, "//button[text()=' Save ']").click()
