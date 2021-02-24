from Offsets import *
from ctypes import *
import ctypes
import pymem
import pymem.process
import time
import win32api
import random
import win32gui
import math
import winsound
sys.path.insert(1, "classes/")
from features_reads import read
import features_check

class sound_esp() :
    def __init__(self):
        try :
            pm = pymem.Pymem("csgo.exe")
        except :
            MessageBox = ctypes.windll.user32.MessageBoxW
            MessageBox(None, 'Could not find the csgo.exe process !', 'Error', 16)
            return

        client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
        engine = pymem.process.module_from_name(pm.process_handle, "engine.dll").lpBaseOfDll

        localPlayer = pm.read_int(client + dwLocalPlayer) # Get localPlayer pointer
        maxSoundESPDistance = 780 # Default: 780, decent distance tbh

        read("misc")

        while features_check.check.sound_esp :

            try :
                read("misc")
                closestPlayer = 99999.0

                for i in range(0, 32):
                    read("misc")
                    ent = pm.read_int(client + dwEntityList + i * 0x10)  # Get current entity based on for-loop variable i

                    if ent is 0x0:
                        break

                    entDormant = pm.read_int(ent + m_bDormant) # Get boolean that states whether glowCurrentPlayer entity is dormant or not

                    myTeamID = pm.read_int(localPlayer + m_iTeamNum) # Get the team ID of the localPlayer
                    entityBaseTeamID = pm.read_int(ent + m_iTeamNum)  # Get the team ID of the ent entity-

                    localPlayerX = pm.read_float(localPlayer + m_vecOrigin) # Get the X coordinate of the vecOrigin of the localPlayer
                    localPlayerY = pm.read_float(localPlayer + m_vecOrigin + 0x4) # Get the Y coordinate of the vecOrigin of the localPlayer
                    localPlayerZ = pm.read_float(localPlayer + m_vecOrigin + 0x8) # Get the Z coordinate of the vecOrigin of the localPlayer

                    entityX = pm.read_float(ent + m_vecOrigin) # Get the X coordinate of the vecOrigin of the ent
                    entityY = pm.read_float(ent + m_vecOrigin + 0x4) # Get the Y coordinate of the vecOrigin of the ent
                    entityZ = pm.read_float(ent + m_vecOrigin + 0x8) # Get the Z coordinate of the vecOrigin of the ent

                    distance = math.sqrt((pow((entityX - localPlayerX), 2) + pow((entityY - localPlayerY), 2) + pow((entityZ - localPlayerZ), 2))) # Get the distance between localPlayer and ent

                    if myTeamID != entityBaseTeamID and closestPlayer > distance: # If not on localPlayer team and team is either 2 or 3 and distance isnt 0 and distance is less than closestPlayer
                        closestPlayer = distance

                if closestPlayer < maxSoundESPDistance: # If closestPlayer isnt default value and closestPlayer is closer than maxSoundESPDistance
                    durMath = 1.000/maxSoundESPDistance # Generate baseline mathematical thingy - use ur brain
                    #winsound.Beep(2500, 2)
                    winsound.Beep(500, int((durMath * closestPlayer) * 1000))
            except :
                pass
        
        pm.close_process()
