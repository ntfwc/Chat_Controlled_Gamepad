from threading import Thread
from Queue import Queue

from CommandContainer import CommandContainer

DEFAULT_MAX_QUEUE_SIZE = 10000

class BaseCommandSelector(Thread):
    def __init__(self, gamepad):
        Thread.__init__(self)
        self.gamepad = gamepad
        self.daemon = True
        self.queue = Queue(DEFAULT_MAX_QUEUE_SIZE)

    def sendInput(self, message, user=0):
        command = self.gamepad.translateInputMessage(message)
        if command != None:
            self.queue.put(CommandContainer(command, user))

    def mainloop(self):
        raise NotImplementedError("mainloop function not implemented")

    def run(self):
        self.gamepad.connect()
        self.mainloop()
