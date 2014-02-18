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
