from winotify import Notification, audio
import time

while True:

    toast = Notification(app_id="IMPORTANT",
                         title="Message", msg="Hey Moyukh, Drink water",
                         duration="short", icon="C:\water.jpeg")
    toast.set_audio(audio.LoopingAlarm, loop=False)

    toast.show()
    time.sleep(10)