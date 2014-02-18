from gamepads.NESGamepad import NESGamepad
#from commandSelectors.BasicCommandSelector import BasicCommandSelector
from commandSelectors.CommandVotingSelector import CommandVotingSelector
#from chatClients.CommandLineClient import CommandLineClient
from chatClients.IRCClient import IRCClient

IRC_HOST = "127.0.0.1"
IRC_PORT = 6667
IRC_NICKNAME = "gamepadBot"
IRC_CHANNEL = "blarg"

INPUT_COLLECTION_TIME = 1.2

def main():
    gamepad = NESGamepad()
    #commandSelector = BasicCommandSelector(gamepad)
    commandSelector = CommandVotingSelector(gamepad, INPUT_COLLECTION_TIME)
    #chatClient = CommandLineClient(commandSelector)
    chatClient = IRCClient(commandSelector, IRC_HOST, IRC_PORT, IRC_NICKNAME, IRC_CHANNEL)
    
    commandSelector.start()
    chatClient.run()


if __name__ == "__main__":
    main()
