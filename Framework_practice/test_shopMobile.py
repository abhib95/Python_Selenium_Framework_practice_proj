import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Page_objects.Checkoutpage import CheckoutPage
from Page_objects.Landingpage import LandingPage
from Page_objects.Shoppingpage import ShoppingPage
from Utilities.Baseclass import Baseclass


class TestTwo(Baseclass):
    def test_shopMobile(self):
        log = self.getLogger()
        
        land = LandingPage(self.driver)
        land.ShopButtonClick().click()
        shop = ShoppingPage(self.driver)
        products = shop.all_products()

        i = -1
        for product in products:
            i = i + 1
            prod_name = product.text
            if prod_name == 'Nokia Edge':
                log.info(prod_name)
                reqd_prod = product.text
                shop.getCardFooter()[i].click()


    
        shop.getCheckOutButton().click()
        checkout = CheckoutPage(self.driver)
        checkout_prod = checkout.get_checkout_product_name().text
        assert reqd_prod == checkout_prod
        checkout.get_input_quantity().clear()
        checkout.get_input_quantity().send_keys('2')
        time.sleep(2)
        checkout.get_final_check_button().click()
        checkout.get_country().send_keys('ind')
        self.explicit_wait(7, checkout.locator_for_wait)
        checkout.get_wait_locator().click()
        checkout.get_check_box_click().click()
        checkout.get_purchase_button().click()
        checkout.get_success_message().is_displayed()
        time.sleep(2)








