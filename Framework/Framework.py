from SubProcessFactory import SubProcessFactory
from apscheduler.schedulers.background import BackgroundScheduler

INPUT1_PATH = r"C:\Users\oveda\Desktop\Python Siemplfy\asserts\lib\json-input\input1.json"


def handle_output(sb):
    out = sb.run()
    print(out)


def run():
    sched = BackgroundScheduler()
    sb_array = [SubProcessFactory(INPUT1_PATH)]

    out = sb_array[0].run()

    for sb in sb_array:

        def wrapper():
            handle_output(sb)

        sched.add_job(wrapper, 'interval', seconds=int(sb.get_interval()))
    sched.start()

    print("press 'Enter' to exit the process")
    while input():
        True


if __name__ == "__main__":
    run()

# TODO:
# class wrapper
# handle_output
# exceptions



