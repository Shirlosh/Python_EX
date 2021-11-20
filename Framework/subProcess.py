import json
import subprocess

from asserts.DataModels import ConnectorSettings, ConnectorParams


class SubProcessFactory:
    __connector_settings = ConnectorSettings()

    def __init__(self, setting_path):
        with open(setting_path) as json_file:
            data = json.load(json_file)
        dict_connector = data[ConnectorSettings.__name__][0]
        self.__init_instance_from_json(dict_connector, ConnectorSettings.__dict__, self.__connector_settings)

    def get_connector_setting(self):
        return self.__connector_settings

    def createSubProcess(self, process_name):
        p = subprocess.Popen(
            process_name,
            shell=True,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            close_fds=True)
        return p

    def __init_instance_from_json(self, dict_connector, class_att_dict, instance):

        cdir = [a for a in ConnectorSettings.__dict__ if not a.startswith('__')]
        for attribute in cdir:
            setattr(instance, attribute, dict_connector[attribute])

