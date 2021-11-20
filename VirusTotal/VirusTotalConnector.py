import glob
from pathlib import Path
from IO.SubProcessInputOutputHandler import SubProcessInputOutputHandler
import os
from VirusTotal.VirusTotalProcess import VirusTotalProcess


class VirusTotalConnector:

    FILE_FORMAT = "json"

    def main(self):
        io_mgr = SubProcessInputOutputHandler()
        VT_process = VirusTotalProcess()
        connector_params = io_mgr.connector_params
        file_path = self.__get_random_file(connector_params)

        connector_result = VT_process.run(file_path, connector_params.iteration_entities_count)

        io_mgr.end(connector_result)
        # done_suffix(file_path)

    @staticmethod
    def __is_contain_format(folder_path, prefix):
        files_counter = len(glob.glob1(folder_path, "*." + prefix))
        if files_counter > 0:
            return True
        else:
            return False

    # get a file path and changes the file suffix to .done
    @staticmethod
    def __done_suffix(file_path):
        new_file_path = str(file_path) + ".done"
        os.rename(file_path, new_file_path)

    # get a random file from the source folder
    # init file_path and return its value
    def __get_random_file(self, connector_params):
        files = Path(connector_params.source_folder_path).glob('*.' + self.FILE_FORMAT)
        file_path = next(files)
        return file_path


# TODO: redesign this:
if __name__ == "__main__":
    vt = VirusTotalConnector()
    vt.main()

    # try:
    #         main()
    #         # TODO: setinterval(main, time) instead of calling main
    #     else:
    #         raise ImportError("the requested folder path is invalid")
    # except Exception as e:
    #     print(e.__class__)
