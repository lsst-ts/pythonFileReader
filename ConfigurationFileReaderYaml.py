import ConfigurationFileReader as cfr
import yaml

class FileReaderYaml(cfr.FileReader):

    def __init__(self, path, settingsSet, settingsVersion, mainSettingsFileName="mainSetup"):
        self.path = path
        self.settingsSet = settingsSet
        self.settingsVersion = str(settingsVersion)
        self.yamlfile = None
        self.separator = "\\"
        self.mainSettingsFileName = mainSettingsFileName

    def getPath(self, settings):
        path = self.path
        if(self.settingsSet != ""):
            path += self.separator+self.settingsSet
        if(self.settingsVersion != ""):
            path += self.separator+self.settingsVersion
        path += self.separator+settings+".yaml"
        return path

    def getAllAttributes(self):
        return self.yamlfile.keys()

    def readValue(self, attribute, yamlfile=None ):
        if(yamlfile is None):
            return self.yamlfile[attribute]
        else:
            return yamlfile[attribute]

    def loadFile(self, settings):
        fileReader = FileReaderYaml(self.path, self.settingsSet, self.settingsVersion)
        yamldata = open(fileReader.getPath(settings), "r")
        self.yamlfile = yaml.safe_load(yamldata)
        yamldata.close()

    def setSettingsSet(self, settingsSet, settingsVersion):
        self.settingsSet = settingsSet
        self.settingsVersion = str(settingsVersion)

    def getRecommendedSettings(self):
        #Recommended settings come from the path + filename
        fileReader = FileReaderYaml(self.path, "", "")
        yamldata = open(fileReader.getPath(self.mainSettingsFileName), "r")
        mainSettings = yaml.safe_load(yamldata)
        recommendedSettings = self.readValue('recommendedSettings', mainSettings)
        yamldata.close()
        return ",".join(recommendedSettings)

    def setSettingsFromLabel(self, settingsToApply):
        fileReader = FileReaderYaml(self.path, "", "")
        yamldata = open(fileReader.getPath(self.mainSettingsFileName), "r")
        mainSettings = yaml.safe_load(yamldata)
        recommendedSettings = self.readValue('aliases', mainSettings)
        if(settingsToApply not in recommendedSettings.keys()): raise ValueError(f"Value=\"{settingsToApply}\" doesn't exist for recommended settings")
        self.settingsSet = recommendedSettings[settingsToApply]['settingSet']
        self.settingsVersion = recommendedSettings[settingsToApply]['settingVersion']
        yamldata.close()


if __name__ == "__main__":
    fileYaml = FileReaderYaml("C:\\Users\\aanania\\PycharmProjects\\ts_electrometer3\\settingFiles", "Test", 1)
    #fileYaml.loadFile("example")
    fileYaml.setSettingsFromLabel("Default13")
#    print(fileYaml.readStringValue('baudrate'))
#    print(fileYaml.getAllAttributes())
