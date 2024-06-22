from selenium.webdriver.common.by import By
# Explicit Wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WebMethods:
    """
    This class is used to contain all the methods that are required to perform the testing for the orange HRM login page
    """

    def enterText(self, driver, locator, textValue):
        """
        This method find the element in web page and send text to input field
        :param driver:
        :param locator:
        :param textValue:
        """
        self.wait = WebDriverWait(driver, 10)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locator))).send_keys(textValue)

    def clickButton(self, driver, locator):
        """
        This Method find the element  in web page and click the button
        :param driver:
        :param locator:
        """
        self.wait = WebDriverWait(driver, 10)
        self.wait.until(EC.presence_of_element_located((By.XPATH, locator))).click()
