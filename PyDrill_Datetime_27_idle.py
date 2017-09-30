import datetime
from datetime import timedelta

now = datetime.datetime.now().time()
NYnow = datetime.datetime.now() + datetime.timedelta(hours=3)
LNnow = datetime.datetime.now() + datetime.timedelta(hours=8)

def start():
    Portland()
    POC()
    NewYork()
    NYOC()
    London()
    LNOC()
    
    
def Portland():
    print ("Current local time in Portland, OR is {}").format(now.strftime('%H:%M:%S'))
def POC():
    if 21 > now.hour >= 9:
        print ("The Portland Branch is Open")
    else:
        print("Portland Branch is Closed")
        
def NewYork():
    print ("\nCurrent local time in New York, NY is {}").format(NYnow.strftime('%H:%M:%S'))
def NYOC():
    if 21 > NYnow.hour >= 9:
        print ("The New York Branch is Open")
    else:
        print("New York Branch is Closed")

def London():
    print ("\nCurrent local time in London, UK is {}").format(LNnow.strftime('%H:%M:%S'))
def LNOC():
    if 21 > LNnow.hour >= 9:
        print ("The London Branch is Open")
    else:
        print("The London Branch is Closed")
           

























if __name__ == "__main__":
    start()
