import pytest
from selenium.webdriver.support.select import Select

from Page_objects.Formpage import Formpage
from Utilities.Baseclass import Baseclass


class Testone(Baseclass):

    def test_formsubmission(self, getData):
        log = self.getLogger()

        form = Formpage(self.driver)
        form.formPage().send_keys(getData["Firstname"])
        log.info('Entering Firstname')
        form.emailPage().send_keys(getData["Email"])
        log.info('Entering Email')
        form.checkbox_Click().click()

        # to operate dropdown

        self.dropdown_button(form.drop_option(), getData["Gender"])
        form.button_success().click()
        Success_text = form.success_message().text
        log.info(Success_text)

        assert 'Success' in Success_text

        self.driver.refresh()

    @pytest.fixture(params=[{"Firstname":"Abhishek","Email":"Bhaskar", "Gender":"Male"},
                            {"Firstname":"Abhs","Email":"Boss","Gender": "Female"}])
    def getData(self, request):
        return request.param






