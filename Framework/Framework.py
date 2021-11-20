import json
import subprocess
from pathlib import Path

from subProcess import SubProcessFactory

INPUT1_PATH = r"C:\Users\oveda\Desktop\Python Siemplfy\asserts\lib\json-input\input1.json"


def run():
    f = SubProcessFactory(INPUT1_PATH)
    connector = f.get_connector_setting()
    p = f.createSubProcess()
    y = json.dumps(connector.params).encode('utf-8')
    out, err = p.communicate(y)
    print(out)


if __name__ == "__main__":
    run()
