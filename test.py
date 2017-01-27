import pytest
from mock import patch

from my_package.myfirstmodule.maps import maps, Send
from my_package.mysecondmodule.utils import connection_to


# Basic test

def test_maps_object():
    assert connection_to in maps


# Mocking

@patch('my_package.myfirstmodule.maps.requests.get')
def test_get_request_called_once(mock_get):
    send = Send()
    send.ping()
    mock_get.assert_called_once_with('http://google.com')

@patch('my_package.myfirstmodule.maps.requests.get')
def test_get_request_not_200(mock_get):
    send = Send()
    mock_get.return_value.status_code = 'not 200'
    assert send.ping() == 'failure'

@patch('my_package.myfirstmodule.maps.requests.get')
def test_get_request_200(mock_get):
    send = Send()
    mock_get.return_value.status_code = 200
    assert send.ping() == 'success'


# Same as the last three tests but with some duplication removed
# Thanks for the fancy footwork, pytest and mock libraries :)

@pytest.fixture(scope='session')
def send(): 
    
    yield Send()

@patch('my_package.myfirstmodule.maps.requests.get')
class TestSend(object):

    def test_get_request_called_once(self, mock_get, send):
        send.ping()
        mock_get.assert_called_once_with('http://google.com')

    def test_get_request_not_200(self, mock_get, send):
        mock_get.return_value.status_code = 'not 200'
        assert send.ping() == 'failure'

    def test_get_request_200(self, mock_get, send):
        mock_get.return_value.status_code = 200
        assert send.ping() == 'success'