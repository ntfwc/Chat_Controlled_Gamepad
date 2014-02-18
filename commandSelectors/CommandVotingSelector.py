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


from _BaseCommandSelector import BaseCommandSelector
from _BaseCommandSelector import DEFAULT_MAX_QUEUE_SIZE
from threading import Thread
from Queue import Queue

from Queue import Empty as EmptyException
from time import sleep

from random import choice

def __addCountToDictionaryEntry(dictionary, entry):
    if entry not in dictionary:
        dictionary[entry] = 1
        return
    dictionary[entry] += 1

def __getHighestValue(dictionary):
    values = dictionary.itervalues()
    highestValueSeen = -100

    for value in values:
        if value > highestValueSeen:
            highestValueSeen = value

    return highestValueSeen

def __getHighestVotedCommands(voteDictionary):
    highestVoteCount = __getHighestValue(voteDictionary)

    highestVotedCommands = []
    items = voteDictionary.iteritems()
    for command, voteCount in items:
        if voteCount == highestVoteCount:
            highestVotedCommands.append(command)

    return highestVotedCommands

def _extractHighestVotedCommand(commandContainerList):
    alreadyVotedSet = set()
    voteDictionary = {}
    for commandContainer in commandContainerList:
        user = commandContainer.user
        if user not in alreadyVotedSet:
            alreadyVotedSet.add(user)
            __addCountToDictionaryEntry(voteDictionary, commandContainer.command)

    highestVotedCommands = __getHighestVotedCommands(voteDictionary)

    return choice(highestVotedCommands)

class CommandVotingSelector(BaseCommandSelector):
    def __init__(self, gamepad, inputCollectionTime):
        Thread.__init__(self)
        self.gamepad = gamepad
        self.daemon = True
        self.queue = Queue(DEFAULT_MAX_QUEUE_SIZE)
        self.inputCollectionTime = inputCollectionTime
    
    def __extractAllQueuedCommands(self):
        l = []
        while True:
            try:
                l.append(self.queue.get_nowait())
            except EmptyException:
                break
        return l
        
    def mainloop(self):
        while True:
            sleep(self.inputCollectionTime)
            commandContainerList = self.__extractAllQueuedCommands()
            if len(commandContainerList) > 0:
                command = _extractHighestVotedCommand(commandContainerList)
                if command != None:
                    self.gamepad.runCommand(command)
