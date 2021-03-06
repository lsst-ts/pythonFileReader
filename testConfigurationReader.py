import unittest
import ConfigurationFileReaderYaml as ryaml

class TestConfigurationReader(unittest.TestCase):

    def setUp(self):
        self.fileYaml = ryaml.FileReaderYaml("C:\\Users\\aanania\\PycharmProjects\\ts_electrometer3\\settingFiles", "Test", 1)
        self.fileYaml.loadFile("serialConfiguration")

    def test_baudrate(self):
        baudrate = self.fileYaml.readValue('baudrate')
        self.assertEqual(57600, baudrate)

    def test_port(self):
        port = self.fileYaml.readValue('port')
        self.assertEqual("/dev/ttyACM1", port)

    def test_parity(self):
        parity = self.fileYaml.readValue('parity')
        self.assertEqual('N', parity)

    def test_stopBits(self):
        stopBits = self.fileYaml.readValue('stopBits')
        self.assertEqual(1, stopBits)

    def test_byteSize(self):
        byteSize = self.fileYaml.readValue('byteSize')
        self.assertEqual(7, byteSize)

    def test_byteToRead(self):
        byteToRead = self.fileYaml.readValue('byteToRead')
        self.assertEqual(1, byteToRead)

    def test_timeout(self):
        timeout = self.fileYaml.readValue('timeout')
        self.assertEqual(3.3, timeout)

    def test_xonxoff(self):
        xonxoff = self.fileYaml.readValue('xonxoff')
        self.assertEqual(0, xonxoff)

    def test_dsrdtr(self):
        dsrdtr = self.fileYaml.readValue('dsrdtr')
        self.assertEqual(0, dsrdtr)

    def test_termChar(self):
        termChar = self.fileYaml.readValue('termChar')
        self.assertEqual("\n", termChar)

    def test_getRecommendedSettings(self):
        recommendedSettings = self.fileYaml.getRecommendedSettings()
        self.assertEqual("Default1,Default2", recommendedSettings)

    def test_setSettingsFromLabelSettingSet(self):
        self.fileYaml.setSettingsFromLabel('Default1')
        self.assertEqual(self.fileYaml.settingsSet, "Test1")

    def test_setSettingsFromLabelSettingsVersion(self):
        self.fileYaml.setSettingsFromLabel('Default1')
        self.assertEqual(self.fileYaml.settingsVersion,1)

    def test_getValueFromMainSettings1(self):
        value = self.fileYaml.getValueFromMainSettings('salId')
        self.assertEqual(value, 1)

    def test_getValueFromMainSettings2(self):
        value = self.fileYaml.getValueFromMainSettings('filePath')
        self.assertEqual(value, "C:\\Users\\aanania\\PycharmProjects\\ts_electrometer3\\fitsFiles")

    def test_setSettingsFromLabelSettingsVersion2(self):
        #Test from direct definition of which settings to use (e.g. Test;1)
        self.fileYaml.setSettingsFromLabel('Test;1')
        self.assertEqual(self.fileYaml.settingsVersion,1)

    def test_setSettingsFromLabelSettingsVersion3(self):
        #Test from direct definition of which settings to use (e.g. Test;1)
        self.fileYaml.setSettingsFromLabel('Test;2')
        self.assertEqual(self.fileYaml.settingsVersion,2)