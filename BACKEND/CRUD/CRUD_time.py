from time import *
import threading

totalTimeToSeconds = {
    '15 minutos': 900,  # 15*60
    '30 minutos': 18000,  # 30*60
    '1 hora': 3600,  # 60*60
    '2 horas': 7200  # 120*60
}


def timer(usersTime):
    global totalTimeToSeconds
    totalSeconds = totalTimeToSeconds[usersTime[1]]
    totalSecondsCopy = totalSeconds
    for second in range(totalSecondsCopy, 0):
        totalSeconds -= 1
        sleep(1)
        print("EL USUARIO CON INDICE -> ", usersTime[0], " HA CUMPLIDO TIEMPO SOLICITADO")

def startTimerThreading():
    countdownThread = threading.Thread(target=timer)
    countdownThread.start()




