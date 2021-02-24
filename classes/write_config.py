from configparser import ConfigParser
from importlib import reload
import ui

class write() :

    def config(self, name) :

        config_object = ConfigParser()

        config_object["VISUALS"] = {
            "glow_active": ui.draw.glow_active,
            "glow_health_based": ui.draw.glow_health_based,
            "glow_ennemies": ui.draw.glow_ennemies,
            "ennemies_glow_color": ui.draw.ennemies_glow_color,
            "glow_allies": ui.draw.glow_allies,
            "allies_glow_color": ui.draw.allies_glow_color,
            "chams_active": ui.draw.chams_active,
            "chams_health_based": ui.draw.chams_health_based,
            "chams_ennemies": ui.draw.chams_ennemies,
            "ennemies_chams_color": ui.draw.ennemies_chams_color,
            "chams_allies": ui.draw.chams_allies,
            "allies_chams_color": ui.draw.allies_chams_color
        }

        config_object["AIM"] = {
            "aimbot": ui.draw.aimbot,
            "aimbot_key": ui.draw.aimbot_key,
            "rcs": ui.draw.rcs,
            "rcs_perfect": ui.draw.rcs_perfect,
            "triggerbot": ui.draw.triggerbot,
            "t_delay": ui.draw.t_delay,
            "triggerbot_key": ui.draw.triggerbot_key,
            "rapid_fire": ui.draw.rapid_fire,
            "rapid_fire_key": ui.draw.rapid_fire_key,
            "silent_aim": ui.draw.silent_aim,
            "silent_aim_key": ui.draw.silent_aim_key,
            "crosshair": ui.draw.crosshair
        }

        config_object["MISC"] = {
            "third_person": ui.draw.third_person,
            "thirdperson_key": ui.draw.thirdperson_key,
            "fov": ui.draw.fov,
            "fov_value": ui.draw.fov_value,
            "hitsound": ui.draw.hitsound,
            "sound": ui.draw.sound,
            "sound_esp": ui.draw.sound_esp,
            "no_flash": ui.draw.no_flash,
            "bhop_rage": ui.draw.bhop_rage,
            "bhop_legit": ui.draw.bhop_legit,
            "show_money": ui.draw.show_money,
            "radar": ui.draw.radar,
            "fake_lag": ui.draw.fake_lag,
            "fake_lag_value": ui.draw.fake_lag_value

        }

        config_object["SETTINGS"] = {
            "ui_color": ui.draw.ui_color
        }

        with open('configs/'+name, 'w') as configfile:
            configfile.seek(0)
            configfile.truncate()
            config_object.write(configfile)