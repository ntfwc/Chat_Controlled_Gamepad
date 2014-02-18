from _BaseCommandSelector import BaseCommandSelector

class BasicCommandSelector(BaseCommandSelector):
    def mainloop(self):
        while True:
            commandContainer = self.queue.get()
            print commandContainer.command
            self.gamepad.runCommand(commandContainer.command)
