import json
import os
from asserts.DataModels import ConnectorParams, ConnectorResult


class SubProcessInputOutputHandler(object):
    __folder_path = None

    @property
    def connector_params(self):
        result = ConnectorParams()
        x = input()
        j = json.loads(x)
        result.source_folder_path = j["source_folder_path"] #TODO: reflection
        result.iteration_entities_count = j["iteration_entities_count"]
        # result.source_folder_path = r"C:\\Users\\oveda\\Desktop\\Python Siemplfy\\asserts\\lib\\URLSource1"  # DEBUG
        # result.iteration_entities_count = 4  # DEBUG
        return result

    def end(self, connector_result: ConnectorResult):
        for k in connector_result.alerts:
            if connector_result.alerts[k] is not None:
                response = self.__handle_response(k, connector_result.alerts[k])
                print(k, ':', response)

    # Create a ConnectorResponse from a VT response
    # Evaluating the url using 'reputation' field
    def __handle_response(self, resource, data):

        if 'error' in data:
            message = data['error']['message']
            raise ConnectionRefusedError("an issue occur with VT server:" + message)

        rep = data['data']['attributes']['reputation']

        if rep >= 0:
            result = "not suspicious"
        else:
            result = self.__format_response_answer(data)

        return result

    # Formatting the result to a string result
    # The result contains the malicious/ suspicious files name and amount
    def __format_response_answer(self, data):
        stats: dict = data['data']['attributes']['last_analysis_stats']
        webs: dict = data['data']['attributes']['last_analysis_results']

        result = "** suspicious **" + os.linesep
        result += '\t' + str(stats.get("malicious")) + " malicious files: " + os.linesep
        result += self.__find_specific_category(webs, "malicious", )
        result += '\t' + str(stats.get("suspicious")) + " suspicious files: " + os.linesep
        result += self.__find_specific_category(webs, "suspicious", )

        return result

    # Find the requested category in the dictionary(webs_dir)
    # Returns the string value of it
    @staticmethod
    def __find_specific_category(webs_dir, category):
        res = ""
        for k in webs_dir.items():
            var = k[1].get('category')
            if var == category:
                res += '\t\t'
                res += k[1].get("engine_name")
                res += os.linesep
        return res
