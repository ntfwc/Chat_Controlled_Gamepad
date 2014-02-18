from _BaseChatClient import BaseChatClient

from twisted.words.protocols import irc
from twisted.internet import reactor, protocol

class _ListeningBot(irc.IRCClient):
    def __init__(self, commandSelector, nickname, password, channel):
        self.commandSelector = commandSelector
        self.nickname = nickname
        self.password = password
        self.channel = channel

    def connectionMade(self):
        irc.IRCClient.connectionMade(self)
        print "Connected to server"

    def connectionLost(self, reason):
        irc.IRCClient.connectionLost(self, reason)
        print "Lost connection to server"
    
    def signedOn(self):
        self.join(self.channel)

    def joined(self, channel):
        print "Joined channel %s" % channel

    def privmsg(self, user, channel, msg):
        usernameEnd = user.find("!")
        username = user[:usernameEnd]
        if channel == self.nickname:
            pass
        else:
            msg = msg.strip().lower()
            self.commandSelector.sendInput(msg, username)

    def action(self, user, channel, msg):
        pass
            
    def alterCollidedNick(self, nickname):
        return nickname + '^'

class _ListeningBotFactory(protocol.ClientFactory):
    def __init__(self, commandSelector, nickname, password, channel):
        self.commandSelector = commandSelector
        self.clientNickname = nickname
        self.clientPassword = password
        self.channel = channel

    def buildProtocol(self, addr):
        p = _ListeningBot(self.commandSelector, self.clientNickname, self.clientPassword, self.channel)
        return p

    def clientConnectionLost(self, connector, reason):
        """If we get disconnected, reconnect to server."""
        connector.connect()

    def clientConnectionFailed(self, connector, reason):
        print "connection failed:", reason
        reactor.stop()


class IRCClient(BaseChatClient):
    def __init__(self, commandSelector, host, port, nickname, channel, password=None):
        self.commandSelector = commandSelector
        self.host = host
        self.port = port
        self.nickname = nickname
        self.password = password
        self.channel = channel
    
    def mainLoop(self):
        factory = _ListeningBotFactory(self.commandSelector, self.nickname, self.password, self.channel)
        reactor.connectTCP(self.host, self.port, factory)
        reactor.run()
