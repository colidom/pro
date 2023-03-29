class OS:

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
    def required_ram(self) -> float:
        return 0.2 * self.ram

    @classmethod
    def total_installations(cls) -> None:
        OS.times_installed += 1

    def get_filesystem_tree(self) -> dict[str, list | object]:
        return self.filesystem

    def boot_system(self):
        self.booted = True
        print("Booting the system!")

    @staticmethod
    def audit(method):
        def wrapper(self, *args, **kwargs):
            process_method = method(self, *args, **kwargs)
            print(f"Process {self.processes} running by method '{method.__name__}'")
            return process_method

        return wrapper

    @audit
    def run_processes(self, *processes):
        for process in processes:
            self.processes.append(process)

    @audit
    def list_process(self):
        for process in self.processes:
            print(process)
            pass


operating_system = OS("pythonOS", "1.0", "5.10.0-19-amd64", 16)
operating_system.total_installations()
operating_system.total_installations()
operating_system.total_installations()
print(f"Filesystem structure: {operating_system.get_filesystem_tree()}")
print(f"OS has been installed {operating_system.times_installed} times so far!")
operating_system.boot_system()
operating_system.run_processes("apache", "php")
