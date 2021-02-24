import time
import ctypes, sys
from Offsets import *
sys.path.insert(1, "classes/")
import pymem
import pymem.process
from features_reads import read
import features_check

class fov() :
    def __init__(self) :
        try :
            pm = pymem.Pymem("csgo.exe")
        except :
            MessageBox = ctypes.windll.user32.MessageBoxW
            MessageBox(None, 'Could not find the csgo.exe process !', 'Error', 16)
            return

        client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
        read("misc")

        inputFOV = int(round(features_check.check.fov_value, 0))

        player = pm.read_int(client + dwLocalPlayer)

        while features_check.check.fov :
            read("misc")
            inputFOV = int(round(features_check.check.fov_value, 0))

            fov = player + m_iFOV
            pm.write_int(fov, inputFOV)
        
        pm.close_process()