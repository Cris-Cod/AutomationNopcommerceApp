from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseUrl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()
    stars = 10 * "*"

    def test_homePageTitle(self, setup):
        self.logger.info(f"{self.stars} Test_001_Login {self.stars}")
        self.logger.info(f"{self.stars} Verifying Home Page Title {self.stars}")
        self.driver = setup
        self.driver.get(self.baseUrl)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info(f"{self.stars} Home page title test is passed {self.stars}")
        else:
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.info(f"{self.stars} Home page title test is failed {self.stars}")
            assert False

    def test_login(self, setup):
        self.logger.info(f"{self.stars} Verifying Login Test {self.stars}")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.implicitly_wait(5)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        print(act_title)
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info(f"{self.stars} Login test is passed {self.stars}")
        else:
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_login.png")
            self.driver.close()
            self.logger.error(f"{self.stars} Login test is failed {self.stars}")
            assert False
        self.lp.clickLogout()
        self.logger.info(f"{self.stars} Login test is passed {self.stars}")