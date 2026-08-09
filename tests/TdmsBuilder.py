from numpy import array
from nptdms import ChannelObject, TdmsFile
import numpy as np

class TdmsBuilder:
    def __init__(self):
        self.root = {}

    def _addGroup(self, groupName):
        if groupName not in self.root:
            self.root[groupName] = {}

    def addChannel(self, group, channel, data):
        if group not in self.root:
            self._addGroup(group)
        self.root[group][channel] = array(data)

    def getChannels(self):
        channels = []
        for group, channelObj, in self.root.items():
            for channel, data, in channelObj.items():
                channels.append(ChannelObject(group, channel, data))
        return channels

    def compare(self, tdmsFile: TdmsFile):
        fileGroups = list(group.name for group in tdmsFile.groups())
        builderGroups = list(self.root.keys())

        if builderGroups != fileGroups:
            return False

        for group in tdmsFile.groups():
            groupName = group.name

            fileChannels = list(channel.name for channel in group.channels())
            builderChannels = list(self.root[groupName].keys())

            if builderChannels != fileChannels:
                return False

            for channel in group.channels():
                channelName = channel.name
                fileData = channel[:]
                builderData = self.root[groupName][channelName]

                if not np.array_equal(builderData, fileData):
                    return False
        return True