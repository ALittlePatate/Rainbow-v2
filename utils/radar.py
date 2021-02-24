import pymem
import pymem.process
import re
import ctypes, sys
sys.path.insert(1, "classes/")
from features_reads import read
import features_check

class radar() :
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
        address = client.lpBaseOfDll + re.search(rb'\x80\xB9.{5}\x74\x12\x8B\x41\x08',
                                                clientModule).start() + 6

        pm.write_uchar(address, 2)
        pm.close_process()