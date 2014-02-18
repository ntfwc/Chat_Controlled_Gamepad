class BaseChatClient(object):
    def __init__(self, commandSelector):
        self.commandSelector = commandSelector
    
    def mainLoop(self):
        raise NotImplementedError("mainloop function not implemented")
    
    def run(self):
        self.mainLoop()

    
