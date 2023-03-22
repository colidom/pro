class MobilePhone:
    def __init__(self, manufacturer, screen_size, num_cores):
        self.manufacturer = manufacturer
        self.screen_size = screen_size
        self.num_cores = num_cores
        self.apps = []
        self.status = 0

    def power_on(self):
        self.status = 1

    def power_off(self):
        self.status = 0

    def install_app(self, *apps):
        for app in apps:
            if app not in self.apps:
                self.apps.append(app)

    def uninstall_app(self, app):
        if app in self.apps:
            self.apps.remove(app)


iphone = MobilePhone("iphone", 5.8, 2)
iphone.power_on()
iphone.install_app("Facebook", "Instagram")
iphone.install_app("Whatsapp", "Instagram")
print("Estado del teléfono: ", iphone.status)
print("Aplicaciones instaladas: ", iphone.apps)

iphone.uninstall_app("Facebook")
print("Aplicaciones instaladas: ", iphone.apps)

iphone.power_off()
print("Estado del teléfono: ", iphone.status)
