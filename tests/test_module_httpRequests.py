# import.global
import pytest

# import.local
from module_httpRequests.class_httpRequest import HttpRequest

# FAILURE
def test_404_failure():
    httpRequest = HttpRequest()
    retVal = httpRequest.check_url("https://www.SiCherKeINgoogle.de")
    assert retVal['httpCode'] == 404

# SUCCESS
def test_401_Auth_success():
    httpRequest = HttpRequest()
    retVal = httpRequest.check_url("http://ER-ANW-ENAIO01/api/dms/info")
    assert retVal['httpCode'] == 401

def test_401_responsteTime_success():
    httpRequest = HttpRequest()
    retVal = httpRequest.check_url("http://ER-ANW-ENAIO01/api/dms/info")
    assert retVal['responseTime'] > 0.0