import time

import pytest

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils

class Test_002_DDT_Login:
    baseUrl = ReadConfig.getApplicationURL()
    path = ".//TestData/LoginData.xlsx"
    logger = LogGen.loggen()
    stars = 10 * "*"

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info(f"{self.stars} Test_002_DDT_Login {self.stars}")
        self.logger.info(f"{self.stars} Verifying Login Test {self.stars}")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)
        self.rows = XLUtils.getRowCount(self.path, 'Hoja1')
        print("Number pf Rows i a Excel:", self.rows)
        lst_status = []

        for r in range(2, self.rows+1):
            self.user = XLUtils.readData(self.path, 'Hoja1', r,1)
            self.password = XLUtils.readData(self.path, 'Hoja1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Hoja1', r, 3)

            self.lp.setUsername(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)
            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"
            if act_title == exp_title:
                if self.exp == 'Pass':
                    self.logger.info(f"{self.stars} Passed {self.stars}")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp == 'Fail':
                    self.driver.save_screenshot(".\\ScreenShots\\" + "test_login.png")
                    self.logger.error(f"{self.stars} Failed {self.stars}")
                    lst_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == 'Pass':
                    self.logger.info(f"{self.stars} Failed {self.stars}")
                    lst_status.append("Fail")
                elif self.exp == 'Fail':
                    self.driver.save_screenshot(".\\ScreenShots\\" + "test_login.png")
                    self.logger.error(f"{self.stars} Passed {self.stars}")
                    lst_status.append("Pass")
        if "Fail" not in lst_status:
            self.logger.info(f"{self.stars} Login DDT test passed {self.stars}")
            self.driver.close()
            assert True
        else:
            self.logger.info(f"{self.stars} Login DDT test failed {self.stars}")
            self.driver.close()
            assert False

        self.logger.info(f"{self.stars} End of login DDT Test {self.stars}")
        self.logger.info(f"{self.stars} Complete TC_loginDDT_002 {self.stars}")

