import pytest
import time

from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random

class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger
    stars = 10 * "*"

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_addCustomer(self, setup):
        self.logger.info(f"{self.stars} Test_003_AddCustomer {self.stars}")
        self.driver= setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info(f"{self.stars} Login succesful {self.stars}")

        self.logger.info(f"{self.stars} Starting Add Customer Test {self.stars}")

        self.addcust = AddCustomer(self.driver)
        time.sleep(5)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()

        self.addcust.clickOnAddnew()

        self.logger.info(f"{self.stars} Providing customer info {self.stars}")

        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setCustomerRoles("Guests")
        self.addcust.setManagerOfVendor("Vendor 2")
        self.addcust.setGender("Male")
        self.addcust.setFirstName("Cris")
        self.addcust.setLastName("Arevalo")
        self.addcust.setDob("7/05/1992")  # Format: D / MM / YYY
        self.addcust.setCompanyName("busyQA")
        self.addcust.setAdminContent("This is for testing.........")
        self.addcust.clickOnSave()

        self.logger.info(f"{self.stars} Saving customer info {self.stars}")

        self.logger.info(f"{self.stars} Add customer validation started {self.stars}")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text

        print(self.msg)
        if 'The new customer has been added successfully.' in self.msg:
            assert True
            self.logger.info(f"{self.stars} Add customer Test Passed {self.stars}")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            self.logger.error(f"{self.stars} Add customer Test Failed {self.stars}")
            assert False

        self.driver.close()
        self.logger.info(f"{self.stars} Ending Add customer test {self.stars}")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))