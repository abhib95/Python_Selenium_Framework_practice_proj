from selenium.webdriver.common.by import By


class ShoppingPage:

    def __init__(self, driver):
        self.driver = driver

    mobiles = (By.CSS_SELECTOR, ".card-title a")
    card_footer = (By.CSS_SELECTOR, ".card-footer button")
    Checkout_btn = (By.CSS_SELECTOR, "a[class='nav-link btn btn-primary']")

    def all_products(self):
        return self.driver.find_elements(*ShoppingPage.mobiles)

    def getCardFooter(self):
        return self.driver.find_elements(*ShoppingPage.card_footer)

    def getCheckOutButton(self):
        return self.driver.find_element(*ShoppingPage.Checkout_btn)

    # product.find_element_by_xpath("div/h4/a")
    # driver.find_element_by_css_selector(".card-footer button")
    # self.driver.find_element_by_css_selector("a[class='nav-link btn btn-primary']")