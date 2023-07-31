class InfiniteList:
    def __init__(self, *items, fill_value=None):
        self.infinite_list = list(items)
        self.fill_value = fill_value

    def __setitem__(self, index: int, item: int) -> None:
        for _ in range(len(self.infinite_list), index + 1):
            self.infinite_list.append(self.fill_value)
        self.infinite_list.append(item)

    def __getitem__(self, index: int):
        return self.infinite_list[index]

    def __str__(self):
        return f"{self.infinite_list}"


super_list = InfiniteList(1, 2, 3, fill_value="*")
super_list[20] = "FIN🤓"
print(super_list)
