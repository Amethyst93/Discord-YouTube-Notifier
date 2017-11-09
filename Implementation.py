import urllib.request
import json
import codecs

class YouTuber:

    global GOOGLE_API
    global YouTubeName
    global PlaylistID
    global data
    global videosData
    global oldVideosData
    global userID
    global liveId
    global reader
    isID = False

    def __init__(self, GOOGLE_API_KEY, User, isID = False):

        self.reader = codecs.getreader('utf-8')

        self.GOOGLE_API = GOOGLE_API_KEY
        self.YouTubeName = User
        self.isID = isID

        if not self.isID:
            self.userID = self.getUserID()

        self.PlaylistID = self.setPlaylistID()
        self.data = self.getPlaylistData()
        self.videosData = self.getVideosData(self.data)

    def getUserID(self):

        if self.isID: return self.YouTubeName

        data = json.load(self.reader(urllib.request.urlopen('https://www.googleapis.com/youtube/v3/channels?part=id&forUsername={}&key={}'.format(
            self.YouTubeName, self.GOOGLE_API))))
        return data['items'][0]['id']

    def isUserLive(self):
        data = json.load(self.reader(urllib.request.urlopen('https://www.googleapis.com/youtube/v3/search?part=snippet&channelId={}&type=video&eventType=live&key={}'.format(self.getUserID(), self.GOOGLE_API))))
        if len(data['items']) == 0:
            return False
        if not len(data['items']) == 0:
            self.liveId = self.getUserLiveData()
        return True

    def getUserLiveData(self):
        data = json.load(self.reader(urllib.request.urlopen('https://www.googleapis.com/youtube/v3/search?part=snippet&channelId={}&type=video&eventType=live&key={}'.format(self.getUserID(), self.GOOGLE_API))))
        self.liveId = data['items'][0]['id']['videoId']
        return data['items'][0]['id']['videoId']

    def setPlaylistID(self):
        if self.isID:
            data = json.load(self.reader(urllib.request.urlopen('https://www.googleapis.com/youtube/v3/channels?part=contentDetails&id={}&key={}'.format(self.YouTubeName, self.GOOGLE_API))))
            return data['items'][0]['contentDetails']['relatedPlaylists']['uploads']

        data = json.load(self.reader(urllib.request.urlopen('https://www.googleapis.com/youtube/v3/channels?part=contentDetails&forUsername={}&key={}'.format(self.YouTubeName, self.GOOGLE_API))))
        return data['items'][0]['contentDetails']['relatedPlaylists']['uploads']

    def getPlaylistData(self):
        data = json.load(self.reader(urllib.request.urlopen('https://www.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=5&playlistId={}&key={}'.format(self.PlaylistID, self.GOOGLE_API))))
        return data

    def getVideosNrInPlaylist(self):
        i = 0
        for item in self.data['items']:
            i += 1
        return i

    def getVideosData(self, data):
        videosNr = 0
        for item in data['items']:
            videosNr += 1
        videosTitles = []
        videosLinks  = []
        i = 0
        while i < videosNr:
            videosTitles.append(data['items'][i]['snippet']['title'])
            videosLinks.append(data['items'][i]['snippet']['resourceId']['videoId'])
            i += 1
        videosData = []
        for item in videosTitles:
            tempList = []
            tempList.append(item)
            tempList.append(videosLinks[videosTitles.index(item)])
            videosData.append(tempList)
        return videosData

    def getVideoLink(self, videoID):
        return 'https://www.youtube.com/watch?v={}'.format(videoID)

    def update(self):
        self.oldVideosData = self.videosData
        self.data = self.getPlaylistData()
        self.videosData = self.getVideosData(self.data)
        return self.videosData

    def isNewVideo(self):
        if not self.oldVideosData:
            return False
        if (self.oldVideosData[0][0] == self.videosData[0][0]) and (self.oldVideosData[0][1] == self.videosData[0][1]):
            return False
        return True