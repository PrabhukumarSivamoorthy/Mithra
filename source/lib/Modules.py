#Global imports
import os

########################################################################
#@file        : Modules.py
#@brief       : To add required modules
#@author      : Prabhukumar Sivamoorthy
#@date        : 12 MARCH 2020
#@copyright   : Prabhukumar Sivamoorthy
########################################################################
class MODULES:
    """"""
    #----------------------------------------------------------------------
    #@breif: Constructor. To make sure it has lastesr version of PIP.
    #
    def __init__(self):
        """Constructor"""
        excCmd = 'python -m pip install --upgrade pip'
        os.system(excCmd)
    
    #----------------------------------------------------------------------
    #@breif: This Method will run the pip install command based on the os
    #        Since , Pip install will vary based on the Operation system
    #        Currently it applicable for windows and Rasbian
    #Params: ModuleName
    #
    def pipInstall(self,ModuleName):
        """"""
        excCmd = 'python -m pip install '+ ModuleName
        os.system(excCmd)        

    #----------------------------------------------------------------------
    #@breif: Will access the list of required moudles from the txt file
    #        install them, if its is not availble in the machine
    #
    def requirementsCheck(self):
        """"""
        RequiredModule=['playsound','pypiwin32','schedule','pyttsx3']
        for module in RequiredModule:
            self.pipInstall(module)