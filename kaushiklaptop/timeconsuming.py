from gtts import gTTS
def convert_to_audio(text):
     my_audio = gTTS(text)
     my_audio.save('hello2.mp3')

convert_to_audio(" abbe tor babar nam vulia debo. tor ma k bol j tor baba k. dekhbi bol lo kaushik dhar")

# from pygame import mixer
#
# mixer.init()
# mixer.music.load('hello.mp3')
# mixer.music.play()
# from playsound import playsound
# playsound('D:\sem6\drink.mp3')
# playsound('D:\sem6\eyes.mp3')
# playsound('D:\sem6\exercise.mp3')
# import multiprocessing
# from playsound import playsound
#
# p = multiprocessing.Process(playsound('D:\sem6\drink.mp3'))
# p.start()
#
# i=input("press ENTER to stop playback")
# p.join()

# target=playsound, args=("drink.mp3",)
import time
from pygame import mixer

def play(soundfile, duration_secs):
    """Play a soundfile for a configurable duration"""

    mixer.init()
    mixer.music.load(soundfile)
    mixer.music.play()
    time.sleep(duration_secs)
    mixer.music.stop()
    mixer.quit()

# Play for 5 seconds
play('hello2.mp3', 20)