import datetime
from threading import *
import time
from notifier import show_notification
from pydub.playback import play
from pydub import AudioSegment

t_alarm = None
stop_thread = False

def set_alarm(text_time, description):
    t_alarm=Thread(target=new_alarm, args=(text_time,description))
    t_alarm.daemon = True
    t_alarm.start()

def new_alarm(text_time,description):
    now = datetime.datetime.now()
    hour = datetime.datetime.strptime(text_time, '%H:%M:%S').hour
    minute = datetime.datetime.strptime(text_time, '%H:%M:%S').minute
    second = datetime.datetime.strptime(text_time, '%H:%M:%S').second
    time_alarm = now.replace(hour=hour,minute=minute,second=second)
    if now>time_alarm:
      time_alarm = time_alarm.replace(day=now.day+1)
    while True:
        if stop_thread:
          break
        time.sleep(1)
        current_time = datetime.datetime.now()
        if current_time>time_alarm:
            hour_alarm = time_alarm.strftime("%H:%M:%S")
            show_notification(f"{hour_alarm} - {description}")
            sound = AudioSegment.from_file('assets/alarm.mp3')
            play(sound)
            break