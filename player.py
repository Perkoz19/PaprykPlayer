from pygame import mixer
import pygame
import random

MUSIC_ENDED = pygame.USEREVENT
pygame.mixer.music.set_endevent(MUSIC_ENDED)

class Player:
    def __init__(self):
        pygame.init()
        self.player = mixer.init()
        self.playlist = []
        self.paused = False
        self.set = []
        self.rand = False


    def musicAdd(self, pathtofile):
        self.playlist.append(pathtofile)

    def musicPlay(self, selected):
        if self.paused:
            mixer.music.unpause()
            self.paused = False
        else:
            song = self.playlist[selected]
            mixer.music.load(song)
            mixer.music.play()

    def musicPause(self):
        mixer.music.pause()
        self.paused = True

    def musicNext(self, selected):
        selected += 1
        self.musicPlay(self, selected)

    def getPlaylistLength(self):
        return len(self.playlist)

    def makeRandom(self):
        length = self.getPlaylistLength()
        for i in range(length):
            self.set.append(i)
        random.shuffle(self.set)

    def musicPlayRandom(self):
        le = self.getPlaylistLength()
        self.makeRandom()

        for s in self.set:
            # self.musicPlay(s)
            mixer.music.load(self.playlist[s])
            mixer.music.play()
            while mixer.music.get_busy():
                pygame.time.Clock().tick(5)
        # index = 0
        # self.musicPlay(self.set[index])
        # index += 1
        # while mixer.music.get_busy():
        #     pygame.time.Clock().tick(5)

        # while True:
        #     for event in pygame.event.get():
        #         if event.type == MUSIC_ENDED:
        #             index += 1
        #             if index == le:
        #                 index = 0
        #             self.musicPlay(self.set[index])
