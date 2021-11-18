from pathlib import Path

from Assert.DataModels import ConnectorParams


class SubProcessInputOutputHandler(object):
    __folder_path = None
    __file_format = None
    __file_path = None

    def __init__(self, folder_path, file_format):
        self.__folder_path = folder_path
        self.__file_format = file_format

    @property
    def connector_params(self):
        result = ConnectorParams()
        result.source_folder_path = self.get_random_file()
        result.iteration_count = input("please enter a number of entities to read from " + str(self.__file_path))
        return result

    def end(self, connector_result):
        # TODO: output the result to stdout
        raise Exception()

    # get a random file from the source folder
    # init file_path and return its value
    def get_random_file(self):
        files = Path(self.__folder_path).glob('*.' + self.__file_format)
        self.__file_path = next(files)
        return self.__file_path
