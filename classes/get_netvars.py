from netvar_manager import NetvarsManager
import pymem
import pymem.process

class get_netvars() :
    def __init__(self) :
        pm = pymem.Pymem("csgo.exe")
        netvars_manager = NetvarsManager(pm)
        out_file = "classes/netvars.json"
        if out_file:
            with open(out_file, 'w+') as fp:
                netvars_manager.dump_netvars(
                    fp,
                    json_format=out_file.endswith('.json')
                )
        else:
            netvars_manager.dump_netvars()
        
        pm.close_process()