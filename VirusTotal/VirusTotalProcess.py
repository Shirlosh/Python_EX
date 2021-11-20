import base64
import json
import os
import random
import requests
from asserts.DataModels import ConnectorResult


class VirusTotalProcess:
    __API_KEY = "c4759908a9936bf945e73018b64b11c8c39bcad147221276a1e1b0ed8b83e2d1"
    __VT_URL = "https://www.virustotal.com/api/v3/urls/"
    __urls: list
    __connector_result = ConnectorResult()
    folder_path = 'C:\\\\Users\\\\oveda\\\\Desktop\\\\Python Siemplfy\\\\asserts\\\\lib\\\\URLSource1\\\\Source1.json'

    #  Launch the desired amount of URL requests to the server
    #  Returns ConnectorResult as an answer (a dictionary of answers)
    def run(self, file_path, iteration_count):
        self.__init_urls(file_path)
        #self.__init_urls(self.folder_path)
        self.__init_connectorResult()
        iteration_count = int(iteration_count)

        for i in range(iteration_count):
            url = random.choice(self.__urls)
            response = self.__scanURL(url)
            self.__handle_response(url, response)
            self.__deleteURL_from_list(url)

        return self.__connector_result

    # Get a url and scan it using VirusTotal
    # Returns VirusTotal response
    def __scanURL(self, resource):
        headers = {
            "Accept": "application/json",
            "x-apikey": self.__API_KEY
        }

        url = self.__buildURLWithResource(resource)
        response = requests.request("GET", url, headers=headers)

        return response

    # Get a resource and create a proper URL to send
    def __buildURLWithResource(self, resource):
        resource_base64 = base64.urlsafe_b64encode(resource.encode()).decode().strip("=")
        return self.__VT_URL + resource_base64

    # Init URLS array variable
    def __init_urls(self, file_path):
        data = json.loads(open(file_path).read())
        self.__urls = data

    # Init connector result
    def __init_connectorResult(self):
        self.__connector_result.alerts = dict.fromkeys(self.__urls)

    # Removes a specific url from the URLs list
    def __deleteURL_from_list(self, url):
        self.__urls.remove(url)

    # Init the connector_result.alerts dictionary with the response data
    def __handle_response(self, resource, response):
        data = json.loads(response.content)
        self.__connector_result.alerts[resource] = data
