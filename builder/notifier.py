from pydub.playback import play
from pydub import AudioSegment
import os

def show_notification(description):
  cwd = os.getcwd()
  os.system(f'notify-send -t 5000 -i {cwd}/assets/app.ico "Pratical Alarm" "{description}"')
  sound = AudioSegment.from_file('assets/tick.wav')
  play(sound)
