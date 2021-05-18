from selenium.webdriver.common.by import By


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    check_prod_name = (By.XPATH, '//div[@class="media-body"]/h4/a')
    input_quantity = (By.ID, 'exampleInputEmail1')
    final_check_button = (By.CSS_SELECTOR, 'button[class*="btn-success"]')
    country = (By.ID, 'country')
    locator_for_wait = (By.LINK_TEXT, 'India')
    check_box = (By.CSS_SELECTOR, "div[class*='checkbox-primary']")
    purchase = (By.XPATH, '//input[@value="Purchase"]')
    succ_message = (By.CSS_SELECTOR, "div[class*='alert-dismissible']")

    def get_checkout_product_name(self):
        return self.driver.find_element(*CheckoutPage.check_prod_name)

    def get_input_quantity(self):
        return self.driver.find_element(*CheckoutPage.input_quantity)

    def get_final_check_button(self):
        return self.driver.find_element(*CheckoutPage.final_check_button)

    def get_country(self):
        return self.driver.find_element(*CheckoutPage.country)

    def get_wait_locator(self):
        return self.driver.find_element(*CheckoutPage.locator_for_wait)

    def get_check_box_click(self):
        return self.driver.find_element(*CheckoutPage.check_box)

    def get_purchase_button(self):
        return self.driver.find_element(*CheckoutPage.purchase)

    def get_success_message(self):
        return self.driver.find_element(*CheckoutPage.succ_message)

    # self.driver.find_element_by_css_selector("div[class*='checkbox-primary']").click()
    # self.driver.find_element_by_xpath('//input[@value="Purchase"]').click()
    # self.driver.find_element_by_css_selector("div[class*='alert-dismissible']").is_displayed()