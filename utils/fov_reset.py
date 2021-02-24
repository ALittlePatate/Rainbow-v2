import ctypes, sys
from Offsets import *
sys.path.insert(1, "classes/")
import pymem
import pymem.process

class fov_reset() :
    def __init__(self) :
        try :
            pm = pymem.Pymem("csgo.exe")
        except :
            MessageBox = ctypes.windll.user32.MessageBoxW
            MessageBox(None, 'Could not find the csgo.exe process !', 'Error', 16)
            return

        client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll

        player = pm.read_int(client + dwLocalPlayer)
        fov = player + m_iFOV

        pm.write_int(fov, 90)
        pm.close_process()