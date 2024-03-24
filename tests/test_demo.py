from resources import paths
from utilities import run_api
import pytest

@pytest.mark.filterwarnings("ignore::requests.packages.urllib3.exceptions.InsecureRequestWarning")
def test_health_check_api(get_config_details):
    url = get_config_details['hosturl']
    path = paths.health_check_of_api
    url = url+path
    payload= ""
    headers = ""
    status_code, response_body, response_headers = run_api.run_api(url,payload,headers, request_type="GET")
    assert status_code==201
