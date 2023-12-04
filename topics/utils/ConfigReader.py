import configparser
import pathlib

class ConfigReader:
    defaultConfigFile="config.ini"
    defaultConfigDir="config"
    def __init__(self,configFile=defaultConfigFile,configDir=defaultConfigDir):
        self.configFile=pathlib.Path(__file__).resolve().parent.parent.joinpath(configDir).joinpath(configFile)
        self.configParser=configparser.ConfigParser()
        self.configParser.read(self.configFile)
    def get_gmail_email(self):
        return self.configParser['gmail']['email']