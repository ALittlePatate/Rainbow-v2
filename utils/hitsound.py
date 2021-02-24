import time
import ctypes, sys
from Offsets import *
sys.path.insert(1, "classes/")
from features_reads import read
import features_check
import pymem
import pymem.process
import winsound

class hitsound() :
    def __init__(self) :

        try :
            pm = pymem.Pymem("csgo.exe")
        except :
            MessageBox = ctypes.windll.user32.MessageBoxW
            MessageBox(None, 'Could not find the csgo.exe process !', 'Error', 16)
            return
        
        client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll

        read("misc")

        while features_check.check.hitsound :
            try :
                read("misc")

                player = pm.read_int(client + dwLocalPlayer)
                
                hitsound = pm.read_int(player + m_totalHitsOnServer)

                if hitsound > 0:
                    pm.write_int(player + m_totalHitsOnServer, 0)

                    winsound.PlaySound("sounds/"+features_check.check.sound, winsound.SND_FILENAME)

                time.sleep(0.1)
            except :
                pass
        
        pm.close_process()