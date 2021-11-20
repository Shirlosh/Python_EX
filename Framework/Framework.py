import json
import subprocess
from pathlib import Path

from subProcess import SubProcessFactory

INPUT1_PATH = r"C:\Users\oveda\Desktop\Python Siemplfy\asserts\lib\json-input\input1.json"

def run():
    f = SubProcessFactory(INPUT1_PATH)
    # p = f.createSubProcess()


if __name__ == "__main__":
    run()
