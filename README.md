# Discord YouTube Notifier

A selfhosted YouTube feed bot for Discord. Basically, this bot keeps you and your friends up-to-date with everything that's happening on YouTube. Or, if you are a YouTuber or YouTube livestreamer yourself, and like to forget to promote yourself like I do, this bot takes care of that too.

### Features
- Multi YouTuber support (you can add as many as you want)
- Multi Discord channel support, so you can push the update feed in more than one server or channel at a time!
- Livestream support
- Custom messages for user uploads and livestreams!
     - Support for custom messages per channel!
- Easy yaml configuration file (config.yml)

### Requirements
- [Python 3.5](https://www.python.org/downloads/release/python-354/)
- Microsoft Windows, **I do not have Linux and all the launchers are done in batch**
(The bot *should in theory* still run just fine on Linux in a terminal, you would have to install the requirements manualy, though. I do **NOT** know if you need anything else for it to work, though.)
- [Discord.py](https://github.com/Rapptz/discord.py)
- [PyYaml](https://github.com/yaml/pyyaml)
- Google API Key (with YouTube Data API v3 activated), Tutorial in "**Preparation**"
- Registered Discord bot, Tutorial in "**Preparation**"

### Preparation
- **1.)** Install [Python 3.5](https://www.python.org/downloads/release/python-354/), and make sure it is included to your PATH.
- **2.)** In order to obtain an Google API Key (with YouTube Data API v3 activated) follow the Steps 1-3 [here](https://developers.google.com/youtube/v3/getting-started) and then generate a key for the API. This key will later on go to the config file of the bot.
- **3.)** Set up a discord bot, get the token and invite the bot to your server, by following [this guide](https://github.com/reactiflux/discord-irc/wiki/Creating-a-discord-bot-&-getting-a-token). The bot token will later on go to the config file of the bot.
- **4.)** You need to enable developer mode in your discord client to obtain the channel ID's you want the feed to appear on. Do so by going to your **User settings** -> **Appearance** -> Tick **"Developer Mode"** in the **ADVANCED** tab.
- **5.)** Obtain the channel ID(s) by right clicking the channel and then clicking **"Copy ID"**.
- **6.)** Obtain a user ID by right clicking the username and then clicking **"Copy ID"** (optional).
- **7.)** Get the YouTube channel ID(s). This is done in 2 ways:
     - Visit the YouTube channel and then copy the channel from the URL, for example:
       - Going to LinusTechTips gives you this URL in the URL bar of your browser: https://www.youtube.com/channel/UCXuqSBlHAE6Xw-yeJA0Tunw
       - The channel ID in that case is "UCXuqSBlHAE6Xw-yeJA0Tunw". Copy it.
     - Some YouTubers hide their channel ID completely and only show their username. In order to obtain the channel ID for them, we have to use this external site: http://johnnythetank.github.io/youtube-channel-name-converter/
       - e.g. entering "PewDiePie" into the "Youtube username" field will return "UC-lHJZR3Gqxm24_Vd_AJ5Yw". this is the one you want to copy.

### Configuration

