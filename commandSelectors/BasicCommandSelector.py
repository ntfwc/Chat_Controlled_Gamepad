from _BaseCommandSelector import BaseCommandSelector

class BasicCommandSelector(BaseCommandSelector):
    def mainloop(self):
        while True:
            commandContainer = self.queue.get()
            self.gamepad.runCommand(commandContainer.command)
