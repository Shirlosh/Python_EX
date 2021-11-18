import threading


class SetInterval:
    action = None
    time = None
    __startTime = None

    def __init__(self, action, time):
        self.action = action
        self.time = int(time)
        self.__setInterval()

    def __setInterval(self):
        e = threading.Event()
        while not e.wait(self.time):
            self.action()
