from datetime import datetime
from pygame import mixer
from time import time


def musicOnLoop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play(loops=1000)
    while True:
        a = input()
        mixer.music.load(file)
        mixer.music.play()
        if a == stopper:
            mixer.music.stop()
            break


def logNow(msg):
    with open("log.txt", "rt") as f:
        data = f.read()
    with open("log.txt", "wt") as f:
        f.write(f" {data}\n"
                f"{msg} {datetime.now()}")


if __name__ == '__main__':
    # musicOnLoop("water.mp3", "stop")
    init_water = time()
    init_eyes = time()
    init_exercise = time()
#     We should drink water every 40 minutes
    water_sec = 60*40
#     Eyes should be given rest every 30 minutes
    eyes_sec = 60*30
#     Exercise should be done every 2 Hours
    exercise_sec = 60*60*2 
    while True:
        if time() - init_water > water_sec:
            print("Kindly Drink some water in order to be Hydrated\n"
                  "If drank, then write 'drank' on the console : ")
            musicOnLoop("water.mp3", "drank")
            init_water = time()
            logNow("Drank water at ")

        if time() - init_eyes > eyes_sec:
            print("Kindly give some rest to you Eyes\n"
                  "If rest is given, then write 'done' on the console : ")
            musicOnLoop("eyes.mp3", "done")
            init_eyes = time()
            logNow("Eyes given rest at ")

        if time() - init_exercise > exercise_sec:
            print("Kindly do some exercise in order to be fit\n"
                  "If you have completed the fitness, then write 'done' on the console : ")
            musicOnLoop("exercise.mp3", "done")
            init_exercise = time()
            logNow("Exercised at ")





















