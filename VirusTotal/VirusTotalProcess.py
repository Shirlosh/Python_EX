import base64
import json
import os
import random

import requests

from asserts.DataModels import ConnectorParams, ConnectorResult


class VirusTotalProcess:
    __API_KEY = "c4759908a9936bf945e73018b64b11c8c39bcad147221276a1e1b0ed8b83e2d1"
    __VT_URL = "https://www.virustotal.com/api/v3/urls/"
    __urls: list
    __connector_result = ConnectorResult()

    #  launch the desired amount of URL requests to the server
    #  returns ConnectorResult as an answer (a dictionary of answers)
    def run(self, connector_params: ConnectorParams):
        self.__init_urls(connector_params.source_folder_path)
        self.__init_connectorResult()
        iteration_count = int(connector_params.iteration_entities_count)

        for i in range(iteration_count):
            url = random.choice(self.__urls)
            response = self.__scanURL(url)
            self.handle_response(url, response)
            self.deleteURL_from_list(url)

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

    # init URLS array variable
    def __init_urls(self, file_path):
        with open(file_path) as json_file:
            data = json.load(json_file)
        self.__urls = data

    # init connector result
    def __init_connectorResult(self):
        self.__connector_result.alerts = dict.fromkeys(self.__urls)

    # removes a specific url from the URLs list
    def deleteURL_from_list(self, url):
        self.__urls.remove(url)

    # s
    def handle_response(self, resource, response):
        data = json.loads(response.content)
        self.__connector_result.alerts[resource] = data
