import glob
from IO.SubProcessInputOutputHandler import SubProcessInputOutputHandler
import sys
import os

from VirusTotal.VirusTotalProcess import VirusTotalProcess

interval_id = None
FILE_FORMAT = "json"


def main():
    folder_path = str(sys.argv[1])
    io_mgr = SubProcessInputOutputHandler(folder_path, FILE_FORMAT)
    API_process = VirusTotalProcess()

    while is_contain_format(folder_path, FILE_FORMAT):
        connector_params = io_mgr.connector_params
        connector_result = API_process.run(connector_params)
        io_mgr.end(connector_result)


def is_contain_format(folder_path, prefix):
    files_counter = len(glob.glob1(folder_path, "*." + prefix))
    if files_counter > 0:
        return True
    else:
        return False


# TODO: redesign this:
if __name__ == "__main__":
    try:
        if os.path.exists(sys.argv[1]):
            main()
            # TODO: setinterval(main, time) instead of calling main
        else:
            raise ImportError("the requested folder path is invalid")
    except Exception as e:
        print(e.__class__)
