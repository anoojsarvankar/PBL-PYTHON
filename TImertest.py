import threading
import time

def countdown():
    when_to_stop = 3
    temp=when_to_stop
    while temp > 0:
        time_left=temp
        print(time_left,'\r',end="")
        time.sleep(1)
        temp-=1
countdown()