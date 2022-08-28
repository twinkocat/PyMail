

def test_mailchimp_client_base_url(mailchimp):
    assert mailchimp.http.base_url == f'https://us18.api.mailchimp.com/3.0/'


def test_mailchimp_client_format_url(mailchimp):
    assert mailchimp.http.format_url('133') == f'https://us18.api.mailchimp.com/3.0/133'

