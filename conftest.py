import pytest
from config import dev,prod,stage


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="dev", help="Specify the environment (dev, test, prod)")

@pytest.fixture
def get_config_details(request):
    env = request.config.getoption("--env")
    if env=='dev':
        yield dev.config
    elif env=='prod':
        yield prod.config
    elif env=='stage':
        yield stage.config
    else:
        return ValueError(f"Unknown environment - {env}")
    