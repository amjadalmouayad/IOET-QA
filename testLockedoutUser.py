import import_data
import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec
import unittest

driver = None
wait = None


def setup_module(module):
    if import_data.num_test != 0:
        print("\nName of the test case: " + str(import_data.arrListTest[0][0]))
        path = './geckodriver'
        global driver
        driver = Firefox(executable_path=path)
        driver.delete_all_cookies()
        global wait
        driver.implicitly_wait(10)
        wait = WebDriverWait(driver, 10)
        # Import data of the test case
        print("\nNumber of test cases: " + str(import_data.num_test))
        import_data.update_input_file()

    else:
        pytest.exit("\nAn unexpected number of test case,s Please insert the input data for the test case in "
                    "input.xlsx\n For more information please open Readme file")


def teardown_module(module):
    driver.quit()
    import_data.update_output_file()


def test_open_url():
    print("\nURL: " + import_data.arrListTest[0][1])
    driver.get(import_data.arrListTest[0][1])
    assert "Swag Labs" in driver.title


def test_insert_username_button_next():
    try:
        # | INSERT USERNAME |
        print("\nusername is: " + import_data.arrListTest[0][2])
        driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys(import_data.arrListTest[0][2])
    except NoSuchElementException:
        pytest.exit("\nTest fail: Not found element: username / next  ")


def test_insert_password():
    try:
        # | insert password |
        print("\nPassword is: " + import_data.arrListTest[0][3])
        driver.find_element(By.CSS_SELECTOR, "*[data-test=\"password\"]").send_keys(import_data.arrListTest[0][3])
    except NoSuchElementException:
        pytest.exit("\nTest fail: Not found element: password")


def test_submit_button():
    try:
        # | click Login |
        driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
        print("\n login successfully")
    except NoSuchElementException:
        pytest.exit("\nTest fail: Not found element: Button Login")


def test_products_page():
    elem = driver.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/div[1]/div/form/div[3]/h3").text
    assert "Epic sadface: Sorry, this user has been locked out." == elem
