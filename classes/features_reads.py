from configparser import ConfigParser
import features_check

class read() :
    def __init__(self, *args) :
        config = ConfigParser()

        while True :
            try :
                with open("configs/last/last.txt", "r") as f :
                    for line in f :
                        last = line

                        config.read('configs/'+last)

                        if args :
                            if args[0] == "glow" :
                                features_check.check.glow_active = config.getboolean('VISUALS', 'glow_active')
                                features_check.check.glow_health_based = config.getboolean('VISUALS', 'glow_health_based')
                                features_check.check.glow_ennemies = config.getboolean('VISUALS', 'glow_ennemies')
                                features_check.check.ennemies_glow_color = config.get('VISUALS', 'ennemies_glow_color')
                                features_check.check.glow_allies = config.getboolean('VISUALS', 'glow_allies')
                                features_check.check.allies_glow_color = config.get('VISUALS', 'allies_glow_color')
                                return
                        
                            elif args[0] == "chams" :
                                features_check.check.chams_active = config.getboolean('VISUALS', 'chams_active')
                                features_check.check.chams_health_based = config.getboolean('VISUALS', 'chams_health_based')
                                features_check.check.chams_ennemies = config.getboolean('VISUALS', 'chams_ennemies')
                                features_check.check.ennemies_chams_color = config.get('VISUALS', 'ennemies_chams_color')
                                features_check.check.chams_allies = config.getboolean('VISUALS', 'chams_allies')
                                features_check.check.allies_chams_color = config.get('VISUALS', 'allies_chams_color')
                                return
                            
                            elif args[0] == "aim" :
                                features_check.check.aimbot = config.getboolean('AIM', 'aimbot')
                                features_check.check.aimbot_key = config.get('AIM', 'aimbot_key')
                                features_check.check.silent_aim = config.getboolean('AIM', 'silent_aim')
                                features_check.check.silent_aim_key = config.get('AIM', 'silent_aim_key')
                                features_check.check.crosshair = config.getboolean('AIM', 'crosshair')
                                return
                            
                            elif args[0] == "rcs" :
                                features_check.check.rcs = config.getboolean('AIM', 'rcs')
                                features_check.check.rcs_perfect = config.getfloat('AIM', 'rcs_perfect')
                            
                            elif args[0] == "triggerbot" :
                                features_check.check.triggerbot = config.getboolean('AIM', 'triggerbot')
                                features_check.check.t_delay = config.getfloat('AIM', 't_delay')
                                features_check.check.triggerbot_key = config.get('AIM', 'triggerbot_key')
                            
                            elif args[0] == "rapid fire" :
                                features_check.check.rapid_fire = config.getboolean('AIM', 'rapid_fire')
                                features_check.check.rapid_fire_key = config.get('AIM', 'rapid_fire_key')
                            
                            elif args[0] == "misc" :
                                features_check.check.third_person = config.getboolean('MISC', 'third_person')
                                features_check.check.thirdperson_key = config.get('MISC', 'thirdperson_key')
                                features_check.check.fov = config.getboolean('MISC', 'fov')
                                features_check.check.fov_value = config.getfloat('MISC', 'fov_value')
                                features_check.check.hitsound = config.getboolean('MISC', 'hitsound')
                                features_check.check.sound = config.get('MISC', 'sound')
                                features_check.check.sound_esp = config.getboolean('MISC', 'sound_esp')
                                features_check.check.no_flash = config.getboolean('MISC', 'no_flash')
                                features_check.check.bhop_rage = config.getboolean('MISC', 'bhop_rage')
                                features_check.check.bhop_legit = config.getboolean('MISC', 'bhop_legit')
                                features_check.check.show_money = config.getboolean('MISC', 'show_money')
                                features_check.check.radar = config.getboolean('MISC', 'radar')
                                features_check.check.fake_lag = config.getboolean('MISC', 'fake_lag')
                                features_check.check.fake_lag_value = config.getfloat('MISC', 'fake_lag_value')



                        #VISUALS
                        features_check.check.glow_active = config.getboolean('VISUALS', 'glow_active')
                        features_check.check.glow_health_based = config.getboolean('VISUALS', 'glow_health_based')
                        features_check.check.glow_ennemies = config.getboolean('VISUALS', 'glow_ennemies')
                        features_check.check.ennemies_glow_color = config.get('VISUALS', 'ennemies_glow_color')
                        features_check.check.glow_allies = config.getboolean('VISUALS', 'glow_allies')
                        features_check.check.allies_glow_color = config.get('VISUALS', 'allies_glow_color')
                        features_check.check.chams_active = config.getboolean('VISUALS', 'chams_active')
                        features_check.check.chams_health_based = config.getboolean('VISUALS', 'chams_health_based')
                        features_check.check.chams_ennemies = config.getboolean('VISUALS', 'chams_ennemies')
                        features_check.check.ennemies_chams_color = config.get('VISUALS', 'ennemies_chams_color')
                        features_check.check.chams_allies = config.getboolean('VISUALS', 'chams_allies')
                        features_check.check.allies_chams_color = config.get('VISUALS', 'allies_chams_color')

                        #AIM
                        features_check.check.aimbot = config.getboolean('AIM', 'aimbot')
                        features_check.check.aimbot_key = config.get('AIM', 'aimbot_key')
                        features_check.check.rcs = config.getboolean('AIM', 'rcs')
                        features_check.check.rcs_perfect = config.getfloat('AIM', 'rcs_perfect')
                        features_check.check.triggerbot = config.getboolean('AIM', 'triggerbot')
                        features_check.check.t_delay = config.getfloat('AIM', 't_delay')
                        features_check.check.triggerbot_key = config.get('AIM', 'triggerbot_key')
                        features_check.check.rapid_fire = config.getboolean('AIM', 'rapid_fire')
                        features_check.check.rapid_fire_key = config.get('AIM', 'rapid_fire_key')
                        features_check.check.silent_aim = config.getboolean('AIM', 'silent_aim')
                        features_check.check.silent_aim_key = config.get('AIM', 'silent_aim_key')
                        features_check.check.crosshair = config.getboolean('AIM', 'crosshair')

                        #MISC
                        features_check.check.third_person = config.getboolean('MISC', 'third_person')
                        features_check.check.thirdperson_key = config.get('MISC', 'thirdperson_key')
                        features_check.check.fov = config.getboolean('MISC', 'fov')
                        features_check.check.fov_value = config.getfloat('MISC', 'fov_value')
                        features_check.check.hitsound = config.getboolean('MISC', 'hitsound')
                        features_check.check.sound = config.get('MISC', 'sound')
                        features_check.check.sound_esp = config.getboolean('MISC', 'sound_esp')
                        features_check.check.no_flash = config.getboolean('MISC', 'no_flash')
                        features_check.check.bhop_rage = config.getboolean('MISC', 'bhop_rage')
                        features_check.check.bhop_legit = config.getboolean('MISC', 'bhop_legit')
                        features_check.check.show_money = config.getboolean('MISC', 'show_money')
                        features_check.check.radar = config.getboolean('MISC', 'radar')
                        features_check.check.fake_lag = config.getboolean('MISC', 'fake_lag')
                        features_check.check.fake_lag_value = config.getfloat('MISC', 'fake_lag_value')

                        #SETTINGS
                        features_check.check.ui_color = config.get('SETTINGS', 'ui_color')
                        return
                        
            except Exception as e:
                pass