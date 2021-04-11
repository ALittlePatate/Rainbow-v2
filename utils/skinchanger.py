import ctypes, sys, os
import pymem
import requests
import keyboard
from itertools import repeat
from Offsets import *
from configparser import ConfigParser
sys.path.insert(1, "classes/")
from skin_id_dumper import main as skin_dump

class skinchanger_func() :

    def __init__(self):
        try :
            pm = pymem.Pymem("csgo.exe")
        except :
            MessageBox = ctypes.windll.user32.MessageBoxW
            MessageBox(None, 'Could not find the csgo.exe process !', 'Error', 16)
            return

        client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
        engine = pymem.process.module_from_name(pm.process_handle, "engine.dll").lpBaseOfDll

        engine_state = pm.read_int( engine + dwClientState )

        skin_dict, skin_list = skin_dump() #using skin_dict only
        
        weapons_id = {
            "AK47": 7,
            "AUG": 8,
            "FAMAS": 10,
            "Galil_AR": 13,
            "M4A1S": 60,
            "M4A4": 16,
            "SG_553": 39,
            "AWP": 9,
            "SSG_08": 40,
            "G3SG1": 11,
            "SCAR20": 38,
            "MAC10": 17,
            "MP7": 33,
            "MP9": 34,
            "PPBizon": 36,
            "P90": 19,
            "UMP45": 24,
            "MP5SD": 23,
            "MAG7": 27,
            "Nova": 35,
            "SawedOff": 29,
            "XM1014": 25,
            "Negev": 28,
            "M249": 14,
            "USPS": 61,
            "Desert_Eagle": 1,
            "Glock18": 4,
            "FiveSeven": 3,
            "P250": 36,
            "Tec9": 30,
            "P2000": 32,
            "R8_Revolver": 64,
            "CZ75Auto": 63,
            "Dual_Berettas": 2
        }

        self.config_p = ConfigParser()

        while 1 :
            self.config_last = config.read_last(self)

            self.config_p.read('configs/'+self.config_last)
            
            active_weapons = config.active_weapons(self)

            for weapon, skin in active_weapons.items() :
                fallbackpaint, seed, float_v, stattrack_y = int(skin_dict[skin]), self.config_p.getint('SKINCHANGER', weapon+"_se"), self.config_p.getfloat('SKINCHANGER', weapon+"_f"), self.config_p.getboolean('SKINCHANGER', weapon+"_st")

                local_player = pm.read_int( client + dwLocalPlayer )
                for _ in repeat(0,2000) :
                    for i in range(0, 8) :
                        my_weapons = pm.read_int( local_player + m_hMyWeapons + (i - 1) * 0x4 ) & 0xFFF
                        weapon_address = pm.read_int( client + dwEntityList + (my_weapons - 1) * 0x10 )
                        if weapon_address:
                            weapon_id_2 = pm.read_short(weapon_address + m_iItemDefinitionIndex)
                            if weapon_id_2 == weapons_id[weapon] :
                                weapon_owner = pm.read_int(weapon_address + m_OriginalOwnerXuidLow)
                                pm.write_int( weapon_address + m_iItemIDHigh, -1 )
                                pm.write_int( weapon_address + m_nFallbackPaintKit, fallbackpaint )
                                pm.write_int( weapon_address + m_iAccountID, weapon_owner )

                                if stattrack_y :
                                    stattrack_v = self.config_p.getint('SKINCHANGER', weapon+"_stv")
                                    pm.write_int( weapon_address + m_nFallbackStatTrak, stattrack_v )

                                pm.write_int( weapon_address + m_nFallbackSeed, seed )
                                pm.write_float( weapon_address + m_flFallbackWear, float_v)

                        if keyboard.is_pressed( "f6" ):
                            pm.write_int( engine_state + 0x174, -1 )

class config() :
    def read_last(self) :
        while True :   #If there is an error because we are writing the last config at the same time
            try :
                with open("configs/last/last.txt", "r") as f :
                    for line in f :
                        last = line

                return last
            except :
                pass

    def read_active_weapons(self) :

        all_weapons = {
            "AK47": self.config_p.get('SKINCHANGER', 'AK47'),
            "AUG": self.config_p.get('SKINCHANGER', 'AUG'),
            "AWP": self.config_p.get('SKINCHANGER', 'AWP'),
            "CZ75Auto": self.config_p.get('SKINCHANGER', 'CZ75Auto'),
            "Desert_Eagle": self.config_p.get('SKINCHANGER', 'Desert_Eagle'),
            "Dual_Berettas": self.config_p.get('SKINCHANGER', 'Dual_Berettas'),
            "FAMAS": self.config_p.get('SKINCHANGER', 'FAMAS'),
            "FiveSeven": self.config_p.get('SKINCHANGER', 'FiveSeven'),
            "G3SG1": self.config_p.get('SKINCHANGER', 'G3SG1'),
            "Galil_AR": self.config_p.get('SKINCHANGER', 'Galil_AR'),
            "Glock18": self.config_p.get('SKINCHANGER', 'Glock18'),
            "M249": self.config_p.get('SKINCHANGER', 'M249'),
            "M4A1S": self.config_p.get('SKINCHANGER', 'M4A1S'),
            "M4A4": self.config_p.get('SKINCHANGER', 'M4A4'),
            "MAC10": self.config_p.get('SKINCHANGER', 'MAC10'),
            "MAG7": self.config_p.get('SKINCHANGER', 'MAG7'),
            "MP5SD": self.config_p.get('SKINCHANGER', 'MP5SD'),
            "MP7": self.config_p.get('SKINCHANGER', 'MP7'),
            "MP9": self.config_p.get('SKINCHANGER', 'MP9'),
            "Negev": self.config_p.get('SKINCHANGER', 'Negev'),
            "Nova": self.config_p.get('SKINCHANGER', 'Nova'),
            "P2000": self.config_p.get('SKINCHANGER', 'P2000'),
            "P250": self.config_p.get('SKINCHANGER', 'P250'),
            "P90": self.config_p.get('SKINCHANGER', 'P90'),
            "PPBizon": self.config_p.get('SKINCHANGER', 'PPBizon'),
            "R8_Revolver": self.config_p.get('SKINCHANGER', 'R8_Revolver'),
            "SCAR20": self.config_p.get('SKINCHANGER', 'SCAR20'),
            "SG_553": self.config_p.get('SKINCHANGER', 'SG_553'),
            "SSG_08": self.config_p.get('SKINCHANGER', 'SSG_08'),
            "SawedOff": self.config_p.get('SKINCHANGER', 'SawedOff'),
            "Tec9": self.config_p.get('SKINCHANGER', 'Tec9'),
            "UMP45": self.config_p.get('SKINCHANGER', 'UMP45'),
            "USPS": self.config_p.get('SKINCHANGER', 'USPS'),
            "XM1014": self.config_p.get('SKINCHANGER', 'XM1014'),
        }

        return all_weapons

    def active_weapons(self) :
        all_weapons = config.read_active_weapons(self)

        active_weapons = {}
        for weapon, value in all_weapons.items():
            if value != "0" :
                active_weapons[weapon] = value
            
        return active_weapons