from abc import ABC, abstractmethod

class FileReader(ABC):

    def __init__(self):
        self.path = ""
        self.settingsSet = ""
        self.settingsVersion = ""
        self.settingsFileName = settingsFileName
        self.separator = "/"

    @abstractmethod
    def getAllAttributes(self):
        pass

    @abstractmethod
    def loadFile(self):
        pass

    @abstractmethod
    def readValue(self, attribute, yamlfile=None ):
        pass

    @abstractmethod
    def setSettingsSet(self):
        pass

    @abstractmethod
    def getRecommendedSettings(self):
        pass

    @abstractmethod
    def setSettingsFromLabel(self, settingsToApply, mainConfigurationFile):
        pass
