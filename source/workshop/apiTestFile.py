#Global imports
import os
import datetime
# test api imports
#from PlayMusic.player import PLAYER
#from AutoEmail.mail import EMAIL
#from win32com.client import Dispatch
#from ModuleLib import ModuleLib
from lib.Modules import MODULES 
from lib.Text2Speech import TEXT2SPEECH
from tasks.DailyRoutineSongs import DailyRoutineSongs
########################################################################
#@file        : apitesefile.py
#@brief       : test all  API
#@author      : Prabhukumar Sivamoorthy
#@date        : 12 MARCH 2020
#@copyright   : Prabhukumar Sivamoorthy
########################################################################
class APPLICATION:
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        lib = MODULES()
        lib.requirementsCheck()       
        self.i=0
        
        
        

    def getCalendarEntries(days=1):
        """
        Returns calender entries for days default is 1
        """
        Outlook = Dispatch("Outlook.Application")
        ns = Outlook.GetNamespace("MAPI")
        appointments = ns.GetDefaultFolder(9).Items
        appointments.Sort("[Start]")
        appointments.IncludeRecurrences = "True"
        today = datetime.datetime.today()
        begin = today.date().strftime("%m/%d/%Y")
        tomorrow= datetime.timedelta(days=1)+today
        end = tomorrow.date().strftime("%m/%d/%Y")
        appointments = appointments.Restrict("[Start] >= '" +begin+ "' AND [END] <= '" +end+ "'")
        events={'Start':[],'Subject':[],'Duration':[]}
        for a in appointments:
            adate=datetime.datetime.fromtimestamp(int(a.Start))
            #print a.Start, a.Subject,a.Duration
            events['Start'].append(adate)
            events['Subject'].append(a.Subject)
            events['Duration'].append(a.Duration)
        return events    
    #----------------------------------------------------------------------
    def printdata(self):
        """"""
        self.i = self.i +1
        print("printing {}....".format(self.i))
    
        
    #----------------------------------------------------------------------
    def run(self):
        """"""      
      
        while True:
            task = DailyRoutineSongs()
            task.run()
       
        #testspeak = TEXT2SPEECH()
        #testspeak.speak(' Good Morning Sir')
        #testspeak.speak('Weather is 28 degree celsius now. it will raise upto 30 degree celsius in after noon. you have meeting at 8:30 am.')
        
        #testspeak.speak('Please, Get up from bed,SIR. and get Ready.')
        #testspeak.speak(' Can I make you a Coffee. ')
        
    # Get the calender events from outlook
        #print("test")
        #data = self.getCalendarEntries()
        #print data
        #import schedule
        #import time
        #schedule.every(10).seconds.do(self.printdata)
        #while True:
            #schedule.run_pending()
            #time.sleep(1)
        
        
    #Send an Email
        #Mail = EMAIL()
        #Mail.constructMail()
        #Mail.send()
        #Mail.Quit()
    #Play a song/Music
        #playerobj = PLAYER()
        #playerobj.play()
        #playerobj.pause()
        #playerobj.unPause()
        #playerobj.stop()        
            
