import pyautogui
import numpy as np
import pickle
import time
SATANIC_KEY = "x"
with open("dota_item_image.txt", 'rb') as fil:
    SATANIC_IMAGE = pickle.load(fil)
SATANIC_SUM = SATANIC_IMAGE.sum()


def has_satanic(I):
    sh = I.shape
    return I[int(-sh[0]/8.3):int(-sh[0]/9.8), int(sh[1]/1.7)+110:int(-sh[1]/2.7)+95].sum() == SATANIC_SUM


def has_low_health(I):
    return not(get_health(I)[35, 220, 1] > 90)


def get_health(I):
    sh = I.shape
    return I[int(-sh[0]/15):, 1065:1692]


def activate_satanic():
    print("SATANIC ACTIVATED")
    pyautogui.write(SATANIC_KEY)


def mainloop():
    ss = np.array(pyautogui.screenshot())
    if has_satanic(ss) and has_low_health(ss):
        activate_satanic()
        time.sleep(5)
    time.sleep(0.5)


while True:
    mainloop()
