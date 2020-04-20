#Global imports

########################################################################
#@file        : Text2Speech.py
#@brief       : used to convert Text into speech
#@author      : Prabhukumar Sivamoorthy
#@date        : 20 MARCH 2020
#@copyright   : Prabhukumar Sivamoorthy
########################################################################
class TEXT2SPEECH:
    """"""

    #----------------------------------------------------------------------
    #@breif : Will establish a connection between the machine and mail server
    #         It creates the empty body message.
    #Reference: 
    #@Params: Default values are passed. it can be overwritten
    #
    def __init__(self):
        """Constructor"""
        import pyttsx3
        self.engine =pyttsx3.init('sapi5')
        self.voices  = self.engine.getProperty('voices')
        
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('voice',self.voices[2].id)
        self.engine.setProperty('volume', 1)
        for voice in self.voices:
            print ("Voice : {}",format(voice.name))
            print ("id : {}",format(voice.id))
            print ("languvage : {}",format(voice.languages))    
            print ("gender : {}",format(voice.gender))
            print ("\n")
        
        

    #----------------------------------------------------------------------
    #@breif : Will send composed the email
    #         will appednd the TO email to the message
    #Reference: 
    #@Params: Default values are passed. it can be overwritten
    #    
    def speak(self,text):
        """"""
        self.engine.say(text)
        self.engine.runAndWait()

  