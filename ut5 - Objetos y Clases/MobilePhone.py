POWER_CONSUMPTION_ON = 5
POWER_CONSUMPTION_OFF = 2.5
POWER_CONSUMPTION_INSTALL = 1
POWER_CONSUMPTION_UNINSTALL = 1
POWER_CONSUMPTION_MUSIC = 3


class MobilePhone:
    def __init__(self, manufacturer, screen_size, num_cores):
        self.manufacturer = manufacturer
        self.screen_size = screen_size
        self.num_cores = num_cores
        self.apps = ["Candy Crash", "Messenger"]
        self.status = False
        self.battery = 0

    def show_info(self):
        print("🏭", f"Brand: {self.manufacturer}")
        print("📱", f"Screen size: {self.screen_size}")
        print("❤️ ", f"Core numbers: {self.num_cores}")
        print("🧮", f"Installed apps: {self.apps}")
        print("🔋", f"Battery status: {self.battery}%")
        print("🔄", f"Power status: {self.status}")
        print("=======================================")

    def switch(self):
        if self.status:
            self.battery -= POWER_CONSUMPTION_OFF
        else:
            self.battery -= POWER_CONSUMPTION_ON
        self.status = not self.status

    def install_app(self, *apps):
        if self.status and self.battery:
            for app in apps:
                if app not in self.apps:
                    self.apps.append(app)
                    self.battery -= POWER_CONSUMPTION_INSTALL
                    print(f"✅ Application {app} has been installed successfully")
                else:
                    self.battery -= POWER_CONSUMPTION_INSTALL
        else:
            self.battery -= POWER_CONSUMPTION_INSTALL

    def update_app(self, app):
        if self.status and self.battery:
            if app in self.apps:
                self.apps.remove(app)
                self.apps.append(app + " (updated)")
                self.battery -= POWER_CONSUMPTION_INSTALL
            else:
                print(
                    "❌ Update error: The application you are trying to update is not installed."
                )
        else:
            print(
                "❌ Update error: The phone is not switched ON or does not have enough battery."
            )

    def uninstall_app(self, app):
        if self.status == True:
            if app in self.apps:
                self.apps.remove(app)
                self.battery -= POWER_CONSUMPTION_UNINSTALL
            else:
                self.battery -= POWER_CONSUMPTION_UNINSTALL

    def recharge_battery(self, power):
        print("🔋", "Chagning battery")
        self.battery += power

    def play_music(self, song_name, duration):
        if self.status == True:
            if self.battery > 0:
                print("⏯️ ", f"Playing song: {song_name} 🎵")
                self.current_song = song_name
                self.battery -= POWER_CONSUMPTION_MUSIC * duration
            else:
                print("❌ Insufficient battery power to play the song.")


iphone = MobilePhone("iPhone", 5.8, 2)
iphone.install_app("Facebook", "Instagram")
iphone.install_app("Whatsapp", "Messenger")
iphone.uninstall_app("Facebook")

# iphone.switch()
iphone.update_app("Whatsapp")
iphone.show_info()

iphone.recharge_battery(10)
iphone.play_music("Symphony of a devil", 6.22)
iphone.show_info()
