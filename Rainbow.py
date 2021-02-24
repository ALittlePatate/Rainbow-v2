import sys, os
from multiprocessing import *
import multiprocessing
sys.path.insert(1, "classes/")
from features_check import check

if __name__ == "__main__" :

    from get_netvars import get_netvars
    print("Dumping the netvars, hold a sec...")
    get_netvars()
    print("Netvars dumped !")

    multiprocessing.freeze_support()
    t_features = Process(target = check)
    t_features.start()

    from ui import draw as window
    window().run()

    t_features.terminate()
