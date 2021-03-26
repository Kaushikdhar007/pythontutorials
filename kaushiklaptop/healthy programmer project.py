from datetime import datetime
from time import time

from pygame import mixer


# work_start_time='09:00:00'
# work_end_time='21:00:00'
# water_to_drink_total=3500
# water_to_drink_per_time=200
# no_of_glass=(water_to_drink_total/water_to_drink_per_time)

def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        input_of_user = input()
        if input_of_user == stopper:

            mixer.music.stop()
            break
def log_now(msg):
    with open("mylogs.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__ == '__main__':
    init_water= time()
    init_eye=time()
    init_exercise=time()
    time_interval_to_drink_water = 8

    time_interval_to_do_eye_exercise = 4

    time_interval_to_do_exercise = 13
    while (True):
       if time() - init_water > time_interval_to_drink_water:
         print("Water Drinking time. Enter 'drank' to stop the alarm.")
         musiconloop('drink.mp3', 'drank')
         init_water = time()
         log_now("Drank Water at")
         # with open("harry-ex.txt", "a") as op:
         #     op.write(str([str(datetime.datetime.now())]) + ": " + "DRANK" + "\n")
         print("successfully written")



       if time() - init_eye > time_interval_to_do_eye_exercise:
         print("Eye exercise time. Enter 'eyedone' to stop the alarm.")
         musiconloop('eyes.mp3', 'eyedone')
         init_eye = time()
         log_now("Eyes Relaxed at")
         # with open("harry-ex.txt", "a") as op:
         #     op.write(str([str(datetime.datetime.now())]) + ": " + "EYEDONE" + "\n")
         print("successfully written")



       if time() - init_exercise >time_interval_to_do_exercise:
         print("Physical Activity Time. Enter 'exdone' to stop the alarm.")
         musiconloop('exercise.mp3', 'exdone')
         init_exercise = time()
         log_now("Physical Activity done at")
         # with open("harry-ex.txt", "a") as op:
         #   op.write(str([str(datetime.datetime.now())]) + ": " + "exercise_done" + "\n")
         print("successfully written")





