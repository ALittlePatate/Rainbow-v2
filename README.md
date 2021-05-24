# Recode
The recode ui is powered by [Kivy](https://kivy.org/doc/stable/api-kivy.modules.html) so it's much much cleaner.
It includes ui, chams and glow colors customization with a much better way to write and read configs (thanks [Configparser](https://docs.python.org/3/library/configparser.html) !).
It's also more stable and more user-friendly.

# Rainbow Cheat CS:GO
A public csgo legit cheat made in [Python](https://www.python.org/) based on cheats found on [Github](https://github.com).
I did all the tests with Python 3.6.8.
All the offsets are from [the hazedumper github page](https://github.com/frk1/hazedumper) (except for some of the netvars) so if the cheat is not working, retry later !
If you want to contribute, be free to send me a message on discord (see contact) !

# Read this (important)
I can't update the cheat every weeks/days, so if someone who's interested in want to work with me, i'll be glad to accept :)
I played with this cheat ~400 hour online on VAC servers.
The cheat is undetectable by VAC (updated the 24/05/2021)

# Installation
### Make sure to have at least [Python 3.6](https://www.python.org/downloads/release/python-360/) and pip added to your PATH and be in the same directory as the cheat
### If you have issues try to update pip
```
pip install -r requirements.txt
```

# Usage
## If you are too lazy to use [python](https://www.python.org/downloads/release/python-360/), download the compiled version of the cheat (soon). Please note that you won't have the crosshair hack.
```
python Rainbow.py
```

# Features
* Fully customizable Chams
* Rank Reveal [BETA]
* Hitsound
* Sound ESP
* Silent Aim
* FOV hack
* Third Person
* Rapid fire
* semi-legit Aimbot
* Crosshair hack
* Money hack
* Radar hack
* RCS (Recoil Control System)
* Triggerbot
* Fully customizable Glow hack
* Auto bhop legit and rage
* No flash
* Fake lag
* Skinchanger [BETA]
* Knifechanger [BETA]

# Contact
If you have ideas of improvements or if you want to report a bug please make a message on [Issues](https://github.com/ALittlePatate/Rainbow-v2/issues) or message me on [Discord](https://discord.com/) at Dogecoin#1252.

# Known issues
* The silent aim isn't very acurate sometimes
* FOV is glitchy when un-scoping
* The aimbot isn't very legit
* Some fps issues (maybe due to Kivy ?)
* The crosshair hack can make your game minimize the first time you use it
* The rank reveal isn't very accurate (sometimes it's one rank bellow or above the real one)
* The knife model won't change twice in the same game unless you retry
* The knives and weapon skins will not always be applied (timing and optimization issue)

# Changelog
# Recode V2.1
* Improved stability
* Added a knifechanger
* The skinchanger/knifechanger are more optimized
* The rank reveal won't crash anymore (but still not really working)
* The Offsets are changed so they work with the knifechanger

# Recode v2
* Improved stability
* Added a fully customizable skinchanger ! (Big thanks to [naaax123](3https://github.com/naaax123) for letting me use his code for the base !)

# Recode v1
* Improved compatibility and stability
* New ui powered by kivy (GPU based)
* The ui color is customizable
* New config reading/writing system
* Added a "Save config" button so you don't have to create a new one
* No more global variables !
* The code is better written (thanks [@teoformartel](https://github.com/teoformartel) for saying to me to use classes !)
* Now for >Python 3.5
* Now a part of the netvars is gathered by the cheat itself
* All the changes of the parameters are updated in real time !
* The glow looks way better (kinda like internal)
* Added customization to the colors of the chams and of the glow
* Added a fake lag
* Now the rank reveal is in a proper window
* You can now choose the kill sound and add you sounds to it !
* Now the radar and no flash reset works !



## V4.04
* The Rank Reveal has now a proper window
* The crosshair hack is now on only when you have a sniper and you are not scoping
* Added a legit bhop

## V4.03
* Added a Rank Reveal [BETA]
* Added some Chams
* Added a Hitsound
* Added a Sound ESP
* Added a Silent Aim
* Fixed the FOV
* Now the color of the wallhack changes in function of the player's health

## V3.03
* Added a rcs perfect percentage config

## V3.02
* Added a FOV hack (need a fix)
* Added a third person hack
* Added the third person configuration
* Added a rapid fire
* Added the rapid fire configuration
* Added a rage mode (completely broke, don't use it)
* Added a legit aimbot
* Added a crosshair hack
* Fixed the configs exports
* The money hack is now optimised, no more delay to set !
* Now you can change a parameter and it will take affect immediatly, no more export/reload config !

## V2.01
* Added a money hack (you can see enemy money)
* Added money hack configuration (refresh delay)
* Added radar hack
* Added RCS (Recoil Control System)
* Added an Aimbot
* Added aimbot configuration (toggle key, fov, smooth)
* Fixed the triggerbot

## V1.01
* Added a "current value" label into the triggerbot configuration.
* Added commentaries.
* Deleted an useless function

## V1.0
* Aimbot (Not added yet)
* Wallhack (the configuration isn't done yet)
* Triggerbot (all the features are working)
* Auto Bhop (working fine)
* No Flash (working fine)
* Configurations loader/exporter (work only for the triggerbot, i'll add the other cheats in a next update)
