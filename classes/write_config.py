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

        config_object["SKINCHANGER"] = {
            "AK47": ui.draw.AK47,
            "AK47_f": ui.draw.AK47_f,
            "AK47_st": ui.draw.AK47_st,
            "AK47_stv": ui.draw.AK47_stv,
            "AK47_se": ui.draw.AK47_se,
            "AUG": ui.draw.AUG,
            "AUG_f": ui.draw.AUG_f,
            "AUG_st": ui.draw.AUG_st,
            "AUG_stv": ui.draw.AUG_stv,
            "AUG_se": ui.draw.AUG_se,
            "AWP": ui.draw.AWP,
            "AWP_f": ui.draw.AWP_f,
            "AWP_st": ui.draw.AWP_st,
            "AWP_stv": ui.draw.AWP_stv,
            "AWP_se": ui.draw.AWP_se,
            "CZ75Auto": ui.draw.CZ75Auto,
            "CZ75Auto_f": ui.draw.CZ75Auto_f,
            "CZ75Auto_st": ui.draw.CZ75Auto_st,
            "CZ75Auto_stv": ui.draw.CZ75Auto_stv,
            "CZ75Auto_se": ui.draw.CZ75Auto_se,
            "Desert_Eagle": ui.draw.Desert_Eagle,
            "Desert_Eagle_f": ui.draw.Desert_Eagle_f,
            "Desert_Eagle_st": ui.draw.Desert_Eagle_st,
            "Desert_Eagle_stv": ui.draw.Desert_Eagle_stv,
            "Desert_Eagle_se": ui.draw.Desert_Eagle_se,
            "Dual_Berettas": ui.draw.Dual_Berettas,
            "Dual_Berettas_f": ui.draw.Dual_Berettas_f,
            "Dual_Berettas_st": ui.draw.Dual_Berettas_st,
            "Dual_Berettas_stv": ui.draw.Dual_Berettas_stv,
            "Dual_Berettas_se": ui.draw.Dual_Berettas_se,
            "FAMAS": ui.draw.FAMAS,
            "FAMAS_f": ui.draw.FAMAS_f,
            "FAMAS_st": ui.draw.FAMAS_st,
            "FAMAS_stv": ui.draw.FAMAS_stv,
            "FAMAS_se": ui.draw.FAMAS_se,
            "FiveSeven": ui.draw.FiveSeven,
            "FiveSeven_f": ui.draw.FiveSeven_f,
            "FiveSeven_st": ui.draw.FiveSeven_st,
            "FiveSeven_stv": ui.draw.FiveSeven_stv,
            "FiveSeven_se": ui.draw.FiveSeven_se,
            "G3SG1": ui.draw.G3SG1,
            "G3SG1_f": ui.draw.G3SG1_f,
            "G3SG1_st": ui.draw.G3SG1_st,
            "G3SG1_stv": ui.draw.G3SG1_stv,
            "G3SG1_se": ui.draw.G3SG1_se,
            "Galil_AR": ui.draw.Galil_AR,
            "Galil_AR_f": ui.draw.Galil_AR_f,
            "Galil_AR_st": ui.draw.Galil_AR_st,
            "Galil_AR_stv": ui.draw.Galil_AR_stv,
            "Galil_AR_se": ui.draw.Galil_AR_se,
            "Glock18": ui.draw.Glock18,
            "Glock18_f": ui.draw.Glock18_f,
            "Glock18_st": ui.draw.Glock18_st,
            "Glock18_stv": ui.draw.Glock18_stv,
            "Glock18_se": ui.draw.Glock18_se,
            "M249": ui.draw.M249,
            "M249_f": ui.draw.M249_f,
            "M249_st": ui.draw.M249_st,
            "M249_stv": ui.draw.M249_stv,
            "M249_se": ui.draw.M249_se,
            "M4A1S": ui.draw.M4A1S,
            "M4A1S_f": ui.draw.M4A1S_f,
            "M4A1S_st": ui.draw.M4A1S_st,
            "M4A1S_stv": ui.draw.M4A1S_stv,
            "M4A1S_se": ui.draw.M4A1S_se,
            "M4A4": ui.draw.M4A4,
            "M4A4_f": ui.draw.M4A4_f,
            "M4A4_st": ui.draw.M4A4_st,
            "M4A4_stv": ui.draw.M4A4_stv,
            "M4A4_se": ui.draw.M4A4_se,
            "MAC10": ui.draw.MAC10,
            "MAC10_f": ui.draw.MAC10_f,
            "MAC10_st": ui.draw.MAC10_st,
            "MAC10_stv": ui.draw.MAC10_stv,
            "MAC10_se": ui.draw.MAC10_se,
            "MAG7": ui.draw.MAG7,
            "MAG7_f": ui.draw.MAG7_f,
            "MAG7_st": ui.draw.MAG7_st,
            "MAG7_stv": ui.draw.MAG7_stv,
            "MAG7_se": ui.draw.MAG7_se,
            "MP5SD": ui.draw.MP5SD,
            "MP5SD_f": ui.draw.MP5SD_f,
            "MP5SD_st": ui.draw.MP5SD_st,
            "MP5SD_stv": ui.draw.MP5SD_stv,
            "MP5SD_se": ui.draw.MP5SD_se,
            "MP7": ui.draw.MP7,
            "MP7_f": ui.draw.MP7_f,
            "MP7_st": ui.draw.MP7_st,
            "MP7_stv": ui.draw.MP7_stv,
            "MP7_se": ui.draw.MP7_se,
            "MP9": ui.draw.MP9,
            "MP9_f": ui.draw.MP9_f,
            "MP9_st": ui.draw.MP9_st,
            "MP9_stv": ui.draw.MP9_stv,
            "MP9_se": ui.draw.MP9_se,
            "Negev": ui.draw.Negev,
            "Negev_f": ui.draw.Negev_f,
            "Negev_st": ui.draw.Negev_st,
            "Negev_stv": ui.draw.Negev_stv,
            "Negev_se": ui.draw.Negev_se,
            "Nova": ui.draw.Nova,
            "Nova_f": ui.draw.Nova_f,
            "Nova_st": ui.draw.Nova_st,
            "Nova_stv": ui.draw.Nova_stv,
            "Nova_se": ui.draw.Nova_se,
            "P2000": ui.draw.P2000,
            "P2000_f": ui.draw.P2000_f,
            "P2000_st": ui.draw.P2000_st,
            "P2000_stv": ui.draw.P2000_stv,
            "P2000_se": ui.draw.P2000_se,
            "P250": ui.draw.P250,
            "P250_f": ui.draw.P250_f,
            "P250_st": ui.draw.P250_st,
            "P250_stv": ui.draw.P250_stv,
            "P250_se": ui.draw.P250_se,
            "P90": ui.draw.P90,
            "P90_f": ui.draw.P90_f,
            "P90_st": ui.draw.P90_st,
            "P90_stv": ui.draw.P90_stv,
            "P90_se": ui.draw.P90_se,
            "PPBizon": ui.draw.PPBizon,
            "PPBizon_f": ui.draw.PPBizon_f,
            "PPBizon_st": ui.draw.PPBizon_st,
            "PPBizon_stv": ui.draw.PPBizon_stv,
            "PPBizon_se": ui.draw.PPBizon_se,
            "R8_Revolver": ui.draw.R8_Revolver,
            "R8_Revolver_f": ui.draw.R8_Revolver_f,
            "R8_Revolver_st": ui.draw.R8_Revolver_st,
            "R8_Revolver_stv": ui.draw.R8_Revolver_stv,
            "R8_Revolver_se": ui.draw.R8_Revolver_se,
            "SCAR20": ui.draw.SCAR20,
            "SCAR20_f": ui.draw.SCAR20_f,
            "SCAR20_st": ui.draw.SCAR20_st,
            "SCAR20_stv": ui.draw.SCAR20_stv,
            "SCAR20_se": ui.draw.SCAR20_se,
            "SG_553": ui.draw.SG_553,
            "SG_553_f": ui.draw.SG_553_f,
            "SG_553_st": ui.draw.SG_553_st,
            "SG_553_stv": ui.draw.SG_553_stv,
            "SG_553_se": ui.draw.SG_553_se,
            "SSG_08": ui.draw.SSG_08,
            "SSG_08_f": ui.draw.SSG_08_f,
            "SSG_08_st": ui.draw.SSG_08_st,
            "SSG_08_stv": ui.draw.SSG_08_stv,
            "SSG_08_se": ui.draw.SSG_08_se,
            "SawedOff": ui.draw.SawedOff,
            "SawedOff_f": ui.draw.SawedOff_f,
            "SawedOff_st": ui.draw.SawedOff_st,
            "SawedOff_stv": ui.draw.SawedOff_stv,
            "SawedOff_se": ui.draw.SawedOff_se,
            "Tec9": ui.draw.Tec9,
            "Tec9_f": ui.draw.Tec9_f,
            "Tec9_st": ui.draw.Tec9_st,
            "Tec9_stv": ui.draw.Tec9_stv,
            "Tec9_se": ui.draw.Tec9_se,
            "UMP45": ui.draw.UMP45,
            "UMP45_f": ui.draw.UMP45_f,
            "UMP45_st": ui.draw.UMP45_st,
            "UMP45_stv": ui.draw.UMP45_stv,
            "UMP45_se": ui.draw.UMP45_se,
            "USPS": ui.draw.USPS,
            "USPS_f": ui.draw.USPS_f,
            "USPS_st": ui.draw.USPS_st,
            "USPS_stv": ui.draw.USPS_stv,
            "USPS_se": ui.draw.USPS_se,
            "XM1014": ui.draw.XM1014,
            "XM1014_f": ui.draw.XM1014_f,
            "XM1014_st": ui.draw.XM1014_st,
            "XM1014_stv": ui.draw.XM1014_stv,
            "XM1014_se": ui.draw.XM1014_se
        }

        with open('configs/'+name, 'w') as configfile:
            configfile.seek(0)
            configfile.truncate()
            config_object.write(configfile)