Configuration is done by editing the config.yaml file. I would suggest using an editor like [Notepad++](https://notepad-plus-plus.org/) to edit the file.

- **In the first section in "connection" you will have to enter your YouTube v3 API Key that you have obtained earlier in Step #2 of Preparation.** Just copy and paste it into the field, so that this:
```
        Google API key: # YouTube v3 API Key
```

Will look like something like this:

```
        Google API key: 4P9nlidzQdMCxCzDymrUDpNwapMQ5jqC # YouTube v3 API Key
```

- **Then you need to provide your discord bot token you have obtained in Step #3 in Preparation.** Again, just copy and paste it, so that this:
```
        Discord bot token: # Discord bot token
```

Becomes something like this:
```
        Discord bot token: 7PGNyakySQu8ZH0T3Y7EDldSnHKlOGbL.SFTM7Zq38J-aDR2pflmUS # Discord bot token
```

- **You can specify the time period in minutes the bot will check the YouTube channels for new content. I do not recommend going lower than 5 minutes though, because your daily use of queries is limited and can be used up very quickly that way. Just change the "5" to whatever you desire.**
```
        Ping Every x Minutes: 5 # at least 5 minutes should be ok, anything lower not recommended, because the API traffic will be used up very quickly otherwise.
```

- **I have included 2 Discord channelID placeholders as an example in the config:**
```
        0:
            channelID: # Discord channel ID
        1:
            channelID: # Discord channel ID
```

You can expand those further by copying it and incrementing the number correspondingly. In this example 4:
```
        0:
            channelID: # Discord channel ID
        1:
            channelID: # Discord channel ID
        2:
            channelID: # Discord channel ID
        3:
            channelID: # Discord channel ID
```

Then you need to provide your discord channel ID(s) you have obtained in Step #5 in **Preparation**. Again, just copy and paste it:
```
        0:
            channelID: 3C2DCFC6DCA9761B # Discord channel ID
        1:
            channelID: 69387236D19A2C12 # Discord channel ID
```
**IMPORTANT:** if you only use **1** channel, you need to delete all other entries:
```
        0:
            channelID: 3C2DCFC6DCA9761B # Discord channel ID
```
- **Now you can specify the YouTubers that you want to push on your discord. Again, I have included placeholders for 2 channels as an example**:
```
        0:
            name: # Name that will be displayed in discord, mentions can be used with <@DiscordUserID>
            channelID: # YouTube Channel ID
        1:
            name: # Name that will be displayed in discord, mentions can be used with <@DiscordUserID>
            channelID: # YouTube Channel ID
```

Again, you can expand them by copying and incrementing accordingly. In this example 4:
```
        0:
            name: # Name that will be displayed in discord, mentions can be used with <@DiscordUserID>
            channelID: # YouTube Channel ID
        1:
            name: # Name that will be displayed in discord, mentions can be used with <@DiscordUserID>
            channelID: # YouTube Channel ID
        2:
            name: # Name that will be displayed in discord, mentions can be used with <@DiscordUserID>
            channelID: # YouTube Channel ID
        3:
            name: # Name that will be displayed in discord, mentions can be used with <@DiscordUserID>
            channelID: # YouTube Channel ID
```

Then you need to provide your channel ID(s) you have obtained in Step #7 in **Preparation**. Again, just copy and paste it:
```
        0:
            name: # Name that will be displayed in discord, mentions can be used with <@DiscordUserID>
            channelID: UCXuqSBlHAE6Xw-yeJA0Tunw # YouTube Channel ID
        1:
            name: # Name that will be displayed in discord, mentions can be used with <@DiscordUserID>
            channelID: UC-lHJZR3Gqxm24_Vd_AJ5Yw # YouTube Channel ID
```

And then provide a name for them. Note, this name is displayed on discord:
```
        0:
            name: LinusTechTips # Name that will be displayed in discord, mentions can be used with <@DiscordUserID>
            channelID: UCXuqSBlHAE6Xw-yeJA0Tunw # YouTube Channel ID
        1:
            name: PewDiePie # Name that will be displayed in discord, mentions can be used with <@DiscordUserID>
            channelID: UC-lHJZR3Gqxm24_Vd_AJ5Yw # YouTube Channel ID
```

Useful if you are a YouTuber yourself and want to automaticaly promote yourself: You can @mention yourself instead of giving a static name by typing <@DiscordUserID> (Replace DiscordUserID with your actual discord user ID you obtained in Step #6 of **Preparation**):
```
        0:
            name: <@32C6E424B5212> # Name that will be displayed in discord, mentions can be used with <@DiscordUserID>
            channelID: UCXuqSBlHAE6Xw-yeJA0Tunw # YouTube Channel ID
        1:
            name: <@7E169455DF2EC> # Name that will be displayed in discord, mentions can be used with <@DiscordUserID>
            channelID: UC-lHJZR3Gqxm24_Vd_AJ5Yw # YouTube Channel ID
```

**AGAIN, IMPORTANT:** if you only use **1** channel, you need to delete all other entries:
```
        0:
            name: LinusTechTips # Name that will be displayed in discord, mentions can be used with <@DiscordUserID>
            channelID: UCXuqSBlHAE6Xw-yeJA0Tunw # YouTube Channel ID
```

- **You can have custom messages for when a user uploads something or is currently livestreaming:**
```
        New video: ":film_frames: **{0} HAS UPLOADED A NEW VIDEO!** :film_frames:" # Message that appears when a YouTuber has uploaded a new video, user placeholder: {0}
        Livestream: ":red_circle: **{0} IS LIVESTREAMING NOW!** :red_circle:" # Message that appears when a YouTuber is livestreaming, user placeholder: {0}
```
- Make sure that your message is quoted (""). The following parameters can be used:
     - {0}
       - Name you specified in the YouTubers configuration
     - @everyone
       - Mention @everyone on Discord
     - <@DiscordUserID>
       - Mention a specific user on discord, ID can be obtained like described in Step #6 in **Preparation**.
     - :EmojiName:
       - In my example configuration file, I am using emoji's like :clapper: and :red_circle:. You can use all the emoji's with :EmojiName:. Emoji names can be obtained by clicking on the emoji symbol on the right in the Discord textchat, and a mouseover will reveal the plain text that you need to enter.

### Installation
Make sure you have Python 3.5 installed.
Then run the file **update_deps.bat** by double clicking.
This should automaticaly install all the python requirements you will need for this bot to function.
Aaaand.. that's all, you are ready to run the bot now.

### Running
Run the bot by opening the runbot.bat file.
