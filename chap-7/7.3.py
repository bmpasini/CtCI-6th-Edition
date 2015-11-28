# Design a musical Jukebox using OO principles.

class Song(object):
    def __init__(self, name, artist):
        self.name = name
        self.artist = artist
        self.genre = None
        self.file = None

# store info like name of album, songs (stored in variable called 'playlist', total length, number of tracks, year, etc.
class CD(object):
    pass

class Playlist(object):
    def __init__(self, songs):
        self.next_songs = list()
        if type(songs) is list:
            self.next_songs = songs # works like a queue: enqueue: append(), dequeue: pop(0)
        elif type(songs) is Song:
            self.next_songs.append(songs)

    def add_song(self, song):
        self.next_songs.append(song)

    def is_empty(self):
        return len(self.next_songs) == 0

class CDPlayer(object):
    def __init__(self, playlist):
        if playlist is type(CD):
            self.playlist = playlist.playlist
        else:
            self.playlist = playlist
        self.playing = None

    def play_next(self):
        if not self.playlist.is_empty():
            self.playing = self.playlist.next_songs.pop(0)
            self.playlist.next_songs.append(self.playing)
            self.playing.play()
        else:
            raise Exception("Select at least one song first!")

    def play_song(self, song):
        pass

    def start_playlist(self):
        self.play_next()

class Jukebox(object):
    def __init__(self, playlist):
        self.playlist = playlist
        self.playing = None

    




        



