from pages.login_page import LoginPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_valid(setup):
    driver = setup
    login = LoginPage(driver)
    login.login("Admin", "admin123")

    # Wait for URL to contain "dashboard"
    WebDriverWait(driver, 10).until(EC.url_contains("dashboard"))
    assert "dashboard" in driver.current_url.lower()
