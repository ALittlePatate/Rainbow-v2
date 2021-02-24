import keyboard
import pymem
import pymem.process
import time
import ctypes, sys
from random import *
from Offsets import *
from win32gui import GetWindowText, GetForegroundWindow
sys.path.insert(1, "classes/")
from features_reads import read
import features_check

class bhop_legit() :
    def __init__(self):
        try :
            pm = pymem.Pymem("csgo.exe")
        except :
            MessageBox = ctypes.windll.user32.MessageBoxW
            MessageBox(None, 'Could not find the csgo.exe process !', 'Error', 16)
            return

        client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll

        read("misc")
        while features_check.check.bhop_legit:
            
            try :
                read("misc")

                if not GetWindowText(GetForegroundWindow()) == "Counter-Strike: Global Offensive":
                    continue

                if keyboard.is_pressed("space"):
                    force_jump = client + dwForceJump
                    player = pm.read_int(client + dwLocalPlayer)
                    if player:
                        on_ground = pm.read_int(player + m_fFlags)
                        if on_ground and on_ground == 257:
                            a = randint(0,5)
                            time.sleep(a/100)
                            pm.write_int(force_jump, 5)
                            time.sleep(0.08)
                            pm.write_int(force_jump, 4)

                time.sleep(0.002)
            
            except :
                pass
        
        pm.close_process()