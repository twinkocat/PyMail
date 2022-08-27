import pytest

import settings
from client import AppMailchimp


app = AppMailchimp()


def test_app_mailchimp():
    dc = settings.MAILCHIMP_API_KEY.split('-')[-1]
    assert app.base_url == f'https://{dc}.api.mailchimp.com/3.0/'
    assert app.format_url('133') == f'https://{dc}.api.mailchimp.com/3.0/133'


def test_get_ok(client):
    pass


def test_get_fail():
    pass


def test_post_ok():
    pass


def test_post_fail():
    pass
