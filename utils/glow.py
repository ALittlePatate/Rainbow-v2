import pymem
import pymem.process
import time
import ctypes, sys
from Offsets import *
sys.path.insert(1, "classes/")
from features_reads import read
import features_check

class glow() :

    def __init__(self):

        try :
            pm = pymem.Pymem("csgo.exe")
        except Exception as e:
            print(e)
            MessageBox = ctypes.windll.user32.MessageBoxW
            MessageBox(None, 'Could not find the csgo.exe process !', 'Error', 16)
            return

        client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
        glow_manager = pm.read_int(client + dwGlowObjectManager)
        read("glow")

        while features_check.check.glow_active :
            
            try :
                read("glow")

                for i in range(1, 32):  # Entities 1-32 are reserved for players.
                    entity = pm.read_int(client + dwEntityList + i * 0x10)

                    if entity:
                        entity_team_id = pm.read_int(entity + m_iTeamNum)
                        player = pm.read_int(client + dwLocalPlayer)
                        player_team = pm.read_int(player + m_iTeamNum)
                        entity_hp = pm.read_int(entity + m_iHealth)
                        entity_glow = pm.read_int(entity + m_iGlowIndex)

                        if features_check.check.glow_health_based :

                            if entity_hp == 100 :
                                ennemies_color = [0, 1, 0, 1]
                                allies_color = [0, 1, 0, 1]
                            if entity_hp < 100 :
                                if entity_hp > 75:
                                    ennemies_color = [0.30, 1, 0, 1]
                                    allies_color = [0.30, 1, 0, 1]
                                if entity_hp < 75:
                                    ennemies_color = [0.70, 0.30, 0, 1]
                                    allies_color = [0.70, 0.30, 0, 1]
                                if entity_hp < 50 :
                                    ennemies_color = [1, 0.10, 0, 1]
                                    allies_color = [1, 0.10, 0, 1]
                                if entity_hp < 25 :
                                    ennemies_color = [1, 0, 0, 1]
                                    allies_color = [1, 0, 0, 1]
                                if entity_hp == 1 :
                                    ennemies_color = [1, 1, 1, 1]
                                    allies_color = [1, 1, 1, 1]

                        if not features_check.check.glow_health_based :
                            ennemies_color = self.rgba(features_check.check.ennemies_glow_color)
                            allies_color = self.rgba(features_check.check.allies_glow_color)
                    

                        if features_check.check.glow_allies :

                            if entity_team_id == player_team:  # Terrorist
                                pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(allies_color[0]))   # R 
                                pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(allies_color[1]))   # G
                                pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(allies_color[2]))   # B
                                pm.write_float(glow_manager + entity_glow * 0x38 + 0x14, float(allies_color[3]))  # Alpha
                                pm.write_int(glow_manager + entity_glow * 0x38 + 0x28, 1)           # Enable glow

                        if features_check.check.glow_ennemies :

                            if entity_team_id != player_team:  # Counter-terrorist
                                pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(ennemies_color[0]))   # R
                                pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(ennemies_color[1]))   # G
                                pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(ennemies_color[2]))   # B
                                pm.write_float(glow_manager + entity_glow * 0x38 + 0x14, float(ennemies_color[3]))  # Alpha
                                pm.write_int(glow_manager + entity_glow * 0x38 + 0x28, 1)           # Enable glow
                        
                        time.sleep(0.002)
                
            except :
                pass
        
        pm.close_process()

    def rgba(self, string) :
        string = str(string)
        
        return string.strip('][').split(', ')
