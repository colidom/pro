class InfiniteList:
    def __init__(self, fill_value=None):
        self.fill_value = fill_value
        self.infinite_list = []

    def __setitem__(self, index: int, item: int) -> None:
        for _ in range(len(self.infinite_list), index):
            self.infinite_list.append(self.fill_value)
        self.infinite_list.append(item)

    def __getitem__(self, index: int):
        return self.infinite_list[index]

    def __str__(self):
        return f"{self.infinite_list}"


super_list = InfiniteList()
super_list[20] = 20
print(super_list)
