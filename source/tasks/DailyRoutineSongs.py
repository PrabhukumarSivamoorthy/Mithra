#Global imports
import datetime
# test api imports

from lib.Players import PLAYLIST
########################################################################
#@file        : DailyRoutineSongs.py
#@brief       : To play the list of songs form the
#@author      : Prabhukumar Sivamoorthy
#@date        : 12 MARCH 2020
#@copyright   : Prabhukumar Sivamoorthy
########################################################################
class DailyRoutineSongs:
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""    
        self.SongList = ['sample','sample']
        self.DayoftheWeek ={0:"Sunday", 1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thrusday", 5:"Friday", 6:"Saturday"} 
        

    def run(self):
        """"""
        #Get Today's date
        now = datetime.datetime.now()
        
        #Get Today's day of the week 
        Day = self.DayoftheWeek.get(int(now.strftime("%w"))) # can be improvised
        
        if now.strftime("%p")=="AM":
            
            #Wakeup Songs
            if int(now.strftime("%I"))== 5 and (int(now.strftime("%M"))>=30 and int(now.strftime("%M"))<=59 ):  
                
                #Play the songs based on the day
                EarlyMoningSongs = PLAYLIST(Day)
        
                #run the playlist
                EarlyMoningSongs.run()
                
            if int(now.strftime("%I"))== 6 and (int(now.strftime("%M"))>=00 and int(now.strftime("%M"))<=30 ):
                
                #To Good moring by Mithra.
                print("Good Morining")
                
        else:
            
            #Yoga Om chating songs.
            if (int(now.strftime("%I"))== 10 and (int(now.strftime("%M"))>=30 and int(now.strftime("%M"))<=59)) or (int(now.strftime("%I"))== 11 and (int(now.strftime("%M"))>=00 and int(now.strftime("%M"))<=29)):
                
                #Play the songs based on the day
                YogaPlaylist = PLAYLIST("Yoga")
                
                #run the playlist
                YogaPlaylist.run()
                
            #Stress night cricket music 
            if int(now.strftime("%I"))== 11 and (int(now.strftime("%M"))>=30 and int(now.strftime("%M"))<=59 ):
                
                #Play the songs based on the day
                NightSleepPlaylist = PLAYLIST("NightSleep")
                
                #run the playlist
                NightSleepPlaylist.run()
                
                
        
        
        
        
        
        #print("{}".format(Mondaysongsplaylist.listOfSongs()))
        #Mondaysongsplaylist.run()
    #Play a song/Musiu
        #MondayMorningSongsobj = AUDIOPLAYER()
        #for song in self.SongList:
            #MondayMorningSongsobj.loadSong(song,'C:\\songs\\')
            #MondayMorningSongsobj.play()
            #while(MondayMorningSongsobj.isRunning() == True):            
                #import time
                #time.sleep(2)
            #print("Completed")
        
        #playerobj.pause()
        #playerobj.unPause()
        #playerobj.stop()        
            
