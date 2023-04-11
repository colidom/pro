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
        self.apps = ["Candy Crash", "Music"]
        self.status = False
        self.battery = 20
        self.song_playing = False

    def show_info(self):
        print("==============Phone State=====================")
        print("🏭", f"Brand: {self.manufacturer}")
        print("📱", f"Screen size: {self.screen_size}")
        print("❤️ ", f"Core numbers: {self.num_cores}")
        print("🧮", f"Installed apps: {self.apps}")
        print("🔋", f"Battery status: {round(self.battery)}%")
        print("🔄", f"Power status: {self.status}")
        print("⏯️ ", f"Music playing: {self.song_playing}")
        print("================================================")

    def switch(self):
        if self.status:
            self.battery -= POWER_CONSUMPTION_OFF
            print("🔴 Swiching OFF the phone.")
        else:
            self.battery -= POWER_CONSUMPTION_ON
            print("🟢 Swiching ON the phone.")
        self.status = not self.status

    def install_app(self, *apps):
        if self.status:
            if self.battery:
                for app in apps:
                    if app not in self.apps:
                        self.apps.append(app)
                    self.battery -= POWER_CONSUMPTION_INSTALL
                    print(f"✅ Application {app.upper()} has been installed successfully")
            else:
                print("❌ Install Error: Not enough battery.")
        else:
            print("❌ Install Error: Please turn on the phone.")

    def update_app(self, app):
        if self.status and self.battery:
            if app in self.apps:
                current_app = self.apps.index(app)
                self.apps[current_app] += " >>>>> (updated)"
                print(f"✅ Application {app.upper()} has been updated successfully")
                self.battery -= POWER_CONSUMPTION_INSTALL
            else:
                print("❌ Update error: The application you are trying to update is not installed.")
        else:
            print("❌ Update error: The phone is not switched ON or does not have enough battery.")

    def uninstall_app(self, app):
        if self.status:
            if app in self.apps:
                self.apps.remove(app)
                print(f"✅ Application {app.upper()} has been uninstalled successfully")
                self.battery -= POWER_CONSUMPTION_UNINSTALL
            else:
                print(f"❌ Uninstall Error: {app.upper()} application is not installed in this phone")
                self.battery -= POWER_CONSUMPTION_UNINSTALL

    def recharge_battery(self, power):
        print("🔋", "Chagning battery")
        self.battery += power

    def play_music(self, song_name, /, *, duration):
        if self.status:
            if self.battery:
                if duration <= self.battery / POWER_CONSUMPTION_MUSIC:
                    print("⏯️ ", f"You're playing: '{song_name}' song")
                    self.song_playing = song_name
                    self.battery -= POWER_CONSUMPTION_MUSIC * duration
                else:
                    print("❌ Insufficient battery power to play the song for its full duration.")
                    self.song_playing = False
            else:
                print("❌ Insufficient battery power to play the song.")
        else:
            print("❌ Cannot play music while the phone is turned off.")


iphone = MobilePhone("iPhone", 5.8, 2)
iphone.show_info()
iphone.switch()
iphone.install_app("Facebook", "Instagram")
iphone.install_app("Whatsapp", "Messenger")
print("📲",f"Current Apps: {iphone.apps}")
iphone.uninstall_app("Facebook")
iphone.uninstall_app("Tinder")
print("📲",f"Current Apps: {iphone.apps}")
iphone.update_app("Whatsapp")
iphone.recharge_battery(20)
iphone.play_music("Symphony of a devil", duration=6.22)
iphone.recharge_battery(5)
iphone.play_music("La Macarena", duration=5.12)
iphone.switch()
iphone.show_info()
