import os

from ConnectorFactory import ConnectorFactory
import json
import subprocess
from asserts.DataModels import ConnectorSettings


class VTConnectorFactory(ConnectorFactory):
    __connector_settings = ConnectorSettings()
    __process = None
    __out = None

    def __init__(self, setting_path):
        if os.path.exists(setting_path) is False:
            raise IOError("input file path is incorrect, please try again")

        with open(setting_path) as json_file:
            data = json.load(json_file)
        dict_connector = data[ConnectorSettings.__name__][0]
        self.__init_instance_from_json(dict_connector)

    # override
    def run(self):
        self.__createSubProcess()
        return self.__setCommunication()

    def __createSubProcess(self):
        self.__process = subprocess.Popen(
            self.__connector_settings.script_file_path,
            shell=True,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            close_fds=True)

    def __setCommunication(self):
        data = json.dumps(self.__connector_settings.params).encode('utf-8')
        return self.__process.communicate(data)

    def __init_instance_from_json(self, dict_connector):
        cdir = [a for a in ConnectorSettings.__dict__ if not a.startswith('__')]
        for attribute in cdir:
            setattr(self.__connector_settings, attribute, dict_connector[attribute])

    def get_interval(self):
        return self.__connector_settings.run_interval_seconds

    def get_output_path(self):
        return self.__connector_settings.output_folder_path
