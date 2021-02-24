import pymem
import pymem.process
import keyboard
import time
import re, sys
from Offsets import *
sys.path.insert(1, "classes/")
from features_reads import read
import features_check

class chams_reset() :
    def __init__(self) :
        self.pm = pymem.Pymem("csgo.exe")
        self.base_client = pymem.process.module_from_name(self.pm.process_handle, "client.dll").lpBaseOfDll
        self.base_engine = pymem.process.module_from_name(self.pm.process_handle, "engine.dll").lpBaseOfDll
        self.dye_em()

    def get_class_id(self, entity):
        buffer = self.pm.read_int(entity + 8)
        buffer = self.pm.read_int(buffer + 2 * 4)
        buffer = self.pm.read_int(buffer + 1)
        return self.pm.read_int(buffer + 20)

    def get_entity_team(self, entity):
        return self.pm.read_int(entity + m_iTeamNum)

    def dye_em(self):
        glowmax = self.pm.read_int(self.base_client + dwGlowObjectManager + 4)
        glow_object = self.pm.read_int(self.base_client + dwGlowObjectManager)
        local_player = self.pm.read_int(self.base_client + dwLocalPlayer)

        read("chams")

        while not features_check.check.chams_active :

            read("chams")

            for i in range(glowmax):
                try:
                    entity = self.pm.read_int(glow_object + 56 * i)
                    if self.get_class_id(entity) == 40:
                        entity_team = self.get_entity_team(entity)

                        if entity_team != 0 and entity != local_player:

                            self.pm.write_uchar(entity + 112, 255)
                            self.pm.write_uchar(entity + 113, 255)
                            self.pm.write_uchar(entity + 114, 255)


                        b = 0
                        pointer = self.pm.read_int(self.base_engine + model_ambient_min - 44)
                        xored = b ^ pointer
                        self.pm.write_int(self.base_engine + model_ambient_min, xored)

                except :
                    pass
            
            return
        
        self.pm.close_process()