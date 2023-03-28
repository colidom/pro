class OS:

    times_installed = 0

    def __init__(self, name, version, kernel, ram) -> None:

        self.name = name
        self.version = version
        self.ram = ram
        self.kernel = kernel
        self.filesystem = []
        self.status = False
        self.booted = False

    @property
    def required_ram(self) -> float:
        return 0.2 * self.ram

    @classmethod
    def total_installations(cls) -> None:
        OS.times_installed += 1


operating_system = OS("pythonOS", "1.0", "5.10.0-19-amd64", 16)
operating_system.filesystem = ["/home", "/downloads", "/documents"]
operating_system.total_installations()
operating_system.total_installations()
operating_system.total_installations()
print(f"OS has been installed {operating_system.times_installed} times so far!")
