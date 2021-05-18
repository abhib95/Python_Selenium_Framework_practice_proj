from selenium.webdriver.common.by import By


class LandingPage:
    def __init__(self, driver):
        self.driver = driver

    shop_button  = (By.XPATH, '//a[@href="/angularpractice/shop"]')

    def ShopButtonClick(self):
        return self.driver.find_element(*LandingPage.shop_button)