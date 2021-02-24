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

class thirdperson() :
    def __init__(self):
        try :
            pm_memory = pymem.Pymem("csgo.exe")
        except :
            MessageBox = ctypes.windll.user32.MessageBoxW
            MessageBox(None, 'Could not find the csgo.exe process !', 'Error', 16)
            return

        client = pymem.process.module_from_name(pm_memory.process_handle, "client.dll").lpBaseOfDll
        lcbase = pm_memory.read_int(client + dwLocalPlayer)
        fov = lcbase + m_iFOV

        read("misc")
        key = self.get_key()
        third_toggle = False

        while features_check.check.third_person :
            read("misc")
            key = self.get_key()

            if key :
                try :

                    if not third_toggle :
                        pm_memory.write_int(lcbase + m_iObserverMode, 1)
                        pm_memory.write_int(fov, 130)

                        third_toggle = True

                    elif third_toggle :
                        pm_memory.write_int(lcbase + m_iObserverMode, 0)
                        pm_memory.write_int(fov, 90)

                        third_toggle = False
                    
                    time.sleep(0.2)
                
                except :
                    pass
        
        pm.close_process()
                    
    def get_key(self) :
        if "Button.right" in features_check.check.thirdperson_key :
            key = win32api.GetKeyState(0x02)
            if key == -127 or key == -128 :
                key = True
            else :
                key = False
        elif "Button.left" in features_check.check.thirdperson_key :
            key = win32api.GetKeyState(0x01)
            if key == -127 or key == -128 :
                key = True
            else :
                key = False
        elif "Button.middle" in features_check.check.thirdperson_key :
            key = win32api.GetKeyState(0x04)
            if key == -127 or key == -128 :
                key = True
            else :
                key = False
            
        else :
            excpected_key = features_check.check.thirdperson_key
            excpected_key = excpected_key.replace("Key.", "")
            key = keyboard.is_pressed(excpected_key)
        
        return key