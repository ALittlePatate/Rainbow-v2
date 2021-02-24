from configparser import ConfigParser
import ui

class read() :
    def config(self, config_name) :
        config = ConfigParser()

        config.read('configs/'+config_name)

        #VISUALS
        ui.draw.glow_active = config.getboolean('VISUALS', 'glow_active')
        ui.draw.glow_health_based = config.getboolean('VISUALS', 'glow_health_based')
        ui.draw.glow_ennemies = config.getboolean('VISUALS', 'glow_ennemies')
        ui.draw.ennemies_glow_color = config.get('VISUALS', 'ennemies_glow_color')
        ui.draw.glow_allies = config.getboolean('VISUALS', 'glow_allies')
        ui.draw.allies_glow_color = config.get('VISUALS', 'allies_glow_color')
        ui.draw.chams_active = config.getboolean('VISUALS', 'chams_active')
        ui.draw.chams_health_based = config.getboolean('VISUALS', 'chams_health_based')
        ui.draw.chams_ennemies = config.getboolean('VISUALS', 'chams_ennemies')
        ui.draw.ennemies_chams_color = config.get('VISUALS', 'ennemies_chams_color')
        ui.draw.chams_allies = config.getboolean('VISUALS', 'chams_allies')
        ui.draw.allies_chams_color = config.get('VISUALS', 'allies_chams_color')

        #AIM
        ui.draw.aimbot = config.getboolean('AIM', 'aimbot')
        ui.draw.aimbot_key = config.get('AIM', 'aimbot_key')
        ui.draw.rcs = config.getboolean('AIM', 'rcs')
        ui.draw.rcs_perfect = config.getfloat('AIM', 'rcs_perfect')
        ui.draw.triggerbot = config.getboolean('AIM', 'triggerbot')
        ui.draw.t_delay = config.getfloat('AIM', 't_delay')
        ui.draw.triggerbot_key = config.get('AIM', 'triggerbot_key')
        ui.draw.rapid_fire = config.getboolean('AIM', 'rapid_fire')
        ui.draw.rapid_fire_key = config.get('AIM', 'rapid_fire_key')
        ui.draw.silent_aim = config.getboolean('AIM', 'silent_aim')
        ui.draw.silent_aim_key = config.get('AIM', 'silent_aim_key')
        ui.draw.crosshair = config.getboolean('AIM', 'crosshair')

        #MISC
        ui.draw.third_person = config.getboolean('MISC', 'third_person')
        ui.draw.thirdperson_key = config.get('MISC', 'thirdperson_key')
        ui.draw.fov = config.getboolean('MISC', 'fov')
        ui.draw.fov_value = config.getfloat('MISC', 'fov_value')
        ui.draw.hitsound = config.getboolean('MISC', 'hitsound')
        ui.draw.sound = config.get('MISC', 'sound')
        ui.draw.sound_esp = config.getboolean('MISC', 'sound_esp')
        ui.draw.no_flash = config.getboolean('MISC', 'no_flash')
        ui.draw.bhop_rage = config.getboolean('MISC', 'bhop_rage')
        ui.draw.bhop_legit = config.getboolean('MISC', 'bhop_legit')
        ui.draw.show_money = config.getboolean('MISC', 'show_money')
        ui.draw.radar = config.getboolean('MISC', 'radar')
        ui.draw.fake_lag = config.getboolean('MISC', 'fake_lag')
        ui.draw.fake_lag_value = config.getfloat('MISC', 'fake_lag_value')

        #SETTINGS
        ui.draw.ui_color = config.get('SETTINGS', 'ui_color')