import pymem
import pymem.process
import time
import ctypes
from tkinter import *
from Offsets import *

class rank_reveal() :
    def __init__(self):
        try :
            pm = pymem.Pymem("csgo.exe")
        except :
            MessageBox = ctypes.windll.user32.MessageBoxW
            MessageBox(None, 'Could not find the csgo.exe process !', 'Error', 16)
            return
        
        top = Tk()
        w = 320
        h = 300
        ws = top.winfo_screenwidth()
        hs = top.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        top.geometry('%dx%d+%d+%d' % (w, h, x, y))
        top.title('Rank Reveal')
        top.iconbitmap("images/re.ico")
        top.config(background='#f0f0f0')
        scrollbar = Scrollbar(top)
        scrollbar.pack(side=RIGHT, fill=Y)
        listbox = Listbox(top)
        listbox.pack(expand=1, fill=BOTH)
        listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=listbox.yview)

        client = pymem.process.module_from_name(pm.process_handle, "client.dll")
        engine = pymem.process.module_from_name(pm.process_handle, "engine.dll")
    
        ranks = ["Unranked" , 
                    "Silver I",
                    "Silver II",
                    "Silver III",
                    "Silver IV",
                    "Silver Elite",
                    "Silver Elite Master",
                    "Gold Nova I",
                    "Gold Nova II",
                    "Gold Nova III",
                    "Gold Nova Master",
                    "Master Guardian I",
                    "Master Guardian II",
                    "Master Guardian Elite",
                    "Distinguished Master Guardian",
                    "Legendary Eagle",
                    "Legendary Eagle Master",
                    "Supreme Master First Class",
                    "The Global Elite"]
        for i in range(0, 32):
            entity = pm.read_int(client.lpBaseOfDll + dwEntityList + i * 0x10)

            if entity:
                entity_team_id = pm.read_int(entity + m_iTeamNum)
                entity_i = pm.read_int(client.lpBaseOfDll + dwLocalPlayer)
                if entity_team_id != pm.read_int(entity_i + m_iTeamNum):
                    player_info = pm.read_int(
                        (pm.read_int(engine.lpBaseOfDll + dwClientState)) + dwClientState_PlayerInfo)
                    player_info_items = pm.read_int(pm.read_int(player_info + 0x40) + 0xC)
                    info = pm.read_int(player_info_items + 0x28 + (i * 0x34))
                    playerres = pm.read_int(client.lpBaseOfDll + dwPlayerResource)
                    rank = pm.read_int(playerres + m_iCompetitiveRanking + i * 4)

                    if pm.read_string(info + 0x10) != 'GOTV':
                        
                        try :
                            listbox.insert(END, pm.read_string(info + 0x10) + "   -->   " + ranks[rank])
                        except :
                            listbox.insert(END, pm.read_string(info + 0x10).encode('iso-8859-1').decode() + "   -->   " + ranks[rank])
                    
        top.mainloop()
        pm.close_process()