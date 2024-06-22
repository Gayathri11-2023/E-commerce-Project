"""
In this project, we will simulate and automate a purchase scenario from an E-Commerce- Website with Selenium & Python.
"""
# own package
from Data import data1
from Locator import locator1
from Method import method
# common
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
# action chains
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

import random
# pytest
import pytest

class TestAddToCart:


        @pytest.fixture()
        def boot(self):
            """
            This method open the url and maximize window and close the browser
            :return:None
            """
            self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            self.driver.get(data1.WebData().url)
            self.driver.maximize_window()
            self.driver.implicitly_wait(8)
            self.wait=WebDriverWait(self.driver, 10)
            self.actions=ActionChains(self.driver)
            yield
            # using yield keyword this block of code execute after function block of code executed
            self.driver.quit()

        @pytest.mark.html
        def test_select_phone_and_add_to_cart(self,boot):
            """
            This method navigate to phone product page add iphone to shopping cart with specified quantities
            :param boot:
            :return:
            """

            try:
                # phone button
                method.WebMethods().clickButton(self.driver,locator1.WebLocator().phone_button_locator)
                # iphone button click
                method.WebMethods().clickButton(self.driver,locator1.WebLocator().iphone_locator)
                # first pic
                method.WebMethods().clickButton(self.driver,locator1.WebLocator().first_pic_locator)
                # loop for all photos
                for _ in range(0,5):
                    method.WebMethods().clickButton(self.driver,locator1.WebLocator().all_photo_left_button)
                    sleep(4)
                self.driver.save_screenshot('screenshot#' + str(random.randint(0, 10)) + '.png')
                sleep(2)
                # x button
                method.WebMethods().clickButton(self.driver,locator1.WebLocator().x_button_locator)
                # quantity
                quantity_button=self.wait.until(EC.presence_of_element_located((By.XPATH, locator1.WebLocator().quantity_locator)))
                sleep(3)
                quantity_button.click()
                quantity_button.clear()
                sleep(3)
                # enter quantity
                method.WebMethods().enterText(self.driver,locator1.WebLocator().quantity_locator,data1.WebData().quantity)
                # click add to cart button
                method.WebMethods().clickButton(self.driver,locator1.WebLocator().add_to_cart_button)
                # print success message from webpage
                print(self.wait.until(EC.presence_of_element_located((By.XPATH, locator1.WebLocator().success_message_phone_locator))).text)
                sleep(2)
                method.WebMethods().clickButton(self.driver,locator1.WebLocator().cart_button)
                cart_text = self.wait.until(EC.presence_of_element_located((By.XPATH, locator1.WebLocator().cart_right_text_button)))
                assert cart_text.text == "x2"
            except NoSuchElementException as e:
                print("Error:Element is not present in the webpage")

        @pytest.mark.html
        def test_search_laptop_and_add_to_cart(self,boot):
            """
            This method navigate to laptop product page add laptop to shopping cart with expected delivery date
            :param boot:
            """
            try:
                # move to laptop page using action chains
                source=self.wait.until(EC.element_to_be_clickable((By.XPATH, locator1.WebLocator().laptop_locator)))
                self.actions.move_to_element(source).perform()
                # all laptop
                method.WebMethods().clickButton(self.driver,locator1.WebLocator().all_laptop_locator)
                # specific model
                method.WebMethods().clickButton(self.driver,locator1.WebLocator().specific_model_locator)
                sleep(2)
                # loop using for scroll down page to show add to cart button
                for _ in range(0,5):
                    self.actions.send_keys(Keys.DOWN).perform()
                sleep(3)
                # click calender
                method.WebMethods().clickButton(self.driver,locator1.WebLocator().calendar_locator)
                month_text=self.wait.until(EC.presence_of_element_located((By.XPATH, locator1.WebLocator().month_year_locator)))
                while month_text.text !="April 2012":
                    method.WebMethods().clickButton(self.driver,locator1.WebLocator().backward_button_locator)
                    sleep(1)
                # specific date
                method.WebMethods().clickButton(self.driver,locator1.WebLocator().date_locator)
                # click add to a cart button
                method.WebMethods().clickButton(self.driver,locator1.WebLocator().add_to_cart_button)# click add to a cart button
                method.WebMethods().clickButton(self.driver,locator1.WebLocator().add_to_cart_button)
                sleep(3)
                # success message from webpage
                print(self.wait.until(EC.presence_of_element_located((By.XPATH, locator1.WebLocator().success_message_phone_locator))).text)
                sleep(2)
                # click cart image
                method.WebMethods().clickButton(self.driver, locator1.WebLocator().cart_button)
                cart_text = self.wait.until(EC.presence_of_element_located((By.XPATH, locator1.WebLocator().cart_right_text_button)))
                assert cart_text.text == "x1"

            except NoSuchElementException as e:
                print("Error: Element is not present in the webpage")