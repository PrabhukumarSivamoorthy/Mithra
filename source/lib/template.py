#Global imports
from email.mime.text import MIMEText
########################################################################
#@file        : Email.py
#@brief       : used to send and recevice email
#@author      : Prabhukumar Sivamoorthy
#@date        : 12 MARCH 2020
#@copyright   : Prabhukumar Sivamoorthy
########################################################################
class EMAIL:
    """"""

    #----------------------------------------------------------------------
    #@breif : Will establish a connection between the machine and mail server
    #         It creates the empty body message.
    #Reference: 
    #@Params: Default values are passed. it can be overwritten
    #
    def __init__(self,From='prabhukumar.sivamoorthy@wdc.com',Password="******"):
        """Constructor"""
        import smtplib
        from email.mime.text import MIMEText
        self.s = smtplib.SMTP('smtp-mail.outlook.com')
        print "connection stablished"
        self.s.starttls()
        self.s.ehlo_or_helo_if_needed()
        self.s.login(From, Password)
        self.From = From
        self.msg = MIMEText("EmailContent")
    
    #----------------------------------------------------------------------
    #@breif : Will send composed the email
    #         will appednd the TO email to the message
    #Reference: 
    #@Params: Default values are passed. it can be overwritten
    #    
    def send(self,To="prabhukumar.sivamoorthy@wdc.com"):
        """"""
        if self.msg['From'] != "":
            self.msg['To'] = To
            self.s.sendmail(self.msg['From'], To, self.msg.as_string())
        else:
            print "Constuct the message"
    
    #----------------------------------------------------------------------
    #@breif : Will disconnect the link between the machine and mail server
    #         
    def Quit(self):
        """"""
        self.s.quit()

    #----------------------------------------------------------------------
    #@breif : Will establish a connection between the machine and mail server
    #         It creates the empty body message.
    #Reference: 
    #@Params: Default values are passed. it can be overwritten
    #
    def constructMail(self, EmailContent ="This is a sample text"):
        """"""
        self.msg = MIMEText(EmailContent)
        self.msg['Subject'] = 'Test email from Prabhu '
        self.msg['From'] = self.From 




    