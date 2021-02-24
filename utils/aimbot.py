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


class aimbot() :
    def __init__(self):
        try :
            self.pm = pymem.Pymem("csgo.exe")
        except :
            MessageBox = ctypes.windll.user32.MessageBoxW
            MessageBox(None, 'Could not find the csgo.exe process !', 'Error', 16)
            return
        
        self.client = pymem.process.module_from_name(self.pm.process_handle, "client.dll").lpBaseOfDll
        self.engine = pymem.process.module_from_name(self.pm.process_handle, "engine.dll").lpBaseOfDll
        self.enginepointer = self.pm.read_int(self.engine + dwClientState)

        read("aim")

        while features_check.check.aimbot :

            read("aim")

            key = self.get_key()
            time.sleep(0.002)

            try :
                while key :
                    key = self.get_key()

                    aimlocalplayer = self.pm.read_int(self.client + dwLocalPlayer)
                    aimflag = self.pm.read_int(aimlocalplayer + m_fFlags)
                    aimteam = self.pm.read_int(aimlocalplayer + m_iTeamNum)
                
                    for y in range(1):

                        if self.pm.read_int(self.client + dwEntityList + y * 0x10):
                            aimplayer = self.GetBestTarget(aimlocalplayer)
                            aimplayerbone = self.pm.read_int(aimplayer + m_dwBoneMatrix)
                            gungameimmunity = self.pm.read_int(aimplayer + m_bGunGameImmunity)
                            aimplayerteam = self.pm.read_int(aimplayer + m_iTeamNum)
                            aimplayerhealth = self.pm.read_int(aimplayer + m_iHealth)
                            if aimplayerteam != aimteam and aimplayerhealth > 0 and gungameimmunity != 1:
                                localpos1 = self.pm.read_float(aimlocalplayer + m_vecOrigin)
                                localpos2 = self.pm.read_float(aimlocalplayer + m_vecOrigin + 4)
                                if aimflag == 263:
                                    localpos3 = self.pm.read_float(aimlocalplayer + m_vecOrigin + 8) + 45
                                elif aimflag == 257:
                                    localpos3 = self.pm.read_float(aimlocalplayer + m_vecOrigin + 8) + 62
                                elif aimflag == 256:
                                    localpos3 = self.pm.read_float(aimlocalplayer + m_vecOrigin + 8) + 64
                                
                                bone = 8 #head
                                enemypos1 = self.pm.read_float(aimplayerbone + 0x30 * bone + 0xC)
                                enemypos2 = self.pm.read_float(aimplayerbone + 0x30 * bone + 0x1C)
                                enemypos3 = self.pm.read_float(aimplayerbone + 0x30 * bone + 0x2C)
                
                                targetline1 = enemypos1 - localpos1
                                targetline2 = enemypos2 - localpos2
                                targetline3 = enemypos3 - localpos3
                
                                viewanglex = self.pm.read_float(self.enginepointer + dwClientState_ViewAngles)
                                viewangley = self.pm.read_float(self.enginepointer + dwClientState_ViewAngles + 0x4)
                
                                if targetline2 == 0 and targetline1 == 0:
                                    yaw = 0
                                    if targetline3 > 0:
                                        pitch = 270
                                    else:
                                        pitch = 90
                                else:
                                    yaw = (atan2(targetline2, targetline1) * 180 / pi)
                                    if yaw < 0:
                                        yaw += 360
                                    hypo = sqrt(
                                        (targetline1 * targetline1) + (targetline2 * targetline2) + (targetline3 * targetline3))
                                    pitch = (atan2(-targetline3, hypo) * 180 / pi)
                
                                    if pitch < 0:
                                        pitch += 360
                
                                pitch, yaw = self.normalizeAngles(pitch, yaw)
                                if self.checkangles(pitch, yaw):
                
                                    distance_x, distance_y = self.calc_distance(viewanglex, viewangley, pitch, yaw)
                
                                    if distance_x < 900 and distance_y < 900:
                
                                        if self.nanchecker(pitch, yaw):
                                            key = self.get_key()
                                            if key :
                                                
                                                self.pm.write_float(self.enginepointer + dwClientState_ViewAngles, pitch)
                                                self.pm.write_float(self.enginepointer + dwClientState_ViewAngles + 0x4, yaw)
            except :
                pass
        
        self.pm.close_process()

    def get_key(self) :
        if "Button.right" in features_check.check.aimbot_key :
            key = win32api.GetKeyState(0x02)
            if key == -127 or key == -128 :
                key = True
            else :
                key = False
        elif "Button.left" in features_check.check.aimbot_key :
            key = win32api.GetKeyState(0x01)
            if key == -127 or key == -128 :
                key = True
            else :
                key = False
        elif "Button.middle" in features_check.check.aimbot_key :
            key = win32api.GetKeyState(0x04)
            if key == -127 or key == -128 :
                key = True
            else :
                key = False
            
        else :
            excpected_key = features_check.check.aimbot_key
            excpected_key = excpected_key.replace("Key.", "")
            key = keyboard.is_pressed(excpected_key)
        
        return key

    def checkindex(self) :
        localplayer = self.pm.read_int(self.client + dwLocalPlayer)
        for y in range(64):
            if self.pm.read_int(self.client + dwEntityList + y * 0x10):
                entity = self.pm.read_int(self.client + dwEntityList + y * 0x10)
                if localplayer == entity and y:
                    return y
    
    def nanchecker(self, first, second):
        if isnan(first) or isnan(second):
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
    
    
    def Magnitude(self, vec_x, vec_y, vec_z):
        return sqrt(vec_x * vec_x + vec_y * vec_y + vec_z * vec_z)
    
    
    def Subtract(self, src_x, src_y, src_z, dst_x, dst_y, dst_z):
        diff_x = src_x - dst_x
        diff_y = src_y - dst_y
        diff_z = src_z - dst_z
        return (diff_x, diff_y, diff_z)
    
    
    def Distance(self, src_x, src_y, src_z, dst_x, dst_y, dst_z):
        diff_x, diff_y, diff_z = self.Subtract(src_x, src_y, src_z, dst_x, dst_y, dst_z)
        src_x += diff_x
        src_y += diff_y
        return self.Magnitude(diff_x, diff_y, diff_z)
    
    
    def calcangle(self, src_x, src_y, src_z, dst_x, dst_y, dst_z):
        x = -atan2(dst_x - src_x, dst_y - src_y) / pi * 180.0 + 180.0
        y = asin((dst_z - src_z) / self.Distance(src_x, src_y, src_z, dst_x, dst_y, dst_z)) * 180.0 / pi
        return x, y
    
    
    def GetBestTarget(self, local):
        while True:
            olddist = 1.7976931348623157e+308
            newdist = None
            target = None
            if local :
                localplayer_team = self.pm.read_int(local + m_iTeamNum)
                for x in range(1):
                    entity_id = self.pm.read_int(local + m_iCrosshairId)
                    entity = self.pm.read_int(self.client + dwEntityList + (entity_id - 1) * 0x10)
                    if self.pm.read_int(self.client + dwEntityList + x * 0x10):
                        spotted = self.pm.read_int(entity + m_bSpottedByMask)
                        index = self.checkindex()
                        entity_health = self.pm.read_int(entity + m_iHealth)
                        entity_team = self.pm.read_int(entity + m_iTeamNum)
                        if localplayer_team != entity_team and entity_health > 0 :# and spotted == 1 << index:
                            entity_bones = self.pm.read_int(entity + m_dwBoneMatrix)
                            localpos_x = self.pm.read_float(local + m_vecOrigin)
                            localpos_y = self.pm.read_float(local + m_vecOrigin + 4)
                            localpos_z = self.pm.read_float(local + m_vecOrigin + 8)
    
                            localpos_x_angles = self.pm.read_float(self.enginepointer + dwClientState_ViewAngles)
                            localpos_y_angles = self.pm.read_float(self.enginepointer + dwClientState_ViewAngles + 0x4)
                            localpos_z_angles = self.pm.read_float(self.enginepointer + dwClientState_ViewAngles + 0x8)

                            bone = 8 #head
                            entitypos_x = self.pm.read_float(entity_bones + 0x30 * bone + 0xC)
                            entitypos_y = self.pm.read_float(entity_bones + 0x30 * bone + 0x1C)
                            entitypos_z = self.pm.read_float(entity_bones + 0x30 * bone + 0x2C) + 64
    
                            X, Y = self.calcangle(entitypos_x, entitypos_y, entitypos_z, localpos_x, localpos_y, localpos_z)
                            newdist = self.Distance(localpos_x_angles, localpos_y_angles, localpos_z_angles, entitypos_x,
                                            entitypos_y, entitypos_z)
                            olddist = newdist
                            target = entity
                if target:
                    return target