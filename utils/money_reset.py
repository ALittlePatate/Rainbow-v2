import pymem
import pymem.process
import re
import time
import ctypes, sys
sys.path.insert(1, "classes/")
from features_reads import read
import features_check

class money_reset() :
    def __init__(self) :
        try :
            pm = pymem.Pymem("csgo.exe")
        except :
            MessageBox = ctypes.windll.user32.MessageBoxW
            MessageBox(None, 'Could not find the csgo.exe process !', 'Error', 16)
            return

        
        client = pymem.process.module_from_name(pm.process_handle,
                                                'client.dll')

        clientModule = pm.read_bytes(client.lpBaseOfDll, client.SizeOfImage)
        address = client.lpBaseOfDll + re.search(rb'.\x0C\x5B\x5F\xB8\xFB\xFF\xFF\xFF',
                                                clientModule).start()


        pm.write_uchar(address, 0x75)
        pm.close_process()