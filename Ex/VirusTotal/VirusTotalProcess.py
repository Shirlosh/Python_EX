import json

import requests
from Ex.Assert.DataModels import ConnectorParams, ConnectorResult


class VirusTotalProcess:
    __API_KEY = "c4759908a9936bf945e73018b64b11c8c39bcad147221276a1e1b0ed8b83e2d1"
    __VT_URL = "https://www.virustotal.com/api/v3/urls/"
    __urls = None

    def run(self, connector_params : ConnectorParams):
        #res = ConnectorResult()
        self.__init_urls(connector_params.source_folder_path)

        #for i in range(self.connector_params.iteration_entities_count):


    def __scanURL(self, resource):
        headers = {
            "Accept": "application/json",
            "x-apikey": self.__API_KEY
        }

        url = self.__buildURLWithResource(resource)
        response = requests.request("GET", url, headers=headers)
        print(response.text)

    def __buildURLWithResource(self, resource):
        return self.__VT_URL + resource

    def __init_urls(self, file_path):
        with open(file_path) as json_file:
            data = json.load(json_file)
            aList = json.dumps(data)
            print(data)
        self.__VT_URL = None;