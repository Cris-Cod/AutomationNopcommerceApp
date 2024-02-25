import configparser

config = configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'baseUrl')
        return url

    @staticmethod
    def getUserEmail():
        user = config.get('common info', 'username')
        return user

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password