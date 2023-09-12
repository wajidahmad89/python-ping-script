import os
import time
from datetime import datetime



def pingFunction():
    
    
    hostname = "192.168.10.66" #example
    response = os.system("ping " + hostname)
    #print(response)
    if response == 512:
        file1 = open("myfile.txt", "a")
        file1.write("\n")
        file1.write(str(now))
        file1.close()
    time.sleep(60)
    
    
while True:
    
    now = datetime.now()
    pingFunction()


