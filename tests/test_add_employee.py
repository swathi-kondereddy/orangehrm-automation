import time
from pages.login_page import LoginPage
from pages.pim_page import PIMPage

def test_add_employee(setup):
    driver = setup

    login_page = LoginPage(driver)
    login_page.login("Admin", "admin123")

    time.sleep(2)  # ⬅️ Let the UI fully load before clicking PIM

    pim_page = PIMPage(driver)
    pim_page.go_to_add_employee()

    # Continue with rest of the test...
