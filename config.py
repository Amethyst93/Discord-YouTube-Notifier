import yaml
import sys

import random
import string

class Config():
    def __init__(self, fileName):

        global cfg

        try:
            with open(fileName, 'r') as ymlfile:
                cfg = yaml.load(ymlfile)
        except Exception as e:
            print(e)
            input("Press any key to exit the program")
            sys.exit()

        if not cfg['config']['connection']['Google API key']:
            input('ERROR: Missing YouTube API v3 key in config file!')
            sys.exit()

        if not cfg['config']['connection']['Discord bot token']:
            input('ERROR: Missing Discord bot token in config file!')
            sys.exit()

        if self.getDiscordChannelNr() == 0:
            input('ERROR: Missing the Discord channel ID in config file!')
            sys.exit()

        if self.getYouTubersNr() == 0:
            input('ERROR: No YouTubers found in config file list or missing information!')
            sys.exit()

    def getConnectionData(self):
        return [cfg['config']['connection']['Google API key'], cfg['config']['connection']['Discord bot token']]

    def getPingTime(self):
        return cfg['config']['main']['Ping Every x Minutes']

    def getYouTubersList(self):
        return cfg['config']['YouTubers']

    def getDiscordChannelList(self):
        return cfg['config']['Discord Channel']

    def getDiscordChannelNr(self):
        if not cfg['config']['Discord Channel']:
            return 0
        return len(cfg['config']['Discord Channel'])
    def getYouTubersNr(self):
        if not cfg['config']['YouTubers']:
            return 0
        return len(cfg['config']['YouTubers'])