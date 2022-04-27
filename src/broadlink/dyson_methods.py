import broadlink
import json
import base64
import time

class dyson_am09:
    def __init__(self):
        print('Connecting')
        self.devices = broadlink.discover()
        self.device = self.devices[0]
        self.device.auth()
        print('Connected')
        self.buttons = self.convert_buttons_to_bytes(self.return_button_str())
        
    def return_button_str(self):
        with open('dyson_am09.json') as json_file:
            buttons = json.load(json_file)
        return buttons
    
    def convert_buttons_to_bytes(self,buttons):
        for button in buttons.keys():
            buttons[button] = base64.b64decode(buttons[button])
        return buttons
    
    def press(self, button):
        print(f'Pressing {button}')
        self.device.send_data(self.buttons[button])
    
    def reset_state(self):
        for x in range(37):
            self.press('TEMP UP')
            time.sleep(0.2)

        for x in range(10):
            self.press('SPEED DOWN')
            time.sleep(0.2)

    def custom_temp(self, tempature):
        print('yup')
        for x in range(37):
            self.press('TEMP UP')
            time.sleep(0.2)
        for x in range((37-tempature)):
            self.press('TEMP DOWN')
            time.sleep(0.2)

    def custom_speed(self, speed):
        for x in range(10):
            self.press('SPEED DOWN')
            time.sleep(0.2)

        for x in range(speed-1):
            self.press('SPEED UP')
            time.sleep(0.2)
            
    def set_temp(self, tempature, speed, hot=True):
        self.reset_state()
        for x in range(speed-1):
            self.press('SPEED UP')
            time.sleep(0.2)
        if hot:
            for x in range((37-tempature)):
                self.press('TEMP DOWN')
                time.sleep(0.2)
        else:
            self.press("COLD")


