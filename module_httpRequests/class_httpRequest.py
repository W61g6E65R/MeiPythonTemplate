# import.general
import os
import logging

# import.project
import requests
from requests.auth import HTTPBasicAuth

class HttpRequest:
    """
    Class for checking http endpoints

    Returns:
        _description_
    """    
    def __init__(self):
        self.__log = logging.getLogger(__name__)

    def check_url(self, url: str, httpMethod="GET", httpBody="", authType=None, username=None, password=None, proxy=None, headers=None, ignorePayload=False) -> int:
        """
        _summary_

        Arguments:
            url -- _description_

        Keyword Arguments:
            httpMethod -- _description_ (default: {"GET"})
            httpBody -- _description_ (default: {""})
            authType -- _description_ (default: {None})
            username -- _description_ (default: {None})
            password -- _description_ (default: {None})
            proxy -- _description_ (default: {None})
            headers -- _description_ (default: {None})
            ignorePayload -- _description_ (default: {False})

        Returns:
            _description_
        """        
        try:
            request_args = {}
            payloadType = ""
            # Sum up arguments
            request_args['headers']= headers
            if authType == "BASIC":
                if username and password:
                    request_args['auth'] = (username, password)

            request_args['proxies'] = {
                        "http": proxy,
                        "https": proxy,
                    }   
            
            if httpBody != "":
                request_args['json'] = httpBody
            
            # REQUEST
            if httpMethod == "POST":
                response = requests.post(url, **request_args)
            else: # GET
                response = requests.get(url, **request_args)
            
            responseTime = (response.elapsed).total_seconds()
            statusCode = response.status_code
            self.__log.info(f"Checking endpoint: {url} [{responseTime}ms/ {statusCode}]")
            
            if statusCode == 200:
                payload = response.text
                status = 1

            if statusCode != 200:
                payload = ""
                status = 0

            if ignorePayload == True:
                payload= ""

            # Check if HTML
            if payload.find("<!DOCTYPE html") != -1:
                isHTML = True
            else:
                isHTML = False

            # Check if JSON
            try:
                jsonObject = json.loads(payload)
                isJson = True
            except:
                isJson = False

            # JSON
            # Only reset status if DOWN in jsons. Else it is set over HTML Status code
            if isHTML == False and isJson == True:
                if "status" in jsonObject:
                    if jsonObject["status"] == "DOWN":
                        status = 0

            if isHTML:
                payloadType = "HTML"
            if isJson:
                payloadType = "JSON"
            
            retVal= {'status': status, 'responseTime': responseTime, 
                    'payload': payload, 'payloadType': payloadType, 
                    'httpCode':statusCode}

            return retVal
        
        except requests.exceptions.ConnectionError as conn_err:
            self.__log.error(f"ERROR while checking url:{url}")
            self.__log.error(conn_err)
            retVal= {'status': 0, 'responseTime': 0, 
                    'payload': "Could not reach url", 'payloadType': "", 
                    'httpCode':404}
            return retVal        

        except requests.exceptions.Timeout as timeout_err:
            self.__log.error(f"ERROR while checking url:{url}")
            self.__log.error(timeout_err)
            retVal= {'status': 0, 'responseTime': 0, 
                    'payload': "Could not reach url", 'payloadType': "", 
                    'httpCode':408}
            return retVal         

        except requests.RequestException as err:
            self.__log.error(f"ERROR while checking url:{url}")
            self.__log.error(err)
            retVal= {'status': 0, 'responseTime': 0, 
                    'payload': "Could not reach url", 'payloadType': "", 
                    'httpCode':0}
            return retVal

    