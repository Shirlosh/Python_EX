import json
import os
import sys
from pathlib import Path

from Ex.Assert.SetInterval import SetInterval
from Ex.VirusTotal.VirusTotalProcess import VirusAPI

interval_id = None


def folderPath():
    folder_path = sys.argv[1]
    if os.path.exists(folder_path):
        files = Path(folder_path).glob('*')
        for file in files:
            with open(file) as json_file:
                data = json.load(json_file)
            print(data)


def main():
    folderPath()


if __name__ == "__main__":
    interval_id = SetInterval(main, 10)

virus = VirusAPI()
virus.scanURL("d0e196a0c25d35dd0a84593cbae0f38333aa58529936444ea26453eab28dfc86")
