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

    def install_app(self, apps):
        for app in apps:
            self.apps.append(app)

    def uninstall_app(self, app):
        self.apps.remove(app)


iPhone = MobilePhone("iPhone", 5.8, 2)
iPhone.power_on()
iPhone.install_app(["Facebook", "Instagram"])
iPhone.install_app(["Whatsapp"])
print("Estado del teléfono: ", iPhone.status)
print("Aplicaciones instaladas: ", iPhone.apps)

iPhone.uninstall_app("Facebook")
print("Aplicaciones instaladas: ", iPhone.apps)

iPhone.power_off()
print("Estado del teléfono: ", iPhone.status)
