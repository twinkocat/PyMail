import pytest
import requests_mock
from mailchimp_client import AppMailchimp


@pytest.fixture
def set_chimp_credentials(settings):
    settings.MAILCHIMP_API_KEY = 'key-us18'


@pytest.fixture
def mailchimp():
    client = AppMailchimp()

    with requests_mock.Mocker() as http_mock:
        client.http_mock = http_mock
        yield client
