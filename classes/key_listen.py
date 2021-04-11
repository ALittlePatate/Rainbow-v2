from pynput import mouse
from pynput.keyboard import Key, Listener
from pynput import keyboard
from functools import partial

class listen :
    def clean_listeners(self) :
        listen.key_listen.stop()
        listen.mouse_listener.stop()

    def on_press_key(self, key) :
        listen.key_key = key
        listen.clean_listeners(self)

    def on_click(self, x, y, button, pressed) :
        listen.button_button = button
        listen.clean_listeners(self)

    def key(self) :
        listen.key_key = None
        listen.button_button = None

        listen.key_listen = keyboard.Listener(on_press=partial(listen.on_press_key, Key))
        listen.key_listen.start()

        listen.mouse_listener = mouse.Listener(on_click=partial(listen.on_click, mouse.Button))
        listen.mouse_listener.start()

        while True :
            try :
                if listen.key_key :
                    return listen.key_key
            
            except :
                pass

            try :
                if listen.button_button :
                    return listen.button_button
            
            except :
                pass