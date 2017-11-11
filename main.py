import discord
import time
import asyncio
import sys
from Implementation import YouTuber
from config import Config

config = Config('config.yml')
client = discord.Client()
youtubers = config.getYouTubersList() if (config.getYouTubersNr() != 0) else sys.exit()
if (config.getDiscordChannelNr() == 0): sys.exit()
id = ''
GOOGLE_API = config.getConnectionData()[0]
pingEveryXMinutes = config.getPingTime()
threads = []
processes = []

i = 0
while i < config.getYouTubersNr():
    temp_list = []
    temp_list.append(config.getYouTubersList()[i]['name'])
    temp_list.append(id) if not config.getYouTubersList()[i]['channelID'] else temp_list.append(config.getYouTubersList()[i]['channelID'])
    temp_list.append(True) if not id else temp_list.append(False)
    temp_list.append('')
    threads.append(temp_list)
    i += 1

i = 0

while i < config.getYouTubersNr():
    processes.append(YouTuber(GOOGLE_API, threads[i][1], threads[i][2]))
    i += 1

async def update():
    while True:
        try:
            waittime = pingEveryXMinutes * 60
            item = 0
            while item < config.getYouTubersNr():
                data = processes[item].update()
                print('Checking for new videos from {}'.format(threads[item][0]))
                if processes[item].isNewVideo():
                    print('{} HAS UPLOADED A NEW VIDEO! PUSHING UPDATE ON DISCORD.'.format(threads[item][0]))
                    for x in range (0, config.getDiscordChannelNr()):
                        newvideo = config.getDiscordChannelList()[x]['New video'].format(threads[item][0]) + '\n{}'.format(processes[item].getVideoLink(processes[item].videosData[0][1]))
                        await client.send_message(client.get_channel(str(config.getDiscordChannelList()[x]['channelID'])), newvideo)

                if processes[item].isUserLive():
                    if not processes[item].liveId == threads[item][3]:
                        print('{} IS LIVESTREAMING NOW! PUSHING UPDATE ON DISCORD.'.format(threads[item][0]))
                        threads[item][3] = processes[item].liveId
                        for x in range (0, config.getDiscordChannelNr()):
                            livestream = config.getDiscordChannelList()[x]['Livestream'].format(threads[item][0]) + '\n{}'.format(processes[item].getVideoLink(processes[item].getUserLiveData()))
                            await client.send_message(client.get_channel(str(config.getDiscordChannelList()[x]['channelID'])), livestream)
                item += 1
        except:
            pass
        while waittime > 0:
            mins, secs = divmod(waittime, 60)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            sys.stdout.write('Rechecking in ' + str(timeformat) + '\r')
            waittime -= 1
            await asyncio.sleep(1)

@client.event
async def on_ready():
    print('Logged in as:')
    print(client.user.name)
    print(client.user.id)
    print('---------------------------------------')
    print('Bot running.')
    asyncio.ensure_future(update())

client.run(config.getConnectionData()[1])