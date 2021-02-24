import time
import ctypes, sys
from Offsets import *
sys.path.insert(1, "classes/")
import pymem
import pymem.process
from features_reads import read
import features_check
import keyboard
import win32api

class rapidfire():

    def __init__(self) :

        read("rapid fire")
        key = self.get_key()

        while features_check.check.rapid_fire :
            try :
                read("rapid fire")
                key = self.get_key()

                if key :

                    while True :
                        ctypes.windll.user32.mouse_event(0x0002, 0, 0, 0, 0)
                        time.sleep(0.01)
                        ctypes.windll.user32.mouse_event(0x0004, 0, 0, 0, 0)
                        time.sleep(0.01)

                        key = self.get_key()
                        if not key :
                            break
            except :
                pass
    
    def get_key(self) :
        if "Button.right" in features_check.check.rapid_fire_key :
            key = win32api.GetKeyState(0x02)
            if key == -127 or key == -128 :
                key = True
            else :
                key = False
        elif "Button.left" in features_check.check.rapid_fire_key :
            key = win32api.GetKeyState(0x01)
            if key == -127 or key == -128 :
                key = True
            else :
                key = False
        elif "Button.middle" in features_check.check.rapid_fire_key :
            key = win32api.GetKeyState(0x04)
            if key == -127 or key == -128 :
                key = True
            else :
                key = False
            
        else :
            excpected_key = features_check.check.rapid_fire_key
            excpected_key = excpected_key.replace("Key.", "")
            key = keyboard.is_pressed(excpected_key)
        
        return key