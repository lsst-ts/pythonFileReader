import lsst.ts.pythonFileReader.ConfigurationFileReader as cfr
import yaml


class FileReaderYaml(cfr.FileReader):

    def __init__(self, path, settingsSet, settingsVersion, settingsFileName=""):
        self.path = path
        self.settingsSet = settingsSet
        self.settingsVersion = str(settingsVersion)
        self.separator = "/"
        self.settingsFileName = settingsFileName

    def getPath(self, settings):
        path = self.path
        if(self.settingsSet != ""):
            path += self.separator + self.settingsSet
        if(self.settingsVersion != ""):
            path += self.separator + self.settingsVersion
        path += self.separator + settings + ".yaml"
        return path

    def getAllAttributes(self):
        return self.yamlfile.keys()

    def readValue(self, attribute, yamlfile=None):
        if(yamlfile is None):
            return self.yamlfile[attribute]
        else:
            return yamlfile[attribute]

    def loadFile(self, settings):
        fileReader = FileReaderYaml(
            self.path, self.settingsSet, self.settingsVersion)
        self.settingsFileName = settings
        yamldata = open(fileReader.getPath(self.settingsFileName), "r")
        self.yamlfile = yaml.safe_load(yamldata)
        yamldata.close()

    def setSettingsSet(self, settingsSet, settingsVersion):
        self.settingsSet = settingsSet
        self.settingsVersion = str(settingsVersion)

    def getRecommendedSettings(self):
        # Recommended settings come from the path + filename
        fileReader = FileReaderYaml(self.path, "", "")
        yamldata = open(fileReader.getPath(self.settingsFileName), "r")
        mainSettings = yaml.safe_load(yamldata)
        recommendedSettings = self.readValue('recommendedSettings')
        yamldata.close()
        return ",".join(recommendedSettings)

    def setSettingsFromLabel(self, settingsToApply, mainConfigurationFile):
        if(settingsToApply.__contains__(";")):
            settingsValues = settingsToApply.split(";", 2)
            self.settingsSet = settingsValues[0]
            self.settingsVersion = int(settingsValues[1])
        else:
            recommendedSettings = mainConfigurationFile.readValue('aliases')
            if(settingsToApply not in recommendedSettings.keys()):
                raise ValueError(
                    f"Value=\"{settingsToApply}\" doesn't exist for recommended settings")
            self.settingsSet = recommendedSettings[settingsToApply]['settingSet']
            self.settingsVersion = recommendedSettings[settingsToApply]['settingVersion']
