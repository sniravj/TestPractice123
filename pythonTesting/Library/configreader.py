import configparser

def conf_reader(section, key):
    config = configparser.ConfigParser()
    config.read('/Users/neha/PycharmProjects/pythonTesting/Config/Config.cfg')
    ['Config.cfg']

    return config[section][key]





