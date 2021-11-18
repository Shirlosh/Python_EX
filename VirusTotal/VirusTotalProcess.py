import base64
import json
import random

import requests

from Assert.DataModels import ConnectorParams, ConnectorResult


class VirusTotalProcess:
    __API_KEY = "c4759908a9936bf945e73018b64b11c8c39bcad147221276a1e1b0ed8b83e2d1"
    __VT_URL = "https://www.virustotal.com/api/v3/urls/"
    __urls = None
    __response = None

    def run(self, connector_params: ConnectorParams):
        self.__init_urls(connector_params.source_folder_path)

        # res = ConnectorResult()
        # res.alerts = {}
        # for i in range(self.connector_params.iteration_entities_count):
        url = random.choice(self.__urls)
        self.__scanURL(url)
        # delete url from the list

    def __scanURL(self, resource):
        headers = {
            "Accept": "application/json",
            "x-apikey": self.__API_KEY
        }
        resource_base64 = base64.urlsafe_b64encode(resource.encode()).decode().strip("=")
        url = self.__buildURLWithResource(resource_base64)
        response = requests.request("GET", url, headers=headers)
        self.add_response_to_result(resource, response)

    def __buildURLWithResource(self, resource):
        return self.__VT_URL + resource

    def __init_urls(self, file_path):
        with open(file_path) as json_file:
            data = json.load(json_file)
        self.__urls = data

    def add_response_to_result(self, resource, response):
        data = json.loads(response.content)
        rep = data['data']['attributes']['reputation']
        if rep < 0:
            result = "suspicious"
        else:
            result = "not suspicious"

        print(resource, ':', result)
        #TODO: add res to result dir