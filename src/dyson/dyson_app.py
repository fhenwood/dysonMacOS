import rumps
from src.broadlink import dyson_am09

class DysonApp(object):
    def __init__(self):
        self.config = {
            "app_name": "Dyson",
            "icon": "icon.png",
            "connect": {"title":"Connect", "methods":self.connect},
            "connected": {"title":"Connected", "methods":self.connect},
            "on": {"title": "Turn On", "methods":self.turn_on, "key": "alt+x"},
            "off": {"title": "Turn Off", "methods": self.turn_on},
            "heat_up": {"title": "Heat Up 🔥", "methods":self.turn_heat_up},
            "heat_down": {"title": "Heat Down ❄️", "methods":self.turn_heat_down},
            "speed_up": {"title": "Speed Up", "methods":self.turn_speed_up},
            "speed_down": {"title": "Speed Down", "methods":self.turn_speed_down},
            "cold": {"title": "Cold ☃️", "methods":self.flip_heat_mode},
            "hot": {"title": "Hot 🌶", "methods":self.flip_heat_mode},
            "reset": {"title": "Reset State", "methods":self.reset_fan_state},
            "set_temp": {"title": 'Set Temperature', "methods":self.raw_temp},
            "set_speed" : {"title":'Set Speed', "methods":self.raw_speed},
            "spin": {"title":'Spin', "methods":self.turn_spin},
        }
        self.menu_items = {
            "connect": rumps.MenuItem(title=self.config["connect"]["title"], callback=self.config["connect"]["methods"]),
            "on": rumps.MenuItem(title=self.config["on"]["title"], callback=None, key=self.config["on"]["key"]),
            "heat_up": rumps.MenuItem(title=self.config["heat_up"]["title"], callback=None),
            "heat_down": rumps.MenuItem(title=self.config["heat_down"]["title"], callback=None),
            "speed_up": rumps.MenuItem(title=self.config["speed_up"]["title"], callback=None),
            "speed_down": rumps.MenuItem(title=self.config["speed_down"]["title"], callback=None),
            "cold": rumps.MenuItem(title=self.config["cold"]["title"], callback=None),
            "set_temp": rumps.MenuItem(title=self.config["set_temp"]["title"], callback=None),
            "set_speed": rumps.MenuItem(title=self.config["set_speed"]["title"], callback=None),
            "tempeature_lists":self.list_temps(),
            "speed_lists": self.list_speeds(),
            "reset": rumps.MenuItem(title=self.config["reset"]["title"], callback=None),
            "spin": rumps.MenuItem(title=self.config["spin"]["title"], callback=None),
        }

        self.app = rumps.App(self.config["app_name"])
        self.set_up_menu() 

        self.app.menu = [self.menu_items["connect"],
        None,
         self.menu_items["on"],
         self.menu_items["reset"],
         None,
         [self.menu_items["set_temp"],
                self.menu_items["tempeature_lists"]], 
         [self.menu_items["set_speed"],
                self.menu_items["speed_lists"]],
        None,
         self.menu_items["cold"],
         self.menu_items["spin"],
        None,
         self.menu_items["heat_up"], 
         self.menu_items["heat_down"], 
         self.menu_items["speed_up"], 
         self.menu_items["speed_down"], 
         ]

        self.menu_flip = ["on", "heat_up", "heat_down", "speed_up", "speed_down", "cold", "spin", "reset"]
        self.dyson = None
        self.connect(None)

    def set_up_menu(self):
        self.app.icon = self.config["icon"]

    def connect(self, sender):
        print('hi')

        if self.menu_items["connect"].title == self.config["connect"]["title"]:
            self.dyson = dyson_am09()
            self.menu_items["connect"].title = self.config["connected"]["title"]
            self.menu_items["connect"].state = 1

            '''Switch on callbacks'''
            for i in self.menu_flip:
                self.menu_items[i].set_callback(self.config[i]["methods"])

            for i in self.menu_items["tempeature_lists"]:
                i.set_callback(self.config["set_temp"]["methods"])

            for i in self.menu_items["speed_lists"]:
                i.set_callback(self.config["set_speed"]["methods"])
            
        else:
            self.menu_items["connect"].title = self.config["connect"]["title"]
            self.menu_items["connect"].state = 0
            self.dyson = None

            '''Switch off callbacks'''
            for i in self.menu_flip:
                self.menu_items[i].set_callback(None)

            for i in self.menu_items["tempeature_lists"]:
                i.set_callback(None)

            for i in self.menu_items["speed_lists"]:
                i.set_callback(None)

    def turn_on(self, sender):
        self.dyson.press("ON")
        if self.menu_items["on"].title ==  self.config["off"]["title"]:
            self.menu_items["on"].title = self.config["on"]["title"]
        else:
            self.menu_items["on"].title = self.config["off"]["title"]

    def turn_heat_up(self, sender):
        self.dyson.press("TEMP UP")
        if self.menu_items["cold"].title ==  self.config["cold"]["title"]:
            self.menu_items["cold"].title = self.config["hot"]["title"]
    
    def turn_heat_down(self, sender):
        self.dyson.press("TEMP DOWN")
        if self.menu_items["cold"].title  ==  self.config["cold"]["title"]:
            self.menu_items["cold"].title = self.config["hot"]["title"]

    def turn_speed_up(self, sender):
        self.dyson.press("SPEED UP")
    
    def turn_speed_down(self, sender):
        self.dyson.press("SPEED DOWN")

    def turn_spin(self, sender):
        self.dyson.press("SPIN")

    def flip_heat_mode(self, sender):
        self.dyson.press("COLD")
        print(self.menu_items["cold"].title)
        print(self.config["cold"]["title"])

        if self.menu_items["cold"].title == self.config["cold"]["title"]:
            self.menu_items["cold"].title = self.config["hot"]["title"]
            self.app.title = "❄️"
        else:
            self.menu_items["cold"].title = self.config["cold"]["title"]

    def reset_fan_state(self, sender):
        if self.menu_items["on"].title == self.config["on"]["title"]:
            self.turn_on(None)
        self.dyson.reset_state()
        self.turn_on(None)
        self.menu_items["cold"].title  = self.config["cold"]["title"]
        self.app.title = "🌶"

    def list_temps(self):
        temps = []
        for i in range(1,38):
            temps.append(rumps.MenuItem(title=(str(i) + ' °C')))
        return temps

    def list_speeds(self):
        speeds = []
        for i in range(1, 11):
            speeds.append(rumps.MenuItem(title=str(i)))
        return speeds

    def raw_temp(self, sender):
        print(sender.title)
        self.app.title = sender.title
        temp = int(sender.title[:-3])
        self.dyson.custom_temp(tempature=temp)

    def raw_speed(self, sender):
        print(sender.title)
        speed = int(sender.title)
        self.dyson.custom_speed(speed)

    def run(self):
        self.app.run()

# if __name__ == '__main__':
#     app = DysonApp()
#     app.run()
    
