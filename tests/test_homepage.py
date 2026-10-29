
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class HomePage:

    SEARCH_BOX = (By.NAME, "q")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def open_homepage(self):
        self.driver.get("https://www.flipkart.com/")

    def get_page_title(self):
        self.wait.until(lambda browser: browser.title != "")
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url

    def search_product(self, product_name):
        search_box = self.wait.until(
            EC.visibility_of_element_located(self.SEARCH_BOX)
        )
        search_box.clear()
        search_box.send_keys(product_name)
        search_box.send_keys(Keys.ENTER)

    def wait_for_search_results(self):
        self.wait.until(
            lambda browser: "/search" in browser.current_url.lower()
        )
