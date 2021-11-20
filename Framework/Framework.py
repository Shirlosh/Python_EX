from apscheduler.schedulers.background import BackgroundScheduler
from VTConnectorFactory import VTConnectorFactory
import warnings

INPUT1_PATH = r"C:\Users\oveda\Desktop\Python Siemplfy\asserts\lib\json-input\input1.json"
INPUT2_PATH = r"C:\Users\oveda\Desktop\Python Siemplfy\asserts\lib\json-input\input2.json"


def handle_output(sb):
    bout, berr = sb.run()
    err = berr.decode()
    out = bout.decode()

    if err:
        print("Errors- " + err)
    if out:
        print("output- " + out)


def run():
    sched = BackgroundScheduler()
    warnings.filterwarnings("ignore")  # ignore module time area warnings
    sb_array = [VTConnectorFactory(INPUT1_PATH),VTConnectorFactory(INPUT1_PATH)]

    for sb in sb_array:
        def wrapper():
            handle_output(sb)

        sched.add_job(wrapper, 'interval', seconds=int(sb.get_interval()))
    sched.start()

    print("press 'Enter' to exit the process")
    while input():
        True


if __name__ == "__main__":
    try:
        run()
    except Exception as e:
        print(e)
