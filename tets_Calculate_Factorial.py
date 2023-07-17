from selenium import webdriver
import Factorial
import time

class TestFactorial:

    def test_calculate_invalid(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://192.168.3.96:6464/")
        self.driver.maximize_window()
        self.factorial = Factorial.Calculate(self.driver)
        self.factorial.calculateFactorial("a")
        message = self.factorial.getValidationmessage()
        assert message == "Please enter an integer"
        print(message)
        time.sleep(5)

    def test_calculate_valid(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://192.168.3.96:6464/")
        self.driver.maximize_window()
        self.factorial = Factorial.Calculate(self.driver)
        self.factorial.calculateFactorial(7)
        result = self.factorial.calculate(7)
        message = self.factorial.getValidationmessage()
        assert message == f"The factorial of 7 is: {result}",result
        print(message)
        time.sleep(5)
