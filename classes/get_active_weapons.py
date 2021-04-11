import ui

class get :
    def active_weapons(self) :
        all_weapons = {
            "Knife": ui.draw.knife,
            "Knife_skin": ui.draw.knife_skin,
            "AK-47": ui.draw.AK47,
            "AUG": ui.draw.AUG,
            "AWP": ui.draw.AWP,
            "CZ75-Auto": ui.draw.CZ75Auto,
            "Desert Eagle": ui.draw.Desert_Eagle,
            "Dual Berettas": ui.draw.Dual_Berettas,
            "FAMAS": ui.draw.FAMAS,
            "Five-Seven": ui.draw.FiveSeven,
            "G3SG1": ui.draw.G3SG1,
            "Galil AR": ui.draw.Galil_AR,
            "Glock-18": ui.draw.Glock18,
            "M249": ui.draw.M249,
            "M4A1-S": ui.draw.M4A1S,
            "M4A4": ui.draw.M4A4,
            "MAC-10": ui.draw.MAC10,
            "MAG-7": ui.draw.MAG7,
            "MP5SD": ui.draw.MP5SD,
            "MP7": ui.draw.MP7,
            "MP9": ui.draw.MP9,
            "Negev": ui.draw.Negev,
            "Nova": ui.draw.Nova,
            "P2000": ui.draw.P2000,
            "P250": ui.draw.P250,
            "P90": ui.draw.P90,
            "PP-Bizon": ui.draw.PPBizon,
            "R8 Revolver": ui.draw.R8_Revolver,
            "SCAR-20": ui.draw.SCAR20,
            "SG 553": ui.draw.SG_553,
            "SSG 08": ui.draw.SSG_08,
            "Sawed-Off": ui.draw.SawedOff,
            "Tec-9": ui.draw.Tec9,
            "UMP45": ui.draw.UMP45,
            "USP-S": ui.draw.USPS,
            "XM1014": ui.draw.XM1014,
        }

        all_knives = ["Gold knife","Spectral knife","Bayonet","Classic knife","Flip knife","Gut knife",
        "Karambit","M9 Bayonet","Huntsman","Falchion knife","Bowie knife",
        "Butterfly knife","Shadow daggers","Cord knife","Canis knife","Ursus knife","Navaja","Nomad knife","Stiletto knife","Talon knife","Skeleton knife"]

        ui.draw.active_weapons = {}
        for weapon, value in all_weapons.items():
            if value != "0" :
                if value in all_knives :
                    ui.draw.active_weapons[value] = ui.draw.knife_skin

                elif weapon == "Knife_skin" : continue

                else :
                    ui.draw.active_weapons[weapon] = value
        
        ui.draw.active_weapons = str(ui.draw.active_weapons)
        ui.draw.active_weapons = ui.draw.active_weapons.replace("{","").replace("}","").replace("'","").replace(":"," : ")
        ui.draw.active_weapons = list(ui.draw.active_weapons.split(","))

        return ui.draw.active_weapons