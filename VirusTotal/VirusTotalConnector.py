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

        # Connect API and get data (via stdin)
        connector_params = io_mgr.connector_params

        if self.__is_contain_format(connector_params.source_folder_path, self.FILE_FORMAT) is True:
            file_path = self.__get_random_file(connector_params)

            # Process Data
            connector_result = VT_process.run(file_path, connector_params.iteration_entities_count)

            # Send data back to Framework(via stdout)
            io_mgr.end(connector_result)
            self.__done_suffix(file_path)

        else:
            self.__end_process("all the source files in this folder have been checked")

    # checks if the folder has files with the required suffix
    @staticmethod
    def __is_contain_format(folder_path, suffix):
        files_counter = len(glob.glob1(folder_path, "*." + suffix))
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

    @staticmethod
    def __end_process(message):
        print(message)
        exit(1)


def mainWrapper():
    try:
        vt = VirusTotalConnector()
        vt.main()
    except ConnectionRefusedError as e:
        print(e)

    except IOError as e:
        raise print(e)

    except Exception:
        print("unknown error occur")


if __name__ == "__main__":
    mainWrapper()
