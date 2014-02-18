##    Copyright (C) 2014 ntfwc <ntfwc@yahoo.com>
##
##    This program is free software; you can redistribute it and/or modify
##    it under the terms of the GNU General Public License as published by
##    the Free Software Foundation; either version 2 of the License, or
##    (at your option) any later version.
##
##    This program is distributed in the hope that it will be useful,
##    but WITHOUT ANY WARRANTY; without even the implied warranty of
##    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##    GNU General Public License for more details.
##
##    You should have received a copy of the GNU General Public License along
##    with this program; if not, write to the Free Software Foundation, Inc.,
##    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.


#from gamepads.NESGamepad import NESGamepad
from gamepads.SNESGamepad import SNESGamepad
#from gamepads.GBAGamepad import GBAGamepad
#from gamepads.PS1Gamepad import PS1Gamepad
from commandSelectors.BasicCommandSelector import BasicCommandSelector
#from commandSelectors.CommandVotingSelector import CommandVotingSelector
from chatClients.CommandLineClient import CommandLineClient
#from chatClients.IRCClient import IRCClient

IRC_HOST = "127.0.0.1"
IRC_PORT = 6667
IRC_NICKNAME = "gamepadBot"
IRC_CHANNEL = "blarg"
IRC_PASSWORD = None

INPUT_COLLECTION_TIME = 1.2

def main():
    #gamepad = NESGamepad()
    gamepad = SNESGamepad()
    #gamepad = GBAGamepad()
    #gamepad = PS1Gamepad()
    #commandSelector = BasicCommandSelector(gamepad)
    commandSelector = CommandVotingSelector(gamepad, INPUT_COLLECTION_TIME)
    chatClient = CommandLineClient(commandSelector)
    #chatClient = IRCClient(commandSelector, IRC_HOST, IRC_PORT, IRC_NICKNAME, IRC_CHANNEL, IRC_PASSWORD)
    
    commandSelector.start()
    chatClient.run()


if __name__ == "__main__":
    main()
