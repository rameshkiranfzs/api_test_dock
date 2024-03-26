from utilities import run_api ,log_setup
from utilities import data_operator as dop
from resources import paths
from common_files import constants_file as cons
import pytest
import test_data

logger = log_setup.getlogger()

@pytest.fixture
def get_token(get_config_details):
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
@pytest.mark.integration
def test_bookings_end_to_end(get_config_details,get_token):
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

