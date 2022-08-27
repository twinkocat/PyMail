from urllib.parse import urljoin

import settings
from http import MailChimpHttp


class AppMailchimp:
    def __init__(self):
        self.http = MailChimpHttp()

    @property
    def base_url(self) -> str:
        dc = settings.MAILCHIMP_API_KEY.split('-')[-1]
        return f'https://{dc}.api.mailchimp.com/3.0/'

    def format_url(self, url: str) -> str:
        return urljoin(self.base_url, url.strip('/'))


a = AppMailchimp()
print(a.format_url('1111'))
