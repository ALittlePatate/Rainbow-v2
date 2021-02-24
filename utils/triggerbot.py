import pymem
import pymem.process
import time
import ctypes, sys
from Offsets import *
sys.path.insert(1, "classes/")
from features_reads import read
from math import *
import features_check
import keyboard
import win32api
from win32gui import GetWindowText, GetForegroundWindow

class triggerbot() :
    def __init__(self):

        try :
            pm = pymem.Pymem("csgo.exe")
        except :
            MessageBox = ctypes.windll.user32.MessageBoxW
            MessageBox(None, 'Could not find the csgo.exe process !', 'Error', 16)
            return

        client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
        engine = pymem.process.module_from_name(pm.process_handle, "engine.dll").lpBaseOfDll


        read("triggerbot")
        delay = features_check.check.t_delay
        key = self.get_key()

        while features_check.check.triggerbot :
            
            read("triggerbot")
            delay = features_check.check.t_delay
            key = self.get_key()

            if not GetWindowText(GetForegroundWindow()) == "Counter-Strike: Global Offensive":
                continue
            
            if key :

                try :
                    key = self.get_key()

                    player = pm.read_int(client + dwLocalPlayer)
                    entity_id = pm.read_int(player + m_iCrosshairId)
                    entity = pm.read_int(client + dwEntityList + (entity_id - 1) * 0x10)

                    entity_team = pm.read_int(entity + m_iTeamNum)
                    player_team = pm.read_int(player + m_iTeamNum)

                    if entity_id > 0 and entity_id <= 64 and player_team != entity_team:
                        if delay == 0 :
                            time.sleep(0)
                        else :
                            time.sleep(delay/1000)
                        pm.write_int(client + dwForceAttack, 6)

                    time.sleep(0.006)
                except :
                    pass
        
        pm.close_process()
    
    def get_key(self) :
        if "Button.right" in features_check.check.triggerbot_key :
            key = win32api.GetKeyState(0x02)
            if key == -127 or key == -128 :
                key = True
            else :
                key = False
        elif "Button.left" in features_check.check.triggerbot_key :
            key = win32api.GetKeyState(0x01)
            if key == -127 or key == -128 :
                key = True
            else :
                key = False
        elif "Button.middle" in features_check.check.triggerbot_key :
            key = win32api.GetKeyState(0x04)
            if key == -127 or key == -128 :
                key = True
            else :
                key = False
            
        else :
            excpected_key = features_check.check.triggerbot_key
            excpected_key = excpected_key.replace("Key.", "")
            key = keyboard.is_pressed(excpected_key)
        
        return key