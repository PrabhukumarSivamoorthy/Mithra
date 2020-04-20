#Global imports
from pygame import mixer

########################################################################
#@file        : Player.py
#@brief       : used to access the Audio player API
#@author      : Prabhukumar Sivamoorthy
#@date        : 12 MARCH 2020
#@copyright   : Prabhukumar Sivamoorthy
########################################################################
class AUDIOPLAYER:
    """"""

    #----------------------------------------------------------------------
    def __init__(self,filename ="",path=""):
        """Constructor"""
        self.fileName = filename if filename !="" else "sample.mp3"
        self.path = path #if path !="" else "C:\Users\7313024\Desktop\Experiment\Main"  
        mixer.init()
        mixer.music.load(self.path+self.fileName)
    
    #----------------------------------------------------------------------
    def loadSong(self,song="",path="C:\\Experiment\\\Mithra\\songs\\"):
        """"""
        if song == "":
            mixer.music.load(self.path+self.fileName)
        else:
            mixer.music.load(path+song+".mp3")
        
    #----------------------------------------------------------------------
    def play(self):
        """"""
        mixer.music.play() 
   
    #----------------------------------------------------------------------
    def pause(self):
        """"""
        mixer.music.pause()
        

    #----------------------------------------------------------------------
    def unPause(self):
        """"""
        mixer.music.unpause()
        

    #----------------------------------------------------------------------
    def stop(self):
        """"""
        mixer.music.stop()
        
    #----------------------------------------------------------------------
    def isRunning(self):
        """"""
        return mixer.music.get_busy()
    
########################################################################
class PLAYLIST:
    """"""
    #----------------------------------------------------------------------
    def __init__(self,day):
        """Constructor"""
        self.audioplayerobj = AUDIOPLAYER()
        self.SongList = self.fetchSongs(day)

    #----------------------------------------------------------------------
    def run(self):
        """"""
        i=0
        for song in self.SongList:
            i+=1
            self.audioplayerobj.loadSong(song,'C:\\Experiment\\\Mithra\\songs\\')
            self.audioplayerobj.play()
            while(self.audioplayerobj.isRunning() == True):            
                import time
                time.sleep(2)
            print("Completed")
            print(i)
            
    #----------------------------------------------------------------------
    def fetchSongs(self,day):
        """"""
        Songlist = []
        path= "C:\\Experiment\\Mithra\\config\\PlaylistConfig\\"+ day +"SongList.txt"
        f=open(path, "r")
        Contents = f.readlines()
        print (Contents)
        for song in Contents:
            Songlist.append(song.replace("\n",""))
        print (Songlist)
        f.close()
        return Songlist
    
  
    
    
    
    