from utilities import run_api ,log_setup
from utilities import data_operator as dop
from resources import paths
from common_files import constants_file as cons
import pytest
import test_data
import pandas as pd

logger = log_setup.getlogger()

@pytest.fixture
def get_token(get_config_details):
    logger.info("--------------------------------Executing API - get_token---------------------------------------")
    db_dict = get_config_details
    hosturl = db_dict["hosturl"]
    # Test - get Token API 
    path = paths.get_token
    url = hosturl+path
    username = cons.username
    password = cons.password
    request_key_value = {}
    request_key_value["username"] = username
    request_key_value["password"] = password
    payload = dop.extract_file_json(cons.request_file_path+'get_token.json')
    payload = run_api.create_payload(payload,request_key_value)
    logger.info(payload)
    status_code, response_body, response_headers = run_api.run_api(url=url, headers="",payload=payload,request_type='POST')

    token = dop.get_value_from_json(response_body,"token")
    return token


@pytest.mark.filterwarnings("ignore::requests.packages.urllib3.exceptions.InsecureRequestWarning")
@pytest.mark.unitlevel
def test_ping_api(get_config_details,get_token):
    logger.info("--------------------------------Executing API - test_ping_api---------------------------------------")

    token = get_token
    logger.info(token)
    print(token)
    db_dict = get_config_details
    hosturl = db_dict["hosturl"]

    # Test -Ping API
    path = paths.health_check_of_api
    url = hosturl+path
    status_code, response_body, response_headers = run_api.run_api(url=url, headers="",payload="",request_type='GET')
    assert str(status_code)=="201"


@pytest.mark.createbooking
def test_post_create_booking(get_config_details,get_token):
    logger.info("--------------------------------Executing API - test_post_create_booking---------------------------------------")

    db_dict = get_config_details
    hosturl = db_dict["hosturl"]
    path = paths.post_create_booking
    url = hosturl+path
    payload = dop.extract_file_json(cons.request_file_path+'post_create_booking.json')
    request_key_value = {}
    request_key_value['firstname'] = dop.random_name_generator(6)
    request_key_value['lastname'] = dop.random_name_generator(4)
    request_key_value['totalprice'] = dop.generate_random_integer(1,100)
    request_key_value['depositpaid'] = "true"
    past_date = dop.get_past_date(30)
    future_date = dop.get_future_date(30)
    request_key_value['checkin'] = past_date
    request_key_value['checkout'] = future_date
    input_df = pd.read_csv(cons.input_csv+"api_data.csv")
    conditon = (input_df['APIName']=='post_create_booking') & (input_df['fieldname']=='additionalneeds')
    request_key_value['additionalneeds'] = input_df.loc[conditon,'fieldvalue'].iloc[0]

    payload = run_api.create_payload(payload,request_key_value)
    status_code, response_body, response_headers = run_api.run_api(url=url, headers="",payload=payload,request_type='POST')
    assert dop.get_value_from_json(response_body,'firstname') == request_key_value['firstname']
    assert dop.get_value_from_json(response_body,'lastname') == request_key_value['lastname']
    assert dop.get_value_from_json(response_body,'totalprice') == request_key_value['totalprice']
    assert dop.get_value_from_json(response_body,'depositpaid') == request_key_value['depositpaid']
    assert dop.get_value_from_json(response_body,'checkin') == request_key_value['checkin']
    assert dop.get_value_from_json(response_body,'checkout') == request_key_value['checkout']
    assert dop.get_value_from_json(response_body,'firstname') == request_key_value['firstname']
    assert dop.get_value_from_json(response_body,'additionalneeds') == request_key_value['additionalneeds']
    assert status_code == 201
    # assert response_body[]

@pytest.mark.unitlevel
def test_get_all_bookings(get_config_details,get_token):

    db_dict = get_config_details
    hosturl = db_dict["hosturl"]
    path = paths.get_all_bookings
    url = hosturl+path
    status_code, response_body, response_headers = run_api.run_api(url=url, headers="",payload="",request_type='GET')
    value = dop.is_value_present_json(response_body,55)
    assert str(status_code)=="201"
