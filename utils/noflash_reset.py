import pymem
import pymem.process
import time
import ctypes, sys
import warnings
warnings.simplefilter("ignore")
from Offsets import *
sys.path.insert(1, "classes/")
from features_reads import read
import features_check

class noflash_reset() :
    def __init__(self):
        try :
            pm = pymem.Pymem("csgo.exe")
        except :
            MessageBox = ctypes.windll.user32.MessageBoxW
            MessageBox(None, 'Could not find the csgo.exe process !', 'Error', 16)
            return

        client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
        player = pm.read_int(client + dwLocalPlayer)
        flash_value = player + m_flFlashMaxAlpha

        read("misc")

        while not features_check.check.no_flash :
            try :
                read("misc")
                pm.write_float(flash_value, float(255))
                time.sleep(0.2)
            except :
                pass
        
        pm.close_process()