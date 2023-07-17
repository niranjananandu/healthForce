from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Calculate:
    input = "//input[@placeholder='Enter an integer']"
    calculate_button = "//button[text()='Calculate!']"
    result_text = "//p[@id='resultDiv']"

    def __init__(self, driver):
        self.driver = driver

    def calculateFactorial(self, userinput):
        self.driver.find_element(By.XPATH, self.input).clear()
        self.driver.find_element(By.XPATH, self.input).send_keys(userinput)
        self.driver.find_element(By.XPATH, self.calculate_button).click()

    def calculate(self,userinput):
        factorial = 1
        for i in range(1,userinput+1):
            factorial = factorial * i

        return factorial





    def getValidationmessage(self):
        message = self.driver.find_element(By.XPATH, self.result_text).text
        return message

