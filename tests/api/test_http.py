import pytest
import requests


@pytest.mark.http
def test_first_request():
    r = requests.get('https://api.github.com/zen')
    print((f"Response is {r.text}").encode("utf-8"))


@pytest.mark.http
def test_second_request():
    r = requests.get('https://api.github.com/users/defunkt')
    body = r.json()
    headers = r.headers 
    #print((f"Response is {r.text}").encode("utf-8"))
    assert body['name'] == 'Chris Wanstrath'
    #print((f"Response Body is {r.json()}").encode("utf-8"))
    assert r.status_code == 200
    #print((f"Response Status is {r.status_code}").encode("utf-8"))
    assert headers['Server'] == 'GitHub.com'
    #print((f"Response Headers is {r.headers}").encode("utf-8"))

@pytest.mark.http
def test_status_code_request():
    r = requests.get('https://api.github.com/users/sergii_butenko')
    assert r.status_code == 404
