import kivy, sys, os
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.config import Config
Config.set('kivy','window_icon','images/rainbow.ico')
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
Config.set('graphics', 'width', '700')
Config.set('graphics', 'height', '400')
Config.set('graphics', 'resizable', False)

from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Rectangle, Color
from kivy.uix.spinner import Spinner
from kivy.uix.colorpicker import ColorPicker
from kivy.lang import Builder
from kivy.app import App

from kivy.uix.popup import Popup
from functools import partial
from kivy.config import Config
from write_config import write
from key_listen import listen
from read_config import read
from last import last
import datetime

from multiprocessing import *
import multiprocessing

sys.path.insert(1, "utils/")
from rank_reveal import rank_reveal

class draw(App):
    def rgba(self, string) :

        string = str(string)
        string = string.replace("[", "")
        string = string.replace("]", "")
        
        return tuple(map(float,string.split(', ')))

    def on_text(self, instance, value):
        self.config_to_save_name = value

    def on_enter(self, instance):
        self.name_of_config_to_write(self)

    def read_config(self, *args) :
        self.config_to_load_name = self.spinnerObject_configs.text

        last.write(self, self.config_to_load_name)
        read.config(self, self.config_to_load_name)

        ui_color_rgba = self.rgba(draw.ui_color)
        self.visuals.background_color = ui_color_rgba
        self.settings.background_color = ui_color_rgba
        self.aim.background_color = ui_color_rgba
        self.misc.background_color = ui_color_rgba
        self.config.background_color = ui_color_rgba

    def name_of_config_to_write(self, *args) :
        if ".ini" in self.config_name_input.text :
            self.config_name_to_save = self.config_name_input.text
        else :
            self.config_name_to_save = self.config_name_input.text+".ini"
        
        last.write(self, self.config_name_to_save)
        write.config(self, self.config_name_to_save)

    def save_config(self, *args) :
        if self.spinnerObject_configs.text != "Select" :
            self.config_name_to_save =  self.spinnerObject_configs.text
            write.config(self, self.config_name_to_save)
        
            last.write(self, self.config_name_to_save)

    def draw_config(self) :
        kv = """

FloatLayout:
    Label:
        text : "Save Config"
        size_hint: 0.1, 0.1
        pos_hint: {"top":0.9, "right": 0.65}
        font_size: 20
    Label:
        text : "Save as"
        size_hint: 0.1, 0.1
        pos_hint: {"top":0.7, "right": 0.38}
        font_size: 20
    Label:
        text : ".ini"
        size_hint: 0.1, 0.1
        pos_hint: {"top":0.7, "right": 0.66}
        font_size: 20
    Button:
        text : "save"
        size_hint: 0.08, 0.08
        pos_hint: {"top":0.69, "right": 0.77}
        on_release: app.name_of_config_to_write(self)

    Label:
        text : "Select Config"
        size_hint: 0.1, 0.1
        pos_hint: {"top":0.5, "right": 0.64}
        font_size: 20
    Button:
        text : "Load"
        size_hint: 0.08, 0.08
        pos_hint: {"top":0.3, "right": 0.7}
        on_release: app.read_config(self)
    Button:
        text : "Save"
        size_hint: 0.08, 0.08
        pos_hint: {"top":0.3, "right": 0.79}
        on_release: app.save_config(self)
"""     
        self.config_name_input = TextInput(multiline=False, pos_hint={"top":0.688, "right": 0.59}, size_hint=(0.2, 0.08))
        self.config_name_input.bind(on_text_validate=self.on_enter)
        self.config_name_input.bind(text=self.on_text)

        folder = "configs/"
        filelist = [fname for fname in os.listdir(folder) if fname.endswith('.ini')]
        self.spinnerObject_configs = Spinner(text ="Select")
        self.spinnerObject_configs.values = filelist
  
        self.spinnerObject_configs.size_hint = (0.1, 0.1) 
        self.spinnerObject_configs.pos_hint ={"top":0.30, "right": 0.58} 

        sm = Builder.load_string(kv)
        self.rl_config = RelativeLayout(size =(0, 0))
        self.rl_config.add_widget(self.config_name_input)
        self.rl_config.add_widget(self.spinnerObject_configs)
        self.rl_config.add_widget(sm)
        self.rl.add_widget(self.rl_config)

    def draw_settings(self) :
        kv = """

FloatLayout:
    Button:
        text : "Ui color"
        background_color : app.rgba(app.ui_color)
        size_hint: 0.1, 0.05
        pos_hint: {"top":0.8, "right": 0.65}
        on_release: app.draw_colorwheel("ui_color")
"""
        sm = Builder.load_string(kv)
        self.rl_settings = RelativeLayout(size =(0, 0))
        self.rl_settings.add_widget(sm)
        self.rl.add_widget(self.rl_settings)

    def on_change_slider(self, value, name) :
        if name == "slider1" :
            try :
                self.rl_aim.remove_widget(self.perfect_value_label)
            except :
                pass
            value = round(value, 1)
            self.perfect_value_label = Label(size_hint =( 0.1, 0.1), pos_hint ={"top":0.87, "right": 0.99}, text = str(value))
            draw.rcs_perfect = value
            self.rl_aim.add_widget(self.perfect_value_label)
        
        elif name == "slider2" :
            try :
                self.rl_aim.remove_widget(self.delay_value_label)
            except :
                pass
            value = round(value, 1)
            self.delay_value_label = Label(size_hint =( 0.1, 0.1), pos_hint ={"top":0.68, "right": 0.70}, text = str(value))
            draw.t_delay = value
            self.rl_aim.add_widget(self.delay_value_label)
        
        elif name == "slider3" :
            try :
                self.rl_misc.remove_widget(self.fov_value_label)
            except :
                pass
            value = round(value, 1)
            self.fov_value_label = Label(size_hint =( 0.1, 0.1), pos_hint ={"top":0.87, "right": 0.99}, text = str(value))
            draw.fov_value = value
            self.rl_misc.add_widget(self.fov_value_label)
        
        elif name == "slider4" :
            try :
                self.rl_misc.remove_widget(self.fake_lag_value_label)
            except :
                pass
            value = round(value, 1)
            self.fake_lag_value_label = Label(size_hint =( 0.1, 0.1), pos_hint ={"top":0.1, "right": 0.71}, text = str(value))
            draw.fake_lag_value = value
            self.rl_misc.add_widget(self.fake_lag_value_label)
        
        last.write(self, "temp.ini")
        write.config(self, "temp.ini")
    
    def spinners(self, spinner, text, *args):
        draw.sound = args[0]

        last.write(self, "temp.ini")
        write.config(self, "temp.ini")
        
    def rank_reveal(self) :
        multiprocessing.freeze_support()
        t_rank_reveal = Process(target = rank_reveal)
        t_rank_reveal.start()

    def draw_misc(self) :
        kv = """

FloatLayout:
    CheckBox:
        id : third_person_chk
        active : app.third_person
        size_hint: 0.1, 0.1
        pos_hint: {"top":0.9, "right": 0.48}
        on_press: app.on_checkbox_Active(third_person_chk.active, "third person")
    Label:
        text : "Third Person"
        size_hint: 0.1, 0.1
        pos_hint: {"top":0.9, "right": 0.38}
        font_size: 20
    Label:
        text : "FOV"
        size_hint: 0.1, 0.1
        pos_hint: {"top":0.9, "right": 0.68}
        font_size: 20
    CheckBox:
        id : fov_chk
        active : app.fov
        size_hint: 0.1, 0.1
        pos_hint: {"top":0.9, "right": 0.73}
        on_press: app.on_checkbox_Active(fov_chk.active, "fov")
    Label:
        text : "Fov value"
        size_hint: 0.1, 0.1
        pos_hint: {"top":0.93, "right": 0.85}
        font_size: 15
    Slider:
        id: slider3
        value : app.fov_value
        min: 0
        max: 180
        size_hint: 0.2, 0.1
        pos_hint: {"top":0.87, "right": 0.91}
        on_value: app.on_change_slider(self.value, "slider3")
    Label:
        text : "Hitsound"
        size_hint: 0.1, 0.1
        pos_hint: {"top":0.7, "right": 0.38}
        font_size: 20
    CheckBox:
        id : hitsound_chk
        active : app.hitsound
        size_hint: 0.1, 0.1
        pos_hint: {"top":0.7, "right": 0.456}
        on_press: app.on_checkbox_Active(hitsound_chk.active, "hitsound")
    Label:
        text : "Sound :"
        size_hint: 0.1, 0.1
        pos_hint: {"top":0.7, "right": 0.56}
        font_size: 18
    CheckBox:
        id : sound_esp_chk
        active : app.sound_esp
        size_hint: 0.1, 0.1
        pos_hint: {"top":0.55, "right": 0.456}
        on_press: app.on_checkbox_Active(sound_esp_chk.active, "sound esp")
    Label:
        text : "Sound ESP"
        size_hint: 0.1, 0.1
        pos_hint: {"top":0.55, "right": 0.37}
        font_size: 18
    CheckBox:
        id : no_flash_chk
        active : app.no_flash
        size_hint: 0.1, 0.1
        pos_hint: {"top":0.55, "right": 0.83}
        on_press: app.on_checkbox_Active(no_flash_chk.active, "no flash")
    Label:
        text : "No Flash"
        size_hint: 0.1, 0.1
        pos_hint: {"top":0.55, "right": 0.76}
        font_size: 18
    Label:
        text : "Bhop rage"
        size_hint: 0.1, 0.1
        pos_hint: {"top":0.4, "right": 0.38}
        font_size: 18
    CheckBox:
        id : bhop_rage_chk
        active : app.bhop_rage
        size_hint: 0.1, 0.1
        pos_hint: {"top":0.4, "right": 0.456}
        on_press: app.on_checkbox_Active(bhop_rage_chk.active, "bhop rage")
    Label:
        text : "Bhop legit"
        size_hint: 0.1, 0.1
        pos_hint: {"top":0.4, "right": 0.767}
        font_size: 18
    CheckBox:
        id : bhop_legit_chk
        active : app.bhop_legit
        size_hint: 0.1, 0.1
        pos_hint: {"top":0.4, "right": 0.84}
        on_press: app.on_checkbox_Active(bhop_legit_chk.active, "bhop legit")
    Label:
        text : "Show Money"
        size_hint: 0.1, 0.1
        pos_hint: {"top":0.26, "right": 0.38}
        font_size: 18
    CheckBox:
        id : show_money_chk
        active : app.show_money
        size_hint: 0.1, 0.1
        pos_hint: {"top":0.26, "right": 0.47}
        on_press: app.on_checkbox_Active(show_money_chk.active, "show money")
    Label:
        text : "Radar Hack"
        size_hint: 0.1, 0.1
        pos_hint: {"top":0.26, "right": 0.77}
        font_size: 18
    CheckBox:
        id : radar_chk
        active : app.radar
        size_hint: 0.1, 0.1
        pos_hint: {"top":0.26, "right": 0.856}
        on_press: app.on_checkbox_Active(radar_chk.active, "radar")
    Label:
        text : "Fake lag"
        size_hint: 0.1, 0.1
        pos_hint: {"top":0.13, "right": 0.38}
        font_size: 20
    CheckBox:
        id : fake_lag_chk
        active : app.fake_lag
        size_hint: 0.1, 0.1
        pos_hint: {"top":0.134, "right": 0.45}
        on_press: app.on_checkbox_Active(fake_lag_chk.active, "fake lag")
    Label:
        text : "Lag in ms"
        size_hint: 0.1, 0.1
        pos_hint: {"top":0.16, "right": 0.58}
        font_size: 15
    Slider:
        id: slider4
        value : app.fake_lag_value
        min: 0
        max: 900
        size_hint: 0.2, 0.1
        pos_hint: {"top":0.1, "right": 0.63}
        on_value: app.on_change_slider(self.value, "slider4")
    Button:
        text : "Rank Reveal"
        size_hint: 0.13, 0.1
        pos_hint: {"top":0.14, "right": 0.98}
        on_release: app.rank_reveal()
"""      
        self.rl_misc = RelativeLayout(size =(0, 0))

        folder = "sounds/"
        filelist = [fname for fname in os.listdir(folder)]
        self.spinnerObject = Spinner(text ="Select")
        self.spinnerObject.values = filelist
        self.spinnerObject.text = draw.sound
        self.spinnerObject.bind(text = partial(self.spinners, "sounds"))
  
        self.spinnerObject.size_hint = (0.1, 0.1) 
        self.spinnerObject.pos_hint ={"top":0.7, "right": 0.66} 

        self.thirdperson_key_but = Button(size_hint =(.12, .07), pos_hint ={"top":0.88, "right": 0.57}, text = draw.thirdperson_key, background_color='#00f7ff')
        self.thirdperson_key_but.bind(on_release=partial(self.key_listen_call, "thirdperson"))
        self.rl_misc.add_widget(self.thirdperson_key_but)

        self.fov_value_label = Label(size_hint =( 0.1, 0.1), pos_hint ={"top":0.87, "right": 0.99}, text = str(draw.fov_value))
        self.rl_misc.add_widget(self.fov_value_label)

        self.fake_lag_value_label = Label(size_hint =( 0.1, 0.1), pos_hint ={"top":0.1, "right": 0.71}, text = str(draw.fake_lag_value))
        self.rl_misc.add_widget(self.fake_lag_value_label)

        sm = Builder.load_string(kv)
        self.rl_misc.add_widget(self.spinnerObject)
        self.rl_misc.add_widget(sm)
        self.rl.add_widget(self.rl_misc)

    def draw_aim(self) : 
        kv = """

FloatLayout:
    CheckBox:
        id : aimbot_chk
        active : app.aimbot
        size_hint: 0.1, 0.1
        pos_hint: {"top":0.9, "right": 0.416}
        on_press: app.on_checkbox_Active(aimbot_chk.active, "aimbot")
    Label:
        text : "Aimbot"
        size_hint: 0.1, 0.1
        pos_hint: {"top":0.9, "right": 0.35}
        font_size: 20
    Label:
        text : "Triggerbot"
        size_hint: 0.1, 0.1
        pos_hint: {"top":0.7, "right": 0.346}
        font_size: 20
    CheckBox:
        id : triggerbot_chk
        active : app.triggerbot
        size_hint: 0.1, 0.1
        pos_hint: {"top":0.7, "right": 0.43}
        on_press: app.on_checkbox_Active(triggerbot_chk.active, "triggerbot")
    Label:
        text : "Delay in ms"
        size_hint: 0.1, 0.1
        pos_hint: {"top":0.75, "right": 0.57}
        font_size: 15
    Slider:
        id: slider2
        value : app.t_delay
        min: 0
        max: 600
        size_hint: 0.2, 0.1
        pos_hint: {"top":0.68, "right": 0.62}
        on_value: app.on_change_slider(self.value, "slider2")
    Label:
        text : "RCS"
        size_hint: 0.1, 0.1
        pos_hint: {"top":0.9, "right": 0.67}
        font_size: 20
    CheckBox:
        id : rcs_chk
        active : app.rcs
        size_hint: 0.1, 0.1
        pos_hint: {"top":0.9, "right": 0.72}
        on_press: app.on_checkbox_Active(rcs_chk.active, "rcs")
    Label:
        text : "Perfection percentage"
        size_hint: 0.1, 0.1
        pos_hint: {"top":0.95, "right": 0.85}
        font_size: 15
    Slider:
        id: slider1
        value : app.rcs_perfect
        size_hint: 0.2, 0.1
        pos_hint: {"top":0.87, "right": 0.91}
        on_value: app.on_change_slider(self.value, "slider1")
    Label:
        text : "Rapid Fire"
        size_hint: 0.1, 0.1
        pos_hint: {"top":0.5, "right": 0.35}
        font_size: 20
    CheckBox:
        id : rapid_fire_chk
        active : app.rapid_fire
        size_hint: 0.1, 0.1
        pos_hint: {"top":0.5, "right": 0.432}
        on_press: app.on_checkbox_Active(rapid_fire_chk.active, "rapid fire")
    Label:
        text : "Silent Aim"
        size_hint: 0.1, 0.1
        pos_hint: {"top":0.34, "right": 0.35}
        font_size: 20
    CheckBox:
        id : silent_aim_chk
        active : app.silent_aim
        size_hint: 0.1, 0.1
        pos_hint: {"top":0.34, "right": 0.43}
        on_press: app.on_checkbox_Active(silent_aim_chk.active, "Silent Aim")
    Label:
        text : "Crosshair hack"
        size_hint: 0.1, 0.1
        pos_hint: {"top":0.34, "right": 0.71}
        font_size: 20
    CheckBox:
        id : crosshair_chk
        active : app.crosshair
        size_hint: 0.1, 0.1
        pos_hint: {"top":0.34, "right": 0.82}
        on_press: app.on_checkbox_Active(crosshair_chk.active, "crosshair")
"""     

        self.rl_aim = RelativeLayout(size =(0, 0))

        self.rapid_fire_key_but = Button(size_hint =(.12, .07), pos_hint ={"top":0.486, "right": 0.52}, text = draw.rapid_fire_key, background_color='#00f7ff')
        self.rapid_fire_key_but.bind(on_release=partial(self.key_listen_call, "rapid fire"))
        self.rl_aim.add_widget(self.rapid_fire_key_but)

        self.silent_aim_key_but = Button(size_hint =(.12, .07), pos_hint ={"top":0.33, "right": 0.52}, text = draw.silent_aim_key, background_color='#00f7ff')
        self.silent_aim_key_but.bind(on_release=partial(self.key_listen_call, "silent aim"))
        self.rl_aim.add_widget(self.silent_aim_key_but)

        self.aimbot_key_but = Button(size_hint =(.12, .07), pos_hint ={"top":0.88, "right": 0.51}, text = draw.aimbot_key, background_color='#00f7ff')
        self.aimbot_key_but.bind(on_release=partial(self.key_listen_call, "aimbot"))
        self.rl_aim.add_widget(self.aimbot_key_but)

        self.triggerbot_key_but = Button(size_hint =(.12, .07), pos_hint ={"top":0.68, "right": 0.8}, text = draw.triggerbot_key, background_color='#00f7ff')
        self.triggerbot_key_but.bind(on_release=partial(self.key_listen_call, "triggerbot"))
        self.rl_aim.add_widget(self.triggerbot_key_but)

        self.perfect_value_label = Label(size_hint =( 0.1, 0.1), pos_hint ={"top":0.87, "right": 0.99}, text = str(draw.rcs_perfect))
        self.rl_aim.add_widget(self.perfect_value_label)
        
        self.delay_value_label = Label(size_hint =( 0.1, 0.1), pos_hint ={"top":0.68, "right": 0.70}, text = str(draw.t_delay))
        self.rl_aim.add_widget(self.delay_value_label)

        sm = Builder.load_string(kv)
        self.rl_aim.add_widget(sm)
        self.rl.add_widget(self.rl_aim)

    def key_listen_call(self, *args) :

        key = str(listen.key(self))
        key = key.replace("'", "")
 
        if args[0] == "rapid fire" :
            self.rapid_fire_key_but.text = key
            draw.rapid_fire_key = key
        
        if args[0] == "silent aim" :
            self.silent_aim_key_but.text = key
            draw.silent_aim_key = key
        
        if args[0] == "aimbot" :
            self.aimbot_key_but.text = key
            draw.aimbot_key = key
        
        if args[0] == "triggerbot" :
            self.triggerbot_key_but.text = key
            draw.triggerbot_key = key
        
        if args[0] == "thirdperson" :
            self.thirdperson_key_but.text = key
            draw.thirdperson_key = key
        
        last.write(self, "temp.ini")
        write.config(self, "temp.ini")


    def on_color(self, instance, value):

        if value != [1.0, 1.0, 1.0, 1] :
            if draw.name == "allies_glow" :
                draw.allies_glow_color = value
            elif draw.name == "ennemies_glow" :
                draw.ennemies_glow_color = value
            elif draw.name == "allies_chams" : 
                draw.allies_chams_color = value
            elif draw.name == "ennemies_chams" :
                draw.ennemies_chams_color = value

            elif draw.name == "ui_color" :
                draw.ui_color = value
                self.visuals.background_color = value
                self.settings.background_color = value
                self.aim.background_color = value
                self.misc.background_color = value
                self.config.background_color = value
        
        last.write(self, "temp.ini")
        write.config(self, "temp.ini")

    def draw_colorwheel(self, name) :
        draw.name = name
        clr_picker = ColorPicker(size_hint =(.5, .5), pos_hint ={"top":0.72, "right": 0.86})
        clr_picker.bind(color=self.on_color)

        if name == "ennemies_glow" :
            try :
                self.rl_visuals.remove_widget(self.rl_wheel_ennemies)
                self.rl_wheel_ennemies = None
                return
            except :
                self.rl_wheel_ennemies = RelativeLayout(size =(0, 0))
                self.rl_wheel_ennemies.add_widget(clr_picker)
                self.rl_visuals.add_widget(self.rl_wheel_ennemies)
        
        elif name == "allies_glow" :
            try :
                self.rl_visuals.remove_widget(self.rl_wheel_allies)
                self.rl_wheel_allies = None
                return
            except :
                self.rl_wheel_allies = RelativeLayout(size =(0, 0))
                self.rl_wheel_allies.add_widget(clr_picker)
                self.rl_visuals.add_widget(self.rl_wheel_allies)
        
        elif name == "ennemies_chams" :
            try :
                self.rl_visuals.remove_widget(self.rl_wheel_ennemies_chams)
                self.rl_wheel_ennemies_chams = None
                return
            except :
                self.rl_wheel_ennemies_chams = RelativeLayout(size =(0, 0))
                self.rl_wheel_ennemies_chams.add_widget(clr_picker)
                self.rl_visuals.add_widget(self.rl_wheel_ennemies_chams)
        
        elif name == "allies_chams" :
            try :
                self.rl_visuals.remove_widget(self.rl_wheel_allies_chams)
                self.rl_wheel_allies_chams = None
                return
            except :
                self.rl_wheel_allies_chams = RelativeLayout(size =(0, 0))
                self.rl_wheel_allies_chams.add_widget(clr_picker)
                self.rl_visuals.add_widget(self.rl_wheel_allies_chams)
            
        elif name == "ui_color" :
            try :
                self.rl_settings.remove_widget(self.rl_wheel_ui)
                self.rl_wheel_ui = None
                return
            except :
                self.rl_wheel_ui = RelativeLayout(size =(0, 0))
                self.rl_wheel_ui.add_widget(clr_picker)
                self.rl_settings.add_widget(self.rl_wheel_ui)

    def draw_visuals(self) :

        kv = """

FloatLayout:
    CheckBox:
        id : glow_chk
        active : app.glow_active
        size_hint: 0.1, 0.1
        pos_hint: {"top":0.9, "right": 0.45}
        on_press: app.on_checkbox_Active(glow_chk.active, "glow")
    Label:
        text : "Glow"
        size_hint: 0.1, 0.1
        pos_hint: {"top":0.9, "right": 0.39}
        font_size: 20
    Label:
        text : "Enemies"
        size_hint: 0.1, 0.1
        pos_hint: {"top":0.9, "right": 0.65}
        font_size: 20
    CheckBox:
        id : glow_chk_ennemies
        active : app.glow_ennemies
        size_hint: 0.1, 0.1
        pos_hint: {"top":0.9, "right": 0.57}
        on_press: app.on_checkbox_Active(glow_chk_ennemies.active, "glow_ennemies")
    Button:
        text : "Pick color"
        background_color : app.rgba(app.ennemies_glow_color)
        size_hint: 0.1, 0.05
        pos_hint: {"top":0.8, "right": 0.65}
        on_release: app.draw_colorwheel("ennemies_glow")
    Label:
        text : "Allies"
        size_hint: 0.1, 0.1
        pos_hint: {"top":0.9, "right": 0.9}
        font_size: 20
    CheckBox:
        id : glow_chk_allies
        active : app.glow_allies
        size_hint: 0.1, 0.1
        pos_hint: {"top":0.9, "right": 0.84}
        on_press: app.on_checkbox_Active(glow_chk_allies.active, "glow_allies")
    Button:
        text : "Pick color"
        background_color : app.rgba(app.allies_glow_color)
        size_hint: 0.1, 0.05
        pos_hint: {"top":0.8, "right": 0.9}
        on_release: app.draw_colorwheel("allies_glow")
    
    Label:
        text : "Based on health"
        size_hint: 0.1, 0.1
        pos_hint: {"top":0.83, "right": 0.39}
        font_size: 20
    CheckBox:
        id : glow_health_based
        active : app.glow_health_based
        size_hint: 0.1, 0.1
        pos_hint: {"top":0.83, "right": 0.52}
        on_press: app.on_checkbox_Active(glow_health_based.active, "glow_health_based")

    CheckBox:
        id : chams_chk
        active : app.chams_active
        size_hint: 0.1, 0.1
        pos_hint: {"top":0.2, "right": 0.45}
        on_press: app.on_checkbox_Active(chams_chk.active, "chams")
    Label:
        text : "Chams"
        size_hint: 0.1, 0.1
        pos_hint: {"top":0.2, "right": 0.38}
        font_size: 20
    Label:
        text : "Based on health"
        size_hint: 0.1, 0.1
        pos_hint: {"top":0.13, "right": 0.39}
        font_size: 20
    CheckBox:
        id : chams_health_based
        active : app.chams_health_based
        size_hint: 0.1, 0.1
        pos_hint: {"top":0.13, "right": 0.52}
        on_press: app.on_checkbox_Active(chams_health_based.active, "chams_health_based")
    Label:
        text : "Enemies"
        size_hint: 0.1, 0.1
        pos_hint: {"top":0.2, "right": 0.65}
        font_size: 20
    CheckBox:
        id : chams_chk_ennemies
        active : app.chams_ennemies
        size_hint: 0.1, 0.1
        pos_hint: {"top":0.2, "right": 0.57}
        on_press: app.on_checkbox_Active(chams_chk_ennemies.active, "chams_ennemies")
    Button:
        text : "Pick color"
        background_color : app.rgba(app.ennemies_chams_color)
        size_hint: 0.1, 0.05
        pos_hint: {"top":0.1, "right": 0.65}
        on_release: app.draw_colorwheel("ennemies_chams")
    Label:
        text : "Allies"
        size_hint: 0.1, 0.1
        pos_hint: {"top":0.2, "right": 0.9}
        font_size: 20
    CheckBox:
        id : chams_chk_allies
        active : app.chams_allies
        size_hint: 0.1, 0.1
        pos_hint: {"top":0.2, "right": 0.84}
        on_press: app.on_checkbox_Active(chams_chk_allies.active, "chams_allies")
    Button:
        text : "Pick color"
        background_color : app.rgba(app.allies_chams_color)
        size_hint: 0.1, 0.05
        pos_hint: {"top":0.1, "right": 0.9}
        on_release: app.draw_colorwheel("allies_chams")
"""

        sm = Builder.load_string(kv)
        self.rl_visuals = RelativeLayout(size =(0, 0))
        self.rl_visuals.add_widget(sm)
        self.rl.add_widget(self.rl_visuals)

    def on_checkbox_Active(self, isActive, *args) :
        if args[0] == "glow" :
            draw.glow_active = isActive
        elif args[0] == "chams" :
            draw.chams_active = isActive
        elif args[0] == "chams_allies" :
            draw.chams_allies = isActive
        elif args[0] == "chams_ennemies" :
            draw.chams_ennemies = isActive
        elif args[0] == "glow_allies" :
            draw.glow_allies = isActive
        elif args[0] == "glow_ennemies" :
            draw.glow_ennemies = isActive
        elif args[0] == "glow_health_based" :
            draw.glow_health_based = isActive
        elif args[0] == "chams_health_based" :
            draw.chams_health_based = isActive
        elif args[0] == "aimbot" :
            draw.aimbot = isActive
        elif args[0] == "triggerbot" :
            draw.triggerbot = isActive
        elif args[0] == "rcs" :
            draw.rcs = isActive
        elif args[0] == "rapid fire" :
            draw.rapid_fire = isActive
        elif args[0] == "Silent Aim" :
            draw.silent_aim = isActive
        elif args[0] == "crosshair" :
            draw.crosshair = isActive
        elif args[0] == "third person" :
            draw.third_person = isActive
        elif args[0] == "fov" :
            draw.fov = isActive
        elif args[0] == "fake lag" :
            draw.fake_lag = isActive
        elif args[0] == "hitsound" :
            draw.hitsound = isActive
        elif args[0] == "sound esp" :
            draw.sound_esp = isActive
        elif args[0] == "show money" :
            draw.show_money = isActive
        elif args[0] == "no flash" :
            draw.no_flash = isActive
        elif args[0] == "radar" :
            draw.radar = isActive
        elif args[0] == "bhop rage" :
            draw.bhop_rage = isActive
        elif args[0] == "bhop legit" :
            draw.bhop_legit = isActive
        
        last.write(self, "temp.ini")
        write.config(self, "temp.ini")

    def disable(self, instance, *args):
        if self.start == True :
            self.rl.remove_widget(self.rl_start_window)
            self.start = False

        if self.visuals.disabled == True :
            self.rl.remove_widget(self.rl_visuals)
        
        if self.aim.disabled == True :
            self.rl.remove_widget(self.rl_aim)
        
        if self.misc.disabled == True :
            self.rl.remove_widget(self.rl_misc)
        
        if self.settings.disabled == True :
            self.rl.remove_widget(self.rl_settings)
        
        if self.config.disabled == True :
            self.rl.remove_widget(self.rl_config)

        self.visuals.disabled = False
        self.aim.disabled = False
        self.misc.disabled = False
        self.config.disabled = False
        self.settings.disabled = False
        instance.disabled = True

        if self.settings.disabled == True :
            self.draw_settings()

        if self.visuals.disabled == True :
            self.draw_visuals()
        
        if self.aim.disabled == True :
            self.draw_aim()
        
        if self.misc.disabled == True :
            self.draw_misc()
        
        if self.config.disabled == True :
            self.draw_config()

    def build(self):
        self.start = True
        self.config_to_load_name = last.read(self)
        read.config(self, self.config_to_load_name)

        ui_color_rgba = self.rgba(draw.ui_color)

        self.title = 'Rainbow CSGO Cheat v1'
        Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
        Config.set('graphics', 'width', '700')
        Config.set('graphics', 'height', '400')
        Config.set('graphics', 'resizable', False)

        self.rl = RelativeLayout(size =(0, 0))

        self.visuals = Button(size_hint =(.2, .21), pos_hint ={'center_x':.100, 'center_y':.893}, text ="Visuals", background_color=ui_color_rgba)
        self.visuals.bind(on_press=partial(self.disable, self.visuals))

        self.aim = Button(size_hint =(.2, .2), pos_hint ={'center_x':.100, 'center_y':.690}, text ="Aim", background_color=ui_color_rgba)
        self.aim.bind(on_press=partial(self.disable, self.aim))

        self.misc = Button(size_hint =(.2, .2), pos_hint ={'center_x':.100, 'center_y':.493}, text ="Misc.", background_color=ui_color_rgba)
        self.misc.bind(on_press=partial(self.disable, self.misc))

        self.config = Button(size_hint =(.2, .2), pos_hint ={'center_x':.100, 'center_y':.296}, text ="Config", background_color=ui_color_rgba)
        self.config.bind(on_press=partial(self.disable, self.config))

        self.settings = Button(size_hint =(.2, .2), pos_hint ={'center_x':.100, 'center_y':.099}, text ="Settings", background_color=ui_color_rgba)
        self.settings.bind(on_press=partial(self.disable, self.settings))
        
        self.cheat_name_label = Label(size_hint =(.2, .2), pos_hint={"top":0.98, "right": 0.6}, text="Rainbow Recode v1 | Elapsed: ", font_size = 25)
        self.elapsed_label = Label(size_hint =(.2, .2), pos_hint={"top":0.98, "right": 0.9}, text=str(datetime.datetime.now().strftime('%H:%M:%S')), font_size = 25)
        self.status_label = Label(size_hint =(.2, .2), pos_hint={"top":0.7, "right": 0.44}, text="Status : ", font_size = 23)
        self.undetected_label = Label(size_hint =(.2, .2), pos_hint={"top":0.7, "right": 0.6}, text="Undetected", font_size = 23, color="green")

        self.rl_start_window = RelativeLayout(size =(0, 0))
        self.rl_start_window.add_widget(self.undetected_label)
        self.rl_start_window.add_widget(self.status_label)
        self.rl_start_window.add_widget(self.cheat_name_label)
        self.rl_start_window.add_widget(self.elapsed_label)

        self.rl.add_widget(self.rl_start_window)
        self.rl.add_widget(self.settings)
        self.rl.add_widget(self.config)
        self.rl.add_widget(self.visuals)
        self.rl.add_widget(self.aim)
        self.rl.add_widget(self.misc)

        return self.rl