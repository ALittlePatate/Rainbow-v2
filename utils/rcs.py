import pymem
import pymem.process
import time
import ctypes, sys, time
from Offsets import *
sys.path.insert(1, "classes/")
from features_reads import read
from math import *
import math
import features_check

class rcs() :
    def __init__(self):
        try :
            self.pm = pymem.Pymem("csgo.exe")
        except :
            MessageBox = ctypes.windll.user32.MessageBoxW
            MessageBox(None, 'Could not find the csgo.exe process !', 'Error', 16)
            return

        self.client = pymem.process.module_from_name(self.pm.process_handle, "client.dll").lpBaseOfDll
        self.engine = pymem.process.module_from_name(self.pm.process_handle, "engine.dll").lpBaseOfDll

        read("rcs")

        perfect_percentage = features_check.check.rcs_perfect

        oldpunchx = 0.0
        oldpunchy = 0.0


        while features_check.check.rcs :
            read("rcs")
            perfect_percentage = features_check.check.rcs_perfect

            try :
                time.sleep(0.01)

                rcslocalplayer = self.pm.read_int(self.client + dwLocalPlayer)
                rcsengine = self.pm.read_int(self.engine + dwClientState)

                if self.pm.read_int(rcslocalplayer + m_iShotsFired) > 2:
                    rcs_x = self.pm.read_float(rcsengine + dwClientState_ViewAngles)
                    rcs_y = self.pm.read_float(rcsengine + dwClientState_ViewAngles + 0x4)
                    punchx = self.pm.read_float(rcslocalplayer + m_aimPunchAngle)
                    punchy = self.pm.read_float(rcslocalplayer + m_aimPunchAngle + 0x4)
                    newrcsx = rcs_x - (punchx - oldpunchx) * (perfect_percentage * 0.02)
                    newrcsy = rcs_y - (punchy - oldpunchy) * (perfect_percentage * 0.02)
                    newrcs, newrcy = self.normalizeAngles(newrcsx, newrcsy)
                    oldpunchx = punchx
                    oldpunchy = punchy
                    if self.nanchecker(newrcsx, newrcsy) and self.checkangles(newrcsx, newrcsy):
                        self.pm.write_float(rcsengine + dwClientState_ViewAngles, newrcsx)
                        self.pm.write_float(rcsengine + dwClientState_ViewAngles + 0x4, newrcsy)
                else:
                    oldpunchx = 0.0
                    oldpunchy = 0.0
                    newrcsx = 0.0
                    newrcsy = 0.0
            except :
                pass
        
        self.pm.close_process()

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
