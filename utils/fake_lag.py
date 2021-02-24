import time
import ctypes, sys
from Offsets import *
sys.path.insert(1, "classes/")
import pymem
import pymem.process
from features_reads import read
import features_check

class fake_lag() :

    def __init__(self) :
        
        try :
            pm = pymem.Pymem("csgo.exe")
        except :
            MessageBox = ctypes.windll.user32.MessageBoxW
            MessageBox(None, 'Could not find the csgo.exe process !', 'Error', 16)
            return
        
        engine = pymem.process.module_from_name(pm.process_handle, "engine.dll").lpBaseOfDll
        read("misc")

        while features_check.check.fake_lag :
            try :
                read("misc")

                pm.write_float(engine + 0x38E6AC4, features_check.check.fake_lag_value/2)
            except :
                pass
        
        pm.close_process()