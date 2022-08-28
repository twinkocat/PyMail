from urllib.parse import urljoin

import requests
from typing import Optional
from requests.auth import HTTPBasicAuth

import settings


class MailchimpHTTPException(BaseException):
    pass


class MailchimpWrongResponse(MailchimpHTTPException):
    pass


class MailchimpNotFound(MailchimpHTTPException):
    pass


class MailChimpHttp:
    @property
    def base_url(self) -> str:
        dc = settings.MAILCHIMP_API_KEY.split('-')[-1]
        return f'https://{dc}.api.mailchimp.com/3.0/'

    def format_url(self, url: str) -> str:
        return urljoin(self.base_url, url.strip('/'))

    def request(self, url: str, method, payload: Optional[dict] = None):
        requests_payload = dict()
        if payload is not None:
            requests_payload['json'] = payload

        response = requests.request(
            method=method,
            url=self.format_url(url),
            auth=HTTPBasicAuth('user', settings.MAILCHIMP_API_KEY),
            **requests_payload,
        )
        if response.status_code == 404:
            raise MailchimpNotFound()

        if response.status_code != 200:
            raise MailchimpWrongResponse()
        return response

    def get(self, url: str):
        response = self.request(url, method='GET')
        return response.json()

    def post(self, url: str, payload: dict):
        response = self.request(url, method='POST', payload=payload)
        return response.json()
