POWER_CONSUMPTION_ON = 5
POWER_CONSUMPTION_OFF = 2.5
POWER_CONSUMPTION_INSTALL = 1
POWER_CONSUMPTION_UNINSTALL = 1


class MobilePhone:
    def __init__(self, manufacturer, screen_size, num_cores):
        self.manufacturer = manufacturer
        self.screen_size = screen_size
        self.num_cores = num_cores
        self.apps = ["Candy Crash", "Messenger"]
        self.status = False
        self.battery = 50

    def switch(self):
        if self.status:
            self.battery -= POWER_CONSUMPTION_OFF
        else:
            self.battery -= POWER_CONSUMPTION_ON
        self.status = not self.status

    def install_app(self, *apps):
        if self.status == False and self.battery:
            for app in apps:
                if app not in self.apps:
                    self.apps.append(app)
                    self.battery -= POWER_CONSUMPTION_INSTALL
                else:
                    self.battery -= POWER_CONSUMPTION_INSTALL
        else:
            self.battery -= POWER_CONSUMPTION_INSTALL

    def uninstall_app(self, app):
        if self.status == False:
            if app in self.apps:
                self.apps.remove(app)
                self.battery -= POWER_CONSUMPTION_UNINSTALL
            else:
                self.battery -= POWER_CONSUMPTION_UNINSTALL

    def recharge_battery(self, power):
        self.battery += power


iphone = MobilePhone("iphone", 5.8, 2)
iphone.switch()
iphone.install_app("Facebook", "Instagram")
iphone.install_app("Whatsapp", "Messenger")
print("Estado del teléfono: ", iphone.status)
print("Aplicaciones instaladas: ", iphone.apps)

iphone.uninstall_app("Facebook")
print("Aplicaciones instaladas: ", iphone.apps)

iphone.switch()
print("Estado del teléfono: ", iphone.status)

print("Batería del teléfono: ", iphone.battery)
iphone.recharge_battery(5)
print("Batería del teléfono: ", iphone.battery)
