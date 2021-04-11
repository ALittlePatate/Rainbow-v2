import pymem
import ctypes, sys, os
from itertools import repeat
from Offsets import *
from configparser import ConfigParser
sys.path.insert(1, "classes/")
from skin_id_dumper import main as skin_dump

class knifechanger_func() :
    def __init__(self):
        self.config_p = ConfigParser()

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

        knife_ids = {
            "Gold knife" : 519,
            "Spectral knife" : 604,
            "Bayonet" : 612,
            "Classic knife" : 615,
            "Flip knife" : 618,
            "Gut knife" : 621,
            "Karambit" : 624,
            "M9 Bayonet" : 627,
            "Huntsman" : 630,
            "Falchion knife" : 633,
            "Bowie knife" : 636,
            "Butterfly knife" : 639,
            "Shadow daggers" : 642,
            "Cord knife" : 646,
            "Canis knife" : 649,
            "Ursus knife" : 652,
            "Navaja" : 655,
            "Nomad knife" : 658,
            "Stiletto knife" : 661,
            "Talon knife": 664,
            "Skeleton knife" : 667
        }

        knifeDefinitionIndex_dict = {
            "Gold knife" : 41,
            "Spectral knife" : 505,
            "Bayonet" : 500,
            "Classic knife" : 503,
            "Flip knife" : 505,
            "Gut knife" : 506,
            "Karambit" : 507,
            "M9 Bayonet" : 508,
            "Huntsman" : 509,
            "Falchion knife" : 512,
            "Bowie knife" : 514,
            "Butterfly knife" : 515,
            "Shadow daggers" : 516,
            "Paracord knife" : 517,
            "Survival knife" : 518,
            "Ursus knife" : 519,
            "Navaja" : 520,
            "Nomad knife" : 521,
            "Stiletto knife" : 522,
            "Talon knife": 523,
            "Skeleton knife" : 525
        }

        CtKnife = 522
        TKnife = 547
        cachedPlayer = 0
        modelIndex = 0
        entityQuality = 3

        b = 500
        while 1 :
            if b == 500 :
                knife_active = config.get_knife(self)

                knifeID, knifeDefinitionIndex, paintKit, fallbackwear, seed = int(knife_ids[knife_active["knife"]]), int(knifeDefinitionIndex_dict[knife_active["knife"]]), int(skin_dict[knife_active["knife_skin"]]), knife_active["knife_f"], knife_active["knife_se"]

                b = 0
            
            b = b + 1

            localPlayer = pm.read_uint(client + dwLocalPlayer)

            if localPlayer == 0:
                modelIndex = 0
                continue

            elif localPlayer != cachedPlayer:
                modelIndex = 0
                cachedPlayer = localPlayer
                
            if paintKit > 0 and modelIndex > 0 :

                for i in repeat(0, 8) :

                    currentWeapon = pm.read_uint(localPlayer + m_hMyWeapons + i * 0x04) & 0xfff
                    currentWeapon = pm.read_uint(client + dwEntityList + (currentWeapon - 1) * 0x10)
                    if currentWeapon == 0:continue

                    weaponID = pm.read_short(currentWeapon + m_iItemDefinitionIndex)

                    fallbackPaint = paintKit
                    if weaponID != 42 and weaponID != 59 and weaponID != knifeDefinitionIndex :continue

                    else:

                        pm.write_short(currentWeapon + m_iItemDefinitionIndex, knifeDefinitionIndex)
                        pm.write_uint(currentWeapon + m_nModelIndex, modelIndex)
                        pm.write_uint(currentWeapon + m_iViewModelIndex, modelIndex)
                        pm.write_int(currentWeapon + m_iEntityQuality, entityQuality)

                    pm.write_int(currentWeapon + m_iItemIDHigh, -1)
                    pm.write_uint(currentWeapon + m_nFallbackPaintKit, fallbackPaint)
                    pm.write_float(currentWeapon + m_flFallbackWear,fallbackwear)

                    if knife_active["knife_st"] :
                        stattrack_v = knife_active["knife_stv"]
                        pm.write_int( currentWeapon + m_nFallbackStatTrak, stattrack_v )
                    
                    pm.write_int( currentWeapon + m_nFallbackSeed, seed )


            for _ in repeat(None, 100) :
                ActiveWeapon = pm.read_int( localPlayer + m_hActiveWeapon) & 0xfff
                ActiveWeapon = pm.read_int( client + dwEntityList + (ActiveWeapon - 1) * 0x10 )

                if ActiveWeapon == 0:

                    continue

                weaponID = pm.read_short( ActiveWeapon + m_iItemDefinitionIndex )

                weaponViewModelId = pm.read_int( ActiveWeapon + m_iViewModelIndex )

                if weaponID == 42 and weaponViewModelId > 0:
                    modelIndex = weaponViewModelId + (knifeID - CtKnife)
                elif weaponID == 59 and weaponViewModelId > 0:
                    modelIndex = weaponViewModelId + (knifeID - TKnife)
                elif weaponID != knifeDefinitionIndex or modelIndex == 0 :
                    continue
                knifeViewModel = pm.read_uint( localPlayer + m_hViewModel ) & 0xfff
                knifeViewModel = pm.read_uint( client + dwEntityList + (knifeViewModel - 1) * 0x10 )

                if knifeViewModel == 0: continue
                pm.write_uint( knifeViewModel + m_nModelIndex, modelIndex)
                

class config() :
    def read_last(self) :
        while 1 :   #If there is an error because we are writing the last config at the same time
            try :
                with open("configs/last/last.txt", "r") as f :
                    for line in f :
                        last = line

                return last
            except :
                pass

    def get_knife(self) :
        self.config_last = config.read_last(self)
        self.config_p.read('configs/'+self.config_last)

        active_weapons = {
            "knife": self.config_p.get('SKINCHANGER', 'knife'),
            "knife_skin": self.config_p.get('SKINCHANGER', 'knife_skin'),
            "knife_f": self.config_p.getfloat('SKINCHANGER', 'knife_f'),
            "knife_st": self.config_p.getboolean('SKINCHANGER', 'knife_st'),
            "knife_stv": self.config_p.getint('SKINCHANGER', 'knife_stv'),
            "knife_se": self.config_p.getint('SKINCHANGER', 'knife_se'),
        }

        return active_weapons