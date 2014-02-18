from gamepads.NESGamepad import NESGamepad
from commandSelectors.BasicCommandSelector import BasicCommandSelector
from chatClients.CommandLineClient import CommandLineClient

def main():
    gamepad = NESGamepad()
    commandSelector = BasicCommandSelector(gamepad)
    chatClient = CommandLineClient(commandSelector)
    
    commandSelector.start()
    chatClient.run()


if __name__ == "__main__":
    main()
