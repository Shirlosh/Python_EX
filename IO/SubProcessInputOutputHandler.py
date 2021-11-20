import json
import os
from pathlib import Path
from asserts.DataModels import ConnectorParams, ConnectorResult


class SubProcessInputOutputHandler(object):
    __folder_path = None
    __file_format = None
    __file_path = None
    #
    # def __init__(self, folder_path, file_format):
    #     self.__folder_path = folder_path
    #     self.__file_format = file_format

    @property
    def connector_params(self):
        result = ConnectorParams()
        x = input()
        j = json.loads(x)
        result.source_folder_path = j["source_folder_path"] #TODO: reflection
        result.iteration_entities_count = j["iteration_entities_count"]
        return result

    def end(self, connector_result: ConnectorResult):
        for k in connector_result.alerts:
            if connector_result.alerts[k] is not None:
                response = self.handle_response(k, connector_result.alerts[k])
                print(k, ':', response)

    # get a random file from the source folder
    # init file_path and return its value
    def get_random_file(self):
        files = Path(self.__folder_path).glob('*.' + self.__file_format)
        self.__file_path = next(files)
        return self.__file_path

    # create a ConnectorResponse from a VT response
    # evaluating the url using 'reputation' field
    def handle_response(self, resource, data):

        rep = data['data']['attributes']['reputation']

        if rep >= 0:
            result = "not suspicious"
        else:
            result = self.format_response_answer(data)

        return result

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
