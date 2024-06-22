"""
The goal is to buy different electronic devices, select the delivery date and complete the checkout process.
"""


# own package
from Data import data2
from Locator import locator2
from Locator import locator1
from Method import method
# common
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium .webdriver.common.keys import Keys
# Exception
from selenium.common.exceptions import NoSuchElementException
# sleep
from time import sleep
# Explicit Wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# select
from selenium.webdriver.support.select import Select
# pytest
import pytest

class Test_checkout_page:

    @pytest.fixture()
    def boot(self):
        """
        This method open the url and maximize window and close the browser
        :return:None
        """
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(data2.WebData().url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)
        self.wait = WebDriverWait(self.driver, 10)
        self.actions = ActionChains(self.driver)
        yield
        # using yield keyword this block of code execute after function block of code executed
        self.driver.quit()

    @pytest.fixture()
    def setup(self,boot):
        """
        this method select laptop product and add the product to cart
        :param boot:
        :return:
        """
        try:
            # move to laptop page using action chains
            source = self.wait.until(EC.element_to_be_clickable((By.XPATH, locator1.WebLocator().laptop_locator)))
            self.actions.move_to_element(source).perform()
            # all laptop
            method.WebMethods().clickButton(self.driver, locator1.WebLocator().all_laptop_locator)
            # specific model
            method.WebMethods().clickButton(self.driver, locator1.WebLocator().specific_model_locator)
            sleep(2)
            # loop using for scroll down page to show add to cart button
            for _ in range(0, 5):
                self.actions.send_keys(Keys.DOWN).perform()
            sleep(3)
            # click add to a cart button
            method.WebMethods().clickButton(self.driver, locator1.WebLocator().add_to_cart_button)
        except NoSuchElementException as e:
            print("Error")

    @pytest.mark.html
    def test_check_out_page(self,boot,setup):
        """
        this method check order placed correctly or not
        :param boot:
        :param setup:
        """
        try:
            # click add to cart image and checkout box
            method.WebMethods().clickButton(self.driver, locator2.WebLocator().add_to_cart_image)
            method.WebMethods().clickButton(self.driver, locator2.WebLocator().checkout_button_locator)
            # select Radio button
            method.WebMethods().clickButton(self.driver,locator2.WebLocator().radio_button_locator)
            # click continue button
            method.WebMethods().clickButton(self.driver,locator2.WebLocator().continue_locator)
            # loop using for scroll down page to show add to cart button
            sleep(2)
            for _ in range(0, 3):
                self.actions.send_keys(Keys.DOWN).perform()
            sleep(4)
            # first Name
            method.WebMethods().enterText(self.driver,locator2.WebLocator().first_name_locator, data2.WebData().first_Name)
            # last Name
            method.WebMethods().enterText(self.driver,locator2.WebLocator().last_name_locator,data2.WebData().last_name)
            # Email
            method.WebMethods().enterText(self.driver,locator2.WebLocator().mail_locator,data2.WebData().email)
            # telephone
            method.WebMethods().enterText(self.driver,locator2.WebLocator().phone_no_locator,data2.WebData().phone_no)
            # address
            method.WebMethods().enterText(self.driver,locator2.WebLocator().address_locator,data2.WebData().address)
            # city
            method.WebMethods().enterText(self.driver,locator2.WebLocator().city_locator,data2.WebData().city)
            # post code
            method.WebMethods().enterText(self.driver,locator2.WebLocator().post_code_locator,data2.WebData().post_code)
            # drop down
            sleep(5)
            country=self.wait.until(EC.element_to_be_clickable((By.XPATH, locator2.WebLocator().state_locator)))
            dropdown=Select(country)
            dropdown.select_by_visible_text("Angus")
            # click continue button
            method.WebMethods().clickButton(self.driver,locator2.WebLocator().continue_input_locator)
            sleep(4)
            # continue2 locator
            method.WebMethods().clickButton(self.driver,locator2.WebLocator().continue2_locator)
            # click terms $ condition
            method.WebMethods().clickButton(self.driver,locator2.WebLocator().terms_condition_locator)
            # continue3 locator
            method.WebMethods().clickButton(self.driver,locator2.WebLocator().continue3_locator)
            # final price
            final_price= self.wait.until(EC.presence_of_element_located((By.XPATH, locator2.WebLocator().final_price_locator)))
            sleep(2)
            print("final price of product:",final_price.text)
            # confirm order locator
            method.WebMethods().clickButton(self.driver,locator2.WebLocator().confirm_locator)
            # print success from webpage
            print(self.wait.until(EC.presence_of_element_located((By.XPATH,locator2.WebLocator().success_message_locator))).text)
            sleep(5)
            assert self.driver.current_url == "https://tutorialsninja.com/demo/index.php?route=checkout/success"
            sleep(6)



        except NoSuchElementException as e:
            print("Error:Element is not present in the webpage")

