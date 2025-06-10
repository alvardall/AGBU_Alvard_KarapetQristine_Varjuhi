import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
import Teastdata.config as config
from Pages.home import Searche

def test_valid_data(test_driver, test_logger):

    searche_obj = Searche(test_driver, test_logger)
    searche_obj.go_to_page(config.url)
    searche_obj.search_item()

    result_count = searche_obj.get_reported_result_count() 
    test_logger.info(f"RESULT COUNT: {result_count}")

    visible_count = searche_obj.get_visible_product_count()

    assert visible_count == result_count, f"Visible items ({visible_count}) don't match reported count ({result_count})"

    brands = searche_obj.get_all_product_brands()
    for b in brands:
        assert config.brand.lower() in b.lower(), f"Unexpected brand: {b}"

    prices = searche_obj.get_all_product_prices()
    for p in prices:
        assert p <= 200.0, f"Price out of range: {p}"

    test_logger.info(f"All test is finished")







    # home_obj.find_and_click(home_obj.btn_register_home)

    # # register user
    # register_obj = Register(test_driver, test_logger)
    # user_name, password = register_obj.register_user()
    # assert register_obj.find_elem_ui(home_obj.btn_login_home), test_logger.error("Login element is not displayed.")
    # test_logger.info("User is registered successfully.")

    # # login with registereed data
    # login_obj = Login(test_driver, test_logger)
    # home_obj.find_and_click(home_obj.btn_login_home)
    # login_obj.login(user_name, password)
    # assert home_obj.find_elem_ui(home_obj.btn_logout_home), test_logger.error("Login elementr is not displayed")
    # test_logger.info("User is logged in successfully.")