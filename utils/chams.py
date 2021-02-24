import pymem
import pymem.process
import keyboard
import time
import re, sys
from Offsets import *
sys.path.insert(1, "classes/")
from features_reads import read
import features_check

class chams() :
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
        first = True

        while features_check.check.chams_active :
            read("chams")

            local_player_team = self.get_entity_team(local_player)
            allies_color_rgba = self.rgba(features_check.check.allies_chams_color)
            ennemies_color_rgba = self.rgba(features_check.check.ennemies_chams_color)

            for i in range(glowmax):
                try:
                    entity = self.pm.read_int(glow_object + 56 * i)
                    if entity != 0 :
                        if self.get_class_id(entity) == 40:
                            entity_team = self.get_entity_team(entity)
                            entity_hp = self.pm.read_int(entity + m_iHealth)

                            if features_check.check.chams_health_based :
                                
                                if entity_hp == 100 :
                                    allies_color_rgba = self.rgba("[0, 1, 0, 1]")
                                    ennemies_color_rgba = self.rgba("[0, 1, 0, 1]")
                                if entity_hp < 100 :
                                    if entity_hp > 75:
                                        ennemies_color_rgba = self.rgba("[0.30, 1, 0, 1]")
                                        allies_color_rgba = self.rgba("[0.30, 1, 0, 1]")
                                    if entity_hp < 75:
                                        ennemies_color_rgba = self.rgba("[0.70, 0.30, 0, 1]")
                                        allies_color_rgba = self.rgba("[0.70, 0.30, 0, 1]")
                                    if entity_hp < 50 :
                                        ennemies_color_rgba = self.rgba("[1, 0.10, 0, 1]")
                                        allies_color_rgba = self.rgba("[1, 0.10, 0, 1]")
                                    if entity_hp < 25 :
                                        ennemies_color_rgba = self.rgba("[1, 0, 0, 1]")
                                        allies_color_rgba = self.rgba("[1, 0, 0, 1]")
                                    if entity_hp == 1 :
                                        ennemies_color_rgba = self.rgba("[1, 1, 1, 1]")
                                        allies_color_rgba = self.rgba("[1, 1, 1, 1]")

                            if features_check.check.chams_allies :
                                if entity_team == local_player_team and entity_team != 0 and entity != local_player:

                                    self.pm.write_uchar(entity + 112, allies_color_rgba[0])
                                    self.pm.write_uchar(entity + 113, allies_color_rgba[1])
                                    self.pm.write_uchar(entity + 114, allies_color_rgba[2])

                            if not features_check.check.chams_allies :
                                if entity_team == local_player_team and entity_team != 0 and entity != local_player:
                                    self.pm.write_uchar(entity + 112, 255)
                                    self.pm.write_uchar(entity + 113, 255)
                                    self.pm.write_uchar(entity + 114, 255)

                            if features_check.check.chams_ennemies :

                                if entity_team != local_player_team and entity_team != 0 and entity != local_player:

                                    self.pm.write_uchar(entity + 112, ennemies_color_rgba[0])
                                    self.pm.write_uchar(entity + 113, ennemies_color_rgba[1])
                                    self.pm.write_uchar(entity + 114, ennemies_color_rgba[2])
                            
                            if not features_check.check.chams_ennemies :
                                if entity_team != local_player_team and entity_team != 0 and entity != local_player:
                                    self.pm.write_uchar(entity + 112, 255)
                                    self.pm.write_uchar(entity + 113, 255)
                                    self.pm.write_uchar(entity + 114, 255)
                                    

                            if first == True :
                                b = 1084227584
                                
                                pointer = self.pm.read_int(self.base_engine + model_ambient_min - 44)
                                xored = b ^ pointer
                                self.pm.write_int(self.base_engine + model_ambient_min, xored)
                                first = False

                    time.sleep(0.002)
                    
                except Exception as e :
                    pass
        
        self.pm.close_process()
            
    
    def rgba(self, string) :
        string = str(string)
        string = string.strip('][').split(', ')

        string[0] = int(round((float(string[0])*255.0)/1.0, 0))
        string[1] = int(round((float(string[1])*255.0)/1.0, 0))
        string[2] = int(round((float(string[2])*255.0)/1.0, 0))

        return string