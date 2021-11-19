import base64
import json
import os
import random

import requests

from Assert.DataModels import ConnectorParams, ConnectorResult


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

    # create a ConnectorResponse from a VT response
    # evaluating the url using 'reputation' field
    def handle_response(self, resource, response):
        data = json.loads(response.content)
        rep = data['data']['attributes']['reputation']

        if rep >= 0:
            result = "not suspicious"
        else:
            result = self.format_response_answer(data)

        self.__connector_result.alerts[resource] = result
        print(resource, ':', result) #TODO: delete debug

    # formatting the result to a string result
    # the result contains the malicious/ suspicious files name and amount
    def format_response_answer(self, data):
        stats: dict = data['data']['attributes']['last_analysis_stats']
        webs: dict = data['data']['attributes']['last_analysis_results']

        result = "** suspicious **" + os.linesep
        result += '\t' + str(stats.get("malicious")) + " malicious files: " + os.linesep
        result += self.find_specific_category(webs, "malicious")
        result += '\t' + str(stats.get("suspicious")) + " suspicious files: " + os.linesep
        result += self.find_specific_category(webs, "suspicious")

        return result

    def find_specific_category(self, webs_dir, category):
        res = ""
        for k in webs_dir.items():
            var = k[1].get('category')
            if var == category:
                res += '\t\t'
                res += k[1].get("engine_name")
                res += os.linesep
        return res
