from SubProcessFactory import SubProcessFactory

INPUT1_PATH = r"C:\Users\oveda\Desktop\Python Siemplfy\asserts\lib\json-input\input1.json"


def run():
    sb = SubProcessFactory(INPUT1_PATH)
    # get interval
    # get file place
    # set interval
    # write result to file
    # handle exceptions
    out, err = sb.run()

    print(out)


if __name__ == "__main__":
    run()
