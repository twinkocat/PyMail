import pytest

from mailchimp_http import MailchimpWrongResponse, MailchimpNotFound


def test_get_ok(mailchimp):
    mailchimp.http_mock.get('https://us18.api.mailchimp.com/3.0/test/endpoint', json={'ok': True})
    assert mailchimp.http.get('test/endpoint') == {'ok': True}


@pytest.mark.parametrize(('code', 'exception'),
                         [(504, MailchimpWrongResponse),
                          (404, MailchimpNotFound)])
def test_get_wrong_status_code(mailchimp, code, exception):
    mailchimp.http_mock.get('https://us18.api.mailchimp.com/3.0/test/endpoint', json={'ok': True}, status_code=code)

    with pytest.raises(exception):
        mailchimp.http.get('test/endpoint')


def test_post_ok(mailchimp):
    mailchimp.http_mock.post('https://us18.api.mailchimp.com/3.0/test/endpoint', json={'ok': True})
    assert mailchimp.http.post('test/endpoint', payload=dict()) == {'ok': True}


@pytest.mark.parametrize(('code', 'exception'),
                         [(504, MailchimpWrongResponse),
                          (404, MailchimpNotFound)])
def test_post_wrong_status_code(mailchimp, code, exception):
    mailchimp.http_mock.post('https://us18.api.mailchimp.com/3.0/test/endpoint', json={'ok': True}, status_code=code)

    with pytest.raises(exception):
        mailchimp.http.post('test/endpoint', payload=dict())


def test_post_payload(mailchimp):
    def assertion(request, context):
        json = request.json()
        assert json['__mocked'] == 'test'

        return {'ok': True}

    mailchimp.http_mock.post('https://us18.api.mailchimp.com/3.0/test/endpoint', json=assertion)
    mailchimp.http.post('test/endpoint', payload={'__mocked': 'test'})


@pytest.mark.xfail(strict=True, reason='Just to check above test work')
def test_post_payload_fail(mailchimp):
    def assertion(request, context):
        json = request.json()
        assert json['__mocked'] == 'SHOULD BE NOT MOCKED'

        return {'ok': True}

    mailchimp.http_mock.post('https://us18.api.mailchimp.com/3.0/test/endpoint', json=assertion)
    mailchimp.http.post('test/endpoint', payload={'__mocked': 'test'})


def test_authenticator(mailchimp):
    def assertion(request, context):
        assert request.headers['Authorization'] == \
               'Basic dXNlcjo1ZWRjMjgxYmM1MDhmZTRkYTdjNTczMTIyMTcwNDhlNi11czE4'

        return {'ok': True}

    mailchimp.http_mock.get('https://us18.api.mailchimp.com/3.0/test/endpoint', json=assertion)
    assert mailchimp.http.get('test/endpoint') == {'ok': True}


@pytest.mark.xfail(strict=True, reason='Just to check above test work')
def test_authenticator_wrong(mailchimp):
    def assertion(request, context):
        assert request.headers['Authorization'] == 'UNKNOWN AUTHORIZATION'

        return {'ok': True}

    mailchimp.http_mock.get('https://us18.api.mailchimp.com/3.0/test/endpoint', json=assertion)
    assert mailchimp.http.get('test/endpoint') == {'ok': True}

