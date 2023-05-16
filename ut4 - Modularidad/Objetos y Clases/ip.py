class IP:
    MAX_LIMIT_CIDR = 32
    MIN_LIMIT_CIDR = 8
    OCTET = "1" * 8 + "."
    ALL_NETWORK = (OCTET * 4).strip(".")
    ALL_HOSTS = ALL_NETWORK.replace("1", 0)
    OCTET_LEN = 8

    def __init__(self, ip: str, cidr: int) -> None:
        if ip:
            self.ip = ip
            self.cidr = cidr

    @property
    def cidr_index(self):
        period_amount = self.cidr // IP.OCTET_LEN
        # Cantidad de puntos '.' que hay en la parte de la red
        return self.cidr + period_amount

    @property
    def ip(self) -> list:
        return self.__ip

    @ip.setter
    def ip(self, ip):
        self.__ip = ip

    @property
    def binary(self):
        if self.__binary_ip is None:
            print("Calculando binario...")
            self.__binary_ip = ".".join(
                f"{int(octet):08b}" for octet in self.ip.split(".")
            )
        return self.__binary_ip

    @property
    def binary_mask(self) -> str:
        return IP.ALL_NETWORK[: self.cidr_index] + IP.ALL_HOSTS[self.cidr_index :]

    @property
    def network_id(self) -> str:
        return IP.binary_ip[: self.cidr_index] + IP.ALL_NETWORK[self.cidr_index :]

    @property
    def ip_broadcast(self) -> str:
        return self.binary_ip[: self.cidr_index] + IP.ALL_NETWORK[self.cidr_index :]

    @staticmethod
    def binary_ip_2_dec(ip: str) -> str:
        return ".".join(str(int(octet, 2)) for octet in ip.split("."))

    @property
    def cidr_fixed_index(self):
        """Propiedad para calcular el índice real del cidr sobre las ip en modo str y binario,
        al tener en cuenta los puntos entre cada octetoy sumarlo al cidr, arreglamos el indice
        """
        period_amount = self.cidr // IP.OCTET_LEN
        return self.cidr + period_amount
