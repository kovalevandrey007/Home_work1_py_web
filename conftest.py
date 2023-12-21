import pytest
import yaml
from check_post import add_post, get_login

with open('config.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)

@pytest.fixture()
def token():
    return get_login()





