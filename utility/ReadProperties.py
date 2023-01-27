import configparser

config = configparser.RawConfigParser()
config.read(filenames='D:/nopCommerceProject/configurations/config.ini')


class ReadProperties:
    @staticmethod
    def getUrl():
        url = config.get('common info', 'url')
        return url

    @staticmethod
    def getUserEmail():
        userEmail = config.get('common info', 'userEmail')
        return userEmail

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password
