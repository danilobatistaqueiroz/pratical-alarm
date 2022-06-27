import datetime
from datetime import timedelta

def add_sec(time,qtd):
    now = datetime.datetime.strptime(time, '%H:%M:%S')
    return add_time(now,0,0,qtd)

def add_min(time,qtd):
    now = datetime.datetime.strptime(time, '%H:%M:%S')
    return add_time(now,0,qtd,0)

def add_hour(time,qtd):
    now = datetime.datetime.strptime(time, '%H:%M:%S')
    return add_time(now,qtd,0,0)

def next_hour():
    now = datetime.datetime.now()
    now = now.replace(minute=0, second=0, microsecond=0)
    return add_time(now,1,0,0)

def set_now():
    now = datetime.datetime.now()
    return add_time(now,0,0,0)

def add_time(time,qtd_h,qtd_m,qtd_s):
  new_time = time + timedelta(hours=qtd_h)
  new_time = new_time + timedelta(minutes=qtd_m)
  new_time = new_time + timedelta(seconds=qtd_s)
  return new_time.strftime("%H:%M:%S")