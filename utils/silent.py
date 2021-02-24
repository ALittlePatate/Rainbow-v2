import pymem
import pymem.process
import time
import ctypes, sys
from Offsets import *
sys.path.insert(1, "classes/")
from features_reads import read
from math import *
import features_check
import keyboard
import win32api

class silent() :
    def __init__(self):
        try :
            self.pm = pymem.Pymem("csgo.exe")
        except :
            MessageBox = ctypes.windll.user32.MessageBoxW
            MessageBox(None, 'Could not find the csgo.exe process !', 'Error', 16)
            return

        self.client = pymem.process.module_from_name(self.pm.process_handle, "client.dll").lpBaseOfDll
        self.engine = pymem.process.module_from_name(self.pm.process_handle, "engine.dll").lpBaseOfDll
        self.engine_pointer = self.pm.read_int(self.engine + dwClientState)

        read("aim")

        while features_check.check.silent_aim :

            read("aim")
            key = self.get_key()

            while key :
                
                try :
                    key = self.get_key()

                    target = None
                    olddistx = 111111111111
                    olddisty = 111111111111

                    if self.client and self.engine and self.pm:
                        try:
                            player = self.pm.read_int(self.client + dwLocalPlayer)
                            localTeam = self.pm.read_int(player + m_iTeamNum)
                        except :
                            continue

                    for i in range(1,32):
                        key = self.get_key()

                        entity = self.pm.read_int(self.client + dwEntityList + i * 0x10)

                        if entity:
                            try:
                                entity_team_id = self.pm.read_int(entity + m_iTeamNum)
                                entity_hp = self.pm.read_int(entity + m_iHealth)
                                entity_dormant = self.pm.read_int(entity + m_bDormant)
                            except :
                                continue
                            
                            if localTeam != entity_team_id and entity_hp > 0:
                                entity_bones = self.pm.read_int(entity + m_dwBoneMatrix)
                                localpos_x_angles = self.pm.read_float(self.engine_pointer + dwClientState_ViewAngles)
                                localpos_y_angles = self.pm.read_float(self.engine_pointer + dwClientState_ViewAngles + 0x4)
                                localpos1 = self.pm.read_float(player + m_vecOrigin)
                                localpos2 = self.pm.read_float(player + m_vecOrigin + 4)
                                localpos_z_angles = self.pm.read_float(player + m_vecViewOffset + 0x8)
                                localpos3 = self.pm.read_float(player + m_vecOrigin + 8) + localpos_z_angles
                                try:
                                    entitypos_x = self.pm.read_float(entity_bones + 0x30 * 8 + 0xC)
                                    entitypos_y = self.pm.read_float(entity_bones + 0x30 * 8 + 0x1C)
                                    entitypos_z = self.pm.read_float(entity_bones + 0x30 * 8 + 0x2C)
                                except:
                                    continue
                                try :
                                    X, Y = self.calcangle(localpos1, localpos2, localpos3, entitypos_x, entitypos_y, entitypos_z)
                                except :
                                    pass
                                newdist_x, newdist_y = self.calc_distance(localpos_x_angles, localpos_y_angles, X, Y)
                                if newdist_x < olddistx and newdist_y < olddisty and newdist_x <= 90 and newdist_y <= 90:
                                    olddistx, olddisty = newdist_x, newdist_y
                                    target, target_hp, target_dormant = entity, entity_hp, entity_dormant
                                    target_x, target_y, target_z = entitypos_x, entitypos_y, entitypos_z
                            if key and player:
                                if target and target_hp > 0 and not target_dormant:
                                    x, y = self.calcangle(localpos1, localpos2, localpos3, target_x, target_y, target_z)
                                    normalize_x, normalize_y = self.normalizeAngles(x, y)
                                    
                                    if key :
                                        #print(dwbSendPackets) #1993604684 #880218
                                        self.pm.write_uchar(self.engine + dwbSendPackets, 0)
                                        Commands = self.pm.read_int(self.client + dwInput + 0xF4)
                                        VerifedCommands = self.pm.read_int(self.client + dwInput + 0xF8)
                                        Desired = self.pm.read_int(self.engine_pointer + clientstate_last_outgoing_command) + 2
                                        OldUser = Commands + ((Desired - 1) % 150) * 100
                                        VerifedOldUser = VerifedCommands + ((Desired - 1) % 150) * 0x68
                                        m_buttons = self.pm.read_int(OldUser + 0x30)
                                        Net_Channel = self.pm.read_uint(self.engine_pointer + clientstate_net_channel)
                                        if self.pm.read_int(Net_Channel + 0x18) >= Desired:
                                            self.pm.write_float(OldUser + 0x0C, normalize_x)
                                            self.pm.write_float(OldUser + 0x10, normalize_y)
                                            self.pm.write_int(OldUser + 0x30, m_buttons | (1 << 0))
                                            self.pm.write_float(VerifedOldUser + 0x0C, normalize_x)
                                            self.pm.write_float(VerifedOldUser + 0x10, normalize_y)
                                            self.pm.write_int(VerifedOldUser + 0x30, m_buttons | (1 << 0))
                                            self.pm.write_uchar(self.engine + dwbSendPackets, 1)
                                        else :
                                            self.pm.write_uchar(self.engine + dwbSendPackets, 1)
                                    else:
                                        self.pm.write_float(self.engine_pointer + dwClientState_ViewAngles, normalize_x)
                                        self.pm.write_float(self.engine_pointer + dwClientState_ViewAngles + 0x4, normalize_y)
                                    
                                        time.sleep(0.2)
                except :
                    pass
            
        self.pm.close_process()
    
    def get_key(self) :
        if "Button.right" in features_check.check.silent_aim_key :
            key = win32api.GetKeyState(0x02)
            if key == -127 or key == -128 :
                key = True
            else :
                key = False
        elif "Button.left" in features_check.check.silent_aim_key :
            key = win32api.GetKeyState(0x01)
            if key == -127 or key == -128 :
                key = True
            else :
                key = False
        elif "Button.middle" in features_check.check.silent_aim_key :
            key = win32api.GetKeyState(0x04)
            if key == -127 or key == -128 :
                key = True
            else :
                key = False
            
        else :
            excpected_key = features_check.check.silent_aim_key
            excpected_key = excpected_key.replace("Key.", "")
            key = keyboard.is_pressed(excpected_key)
        
        return key

    def normalizeAngles(self, viewAngleX, viewAngleY):
        if viewAngleX > 89:
            viewAngleX -= 360
        if viewAngleX < -89:
            viewAngleX += 360
        if viewAngleY > 180:
            viewAngleY -= 360
        if viewAngleY < -180:
            viewAngleY += 360
        return viewAngleX, viewAngleY

    def checkangles(self, x, y):
        if x > 89:
            return False
        elif x < -89:
            return False
        elif y > 360:
            return False
        elif y < -360:
            return False
        else:
            return True

    def nanchecker(self, first, second):
        if math.isnan(first) or math.isnan(second):
            return False
        else:
            return True

    def calc_distance(self, current_x, current_y, new_x, new_y):
        distancex = new_x - current_x
        if distancex < -89:
            distancex += 360
        elif distancex > 89:
            distancex -= 360
        if distancex < 0.0:
            distancex = -distancex
    
        distancey = new_y - current_y
        if distancey < -180:
            distancey += 360
        elif distancey > 180:
            distancey -= 360
        if distancey < 0.0:
            distancey = -distancey
        return distancex, distancey

    def calcangle(self, localpos1, localpos2, localpos3, enemypos1, enemypos2, enemypos3):
        try:
            delta_x = localpos1 - enemypos1
            delta_y = localpos2 - enemypos2
            delta_z = localpos3 - enemypos3
            hyp = sqrt(delta_x * delta_x + delta_y * delta_y + delta_z * delta_z)
            x = atan(delta_z / hyp) * 180 / pi
            y = atan(delta_y / delta_x) * 180 / pi
            if delta_x >= 0.0:
                y += 180.0
            return x, y
        except Exception as e:
            print(e)
            pass