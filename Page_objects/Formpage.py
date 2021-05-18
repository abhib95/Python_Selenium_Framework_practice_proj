from selenium.webdriver.common.by import By


class Formpage:

    def __init__(self, driver):
        self.driver = driver

    name = (By.NAME, 'name')
    email = (By.NAME, 'email')
    checkbox = (By.XPATH, "//input[@class='form-check-input']")
    drop = (By.XPATH, '//select[@id="exampleFormControlSelect1"]')
    success_button = (By.XPATH, '//input[@class="btn btn-success"]')
    message_success = (By.CSS_SELECTOR, 'div[class = "alert alert-success alert-dismissible"]')

    def formPage(self):
        return self.driver.find_element(*Formpage.name)

    def emailPage(self):
        return self.driver.find_element(*Formpage.email)

    def checkbox_Click(self):
        return self.driver.find_element(*Formpage.checkbox)

    def drop_option(self):
        return self.driver.find_element(*Formpage.drop)

    def button_success(self):
        return self.driver.find_element(*Formpage.success_button)

    def success_message(self):
        return self.driver.find_element(*Formpage.message_success)

    #self.driver.find_element_by_css_selector('div[class = "alert alert-success alert-dismissible"]')
    #self.driver.find_element_by_xpath('//input[@class="btn btn-success"]')
    # self.driver.find_element_by_xpath('//select[@id="exampleFormControlSelect1"]')
    #driver.find_element_by_name('name').send_keys('Abhishek')
    #driver.find_element_by_name('email')
    #driver.find_element_by_xpath("//input[@class='form-check-input']")