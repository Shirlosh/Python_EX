import json
import subprocess
from asserts.DataModels import ConnectorSettings

#TODO: factory as a abstract class and this as vtfactory
class SubProcessFactory:
    __connector_settings = ConnectorSettings()
    __process = None
    __out = None

    def __init__(self, setting_path):
        with open(setting_path) as json_file:
            data = json.load(json_file)
        dict_connector = data[ConnectorSettings.__name__][0]
        self.__init_instance_from_json(dict_connector)

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

