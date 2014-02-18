from _BaseChatClient import BaseChatClient

class CommandLineClient(BaseChatClient):
    def mainLoop(self):
        while True:
            message = raw_input()
            self.commandSelector.sendInput(message)
