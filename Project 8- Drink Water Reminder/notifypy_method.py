from notifypy import Notify # pip install notify_py
import time

user = input("what it wants to be reminded about?")
time_user=float(input("in what amount of time, in minutes?"))
timeout = time_user*60
while(timeout):
    notification = Notify()
    notification.title=user
    notification.message = "Keep yourself hydrated, Moyukh"
    time.sleep(timeout)
    notification.send()