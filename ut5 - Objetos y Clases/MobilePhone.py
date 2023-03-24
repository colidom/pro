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

    def show_info(self):
        print(f"Fabricante: {self.manufacturer}")
        print(f"Tamaño de pantalla: {self.screen_size}")
        print(f"Número de núcleos: {self.num_cores}")
        print(f"Aplicaciones instaladas: {self.apps}")
        print(f"Estado de la batería: {self.battery}%")
        print(f"Encendido: {self.status}")

    def switch(self):
        if self.status:
            self.battery -= POWER_CONSUMPTION_OFF
        else:
            self.battery -= POWER_CONSUMPTION_ON
        self.status = not self.status

    def install_app(self, *apps):
        if self.status == True and self.battery:
            for app in apps:
                if app not in self.apps:
                    self.apps.append(app)
                    self.battery -= POWER_CONSUMPTION_INSTALL
                else:
                    self.battery -= POWER_CONSUMPTION_INSTALL
        else:
            self.battery -= POWER_CONSUMPTION_INSTALL

    def update_app(self, app):
        if self.status and self.battery:
            if app in self.apps:
                self.apps.remove(app)
                self.apps.append(app + " (actualizada)")
                self.battery -= POWER_CONSUMPTION_INSTALL
            else:
                print("La aplicación no está instalada.")
        else:
            print("El teléfono no está encendido o no tiene suficiente batería.")

    def uninstall_app(self, app):
        if self.status == True:
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
iphone.uninstall_app("Facebook")

# iphone.switch()
# iphone.recharge_battery(5)
iphone.update_app("Whatsapp")
iphone.show_info()
