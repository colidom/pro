class OS:
    RAM_CONSUMPTION = 1
    STATUS = {"ON": True, "OFF": False}

    times_installed = 0

    def __init__(self, name, version, kernel, ram) -> None:

        self.name = name
        self.version = version
        self.ram = ram
        self.kernel = kernel
        self.filesystem = {
            "/": ["/pro"],
            "/downloads": ["/python", "/php", "/java"],
            "documents": ["exam", "exercises"],
            "pictures": [],
        }
        self.status = False
        self.booted = False
        self.processes = []

    @property
    def ram_consumption(self) -> float:
        consum = 0
        for _ in enumerate(self.processes):
            consum += self.RAM_CONSUMPTION * 0.5
        return consum

    @classmethod
    def total_installations(cls) -> None:
        OS.times_installed += 1

    def get_filesystem_tree(self) -> dict[str, list | object]:
        return self.filesystem

    def boot_system(self) -> None:
        if self.status:
            self.booted = True
            self.status = self.STATUS["ON"]
            print("Booting the system!")
        else:
            self.booted = True
            self.status = self.STATUS["OFF"]
            print("Turning OFF the system!")

        self.status = not self.status

    def system_status(self) -> bool:
        return self.status

    @staticmethod
    def audit(method):
        def wrapper(self, *args, **kwargs):
            process_method = method(self, *args, **kwargs)
            print(f"Process {self.processes} running by method '{method.__name__}'")
            return process_method

        return wrapper

    @audit
    def run_processes(self, *processes: list) -> None:
        for process in processes:
            self.processes.append(process)


operating_system = OS("pythonOS", "1.0", "5.10.0-19-amd64", 16)
operating_system.total_installations()
operating_system.total_installations()
operating_system.total_installations()
print(f"Filesystem structure: {operating_system.get_filesystem_tree()}")
print(f"OS has been installed {operating_system.times_installed} times so far!")
operating_system.boot_system()
print(f"Booted System: {operating_system.system_status()}")
operating_system.run_processes("apache", "php")
print(f"Ram consumption: {operating_system.ram_consumption}")
operating_system.run_processes("MySQL")
operating_system.boot_system()
print(f"Ram consumption: {operating_system.ram_consumption}")
print(f"Booted System: {operating_system.system_status()}")
