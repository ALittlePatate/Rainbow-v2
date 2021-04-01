from multiprocessing import *
import multiprocessing

import sys, time
import importlib
sys.path.insert(1, "classes/")
from features_reads import read

sys.path.insert(1, "utils/")
from glow import glow
from chams import chams
from chams_reset import chams_reset
from aimbot import aimbot
from rcs import rcs
from triggerbot import triggerbot
from rapidfire import rapidfire
from silent import silent
from crosshair_hack import crosshair_hack
from thirdperson import thirdperson
from fov import fov
from fov_reset import fov_reset
from hitsound import hitsound
from soundesp import sound_esp
from noflash import noflash
from noflash_reset import noflash_reset
from bhop_rage import bhop_rage
from bhop_legit import bhop_legit
from money import money
from money_reset import money_reset
from radar import radar
from radar_reset import radar_reset
from fake_lag import fake_lag
from skinchanger import skinchanger_func

class check :
    def __init__(self) :

        self.is_running()

    def is_running(self) :
        glow_switch = False
        chams_switch = False
        chams_reset_switch = False
        aimbot_switch = False
        rcs_switch = False
        triggerbot_switch = False
        rapidfire_switch = False
        silent_aim_switch = False
        crosshair_switch = False
        thirdperson_switch = False
        fov_switch = False
        fov_reset_switch = False
        hitsound_switch = False
        soundesp_switch = False
        noflash_switch = False
        noflash_reset_switch = False
        bhop_rage_switch = False
        bhop_legit_switch = False
        show_money_switch = False
        show_money_reset_switch = False
        radar_switch = False
        radar_reset_switch = False
        fake_lag_switch = False
        
        multiprocessing.freeze_support()
        t_skinchanger = Process(target = skinchanger_func)
        t_skinchanger.start()

        while True :
            try :
            
                read()


                if check.glow_active and glow_switch == False :
                    multiprocessing.freeze_support()
                    t_glow = Process(target = glow)
                    t_glow.start()
                    glow_switch = True

                elif not check.glow_active and glow_switch == True:
                    t_glow.terminate()
                    glow_switch = False
                
                if check.chams_active and chams_switch == False :
                    if chams_reset_switch == True :
                        t_chams_reset.terminate()
                        chams_reset_switch = False

                    multiprocessing.freeze_support()
                    t_chams = Process(target = chams)
                    t_chams.start()
                    chams_switch = True
                
                elif not check.chams_active and chams_switch == True:
                    t_chams.terminate()
                    multiprocessing.freeze_support()
                    t_chams_reset = Process(target = chams_reset)
                    t_chams_reset.start()
                    chams_reset_switch = True
                    chams_switch = False
                
                if check.aimbot and aimbot_switch == False :
                    multiprocessing.freeze_support()
                    t_aimbot = Process(target = aimbot)
                    t_aimbot.start()
                    aimbot_switch = True

                elif not check.aimbot and aimbot_switch == True:
                    t_aimbot.terminate()
                    aimbot_switch = False
                
                if check.rcs and rcs_switch == False :
                    multiprocessing.freeze_support()
                    t_rcs = Process(target = rcs)
                    t_rcs.start()
                    rcs_switch = True

                elif not check.rcs and rcs_switch == True:
                    t_rcs.terminate()
                    rcs_switch = False
                
                if check.triggerbot and triggerbot_switch == False :
                    multiprocessing.freeze_support()
                    t_triggerbot = Process(target = triggerbot)
                    t_triggerbot.start()
                    triggerbot_switch = True

                elif not check.triggerbot and triggerbot_switch == True:
                    t_triggerbot.terminate()
                    triggerbot_switch = False
                
                if check.rapid_fire and rapidfire_switch == False :
                    multiprocessing.freeze_support()
                    t_rapid_fire = Process(target = rapidfire)
                    t_rapid_fire.start()
                    rapidfire_switch = True

                elif not check.rapid_fire and rapidfire_switch == True:
                    t_rapid_fire.terminate()
                    rapidfire_switch = False
                
                if check.silent_aim and silent_aim_switch == False :
                    multiprocessing.freeze_support()
                    t_silent_aim = Process(target = silent)
                    t_silent_aim.start()
                    silent_aim_switch = True

                elif not check.silent_aim and silent_aim_switch == True:
                    t_silent_aim.terminate()
                    silent_aim_switch = False
                
                if check.crosshair and crosshair_switch == False :
                    multiprocessing.freeze_support()
                    t_crosshair = Process(target = crosshair_hack)
                    t_crosshair.start()
                    crosshair_switch = True

                elif not check.crosshair and crosshair_switch == True:
                    t_crosshair.terminate()
                    crosshair_switch = False
                
                if check.third_person and thirdperson_switch == False :
                    multiprocessing.freeze_support()
                    t_thirdperson = Process(target = thirdperson)
                    t_thirdperson.start()
                    thirdperson_switch = True

                elif not check.third_person and thirdperson_switch == True:
                    t_thirdperson.terminate()
                    thirdperson_switch = False
                
                if check.fov and fov_switch == False :
                    if fov_reset_switch == True :
                        t_fov_reset.terminate()
                        fov_reset_switch = False

                    multiprocessing.freeze_support()
                    t_fov = Process(target = fov)
                    t_fov.start()
                    fov_switch = True
                
                elif not check.fov and fov_switch == True:
                    t_fov.terminate()
                    multiprocessing.freeze_support()
                    t_fov_reset = Process(target = fov_reset)
                    t_fov_reset.start()
                    fov_reset_switch = True
                    fov_switch = False
                
                if check.hitsound and hitsound_switch == False :
                    multiprocessing.freeze_support()
                    t_hitsound = Process(target = hitsound)
                    t_hitsound.start()
                    hitsound_switch = True

                elif not check.hitsound and hitsound_switch == True:
                    t_hitsound.terminate()
                    hitsound_switch = False
                
                if check.sound_esp and soundesp_switch == False :
                    multiprocessing.freeze_support()
                    t_soundesp = Process(target = sound_esp)
                    t_soundesp.start()
                    soundesp_switch = True

                elif not check.sound_esp and soundesp_switch == True:
                    t_soundesp.terminate()
                    soundesp_switch = False
                
                if check.no_flash and noflash_switch == False :
                    if noflash_reset_switch == True :
                        t_noflash_reset.terminate()
                        noflash_reset_switch = False

                    multiprocessing.freeze_support()
                    t_noflash = Process(target = noflash)
                    t_noflash.start()
                    noflash_switch = True
                
                elif not check.no_flash and noflash_switch == True:
                    t_noflash.terminate()
                    multiprocessing.freeze_support()
                    t_noflash_reset = Process(target = noflash_reset)
                    t_noflash_reset.start()
                    noflash_reset_switch = True
                    noflash_switch = False
                
                if check.bhop_rage and bhop_rage_switch == False :
                    multiprocessing.freeze_support()
                    t_bhop_rage = Process(target = bhop_rage)
                    t_bhop_rage.start()
                    bhop_rage_switch = True

                elif not check.bhop_rage and bhop_rage_switch == True:
                    t_bhop_rage.terminate()
                    bhop_rage_switch = False
                
                if check.bhop_legit and bhop_legit_switch == False :
                    multiprocessing.freeze_support()
                    t_bhop_legit = Process(target = bhop_legit)
                    t_bhop_legit.start()
                    bhop_legit_switch = True

                elif not check.bhop_legit and bhop_legit_switch == True:
                    t_bhop_legit.terminate()
                    bhop_legit_switch = False
                
                if check.show_money and show_money_switch == False :
                    if show_money_reset_switch == True :
                        t_show_money_reset.terminate()
                        show_money_reset_switch = False

                    multiprocessing.freeze_support()
                    t_show_money = Process(target = money)
                    t_show_money.start()
                    show_money_switch = True
                
                elif not check.show_money and show_money_switch == True:
                    t_show_money.terminate()
                    multiprocessing.freeze_support()
                    t_show_money_reset = Process(target = money_reset)
                    t_show_money_reset.start()
                    show_money_reset_switch = True
                    show_money_switch = False
                
                if check.radar and radar_switch == False :
                    if radar_reset_switch == True :
                        t_radar_reset.terminate()
                        radar_reset_switch = False

                    multiprocessing.freeze_support()
                    t_radar = Process(target = radar)
                    t_radar.start()
                    radar_switch = True
                
                elif not check.radar and radar_switch == True:
                    t_radar.terminate()
                    multiprocessing.freeze_support()
                    t_radar_reset = Process(target = radar_reset)
                    t_radar_reset.start()
                    radar_reset_switch = True
                    radar_switch = False
                
                if check.fake_lag and fake_lag_switch == False :
                    multiprocessing.freeze_support()
                    t_fake_lag = Process(target = fake_lag)
                    t_fake_lag.start()
                    fake_lag_switch = True

                elif not check.fake_lag and fake_lag_switch == True:
                    t_fake_lag.terminate()
                    fake_lag_switch = False
            
            except Exception as e:
                print(e)
