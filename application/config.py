import configparser
config = configparser.ConfigParser()
config['weblog'] = {'index': 'web_log-*',
                     'ipendpoint': '127.0.0.1:9200'
                     }
with open('example.ini', 'w') as configfile:
  config.write(configfile)