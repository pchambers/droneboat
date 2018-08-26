from gps import *

import time
import threading
 
gpsd = None
class GpsPoller(threading.Thread):
   def __init__(self):
       threading.Thread.__init__(self)
       global gpsd
       gpsd=gps(mode=WATCH_ENABLE)
       self.current_value = None
       self.running = True
   def run(self):
       global gpsd
       while gpsp.running:
           gpsd.next()
if  __name__ == "__main__":
   
   gpsp=GpsPoller()
    
   try:
       gpsp.start()
        
       while True:
           with open("locations.csv","w") as f:
               f.write(str(gpsd.fix.longitude) + "," + str(gpsd.fix.latitude) + "\n") 
            
           time.sleep(30)
       
   except(KeyboardInterrupt,SystemExit):
       gpsp.running = False
       gpsp.join()
