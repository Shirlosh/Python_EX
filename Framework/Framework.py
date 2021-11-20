import json
import subprocess
from pathlib import Path

from SubProcessFactory import SubProcessFactory

INPUT1_PATH = r"C:\Users\oveda\Desktop\Python Siemplfy\asserts\lib\json-input\input1.json"


def run():
    sb = SubProcessFactory(INPUT1_PATH)
    out, err = sb.run()

    print(out)


if __name__ == "__main__":
    run()
