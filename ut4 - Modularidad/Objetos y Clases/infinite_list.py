class InfiniteList:
    def __init__(self, *items, fill_value=None):
        self.items = list(items)
        self.fill_value = fill_value

    def __setitem__(self, index: int, item: int) -> None:
        for _ in range(len(self.items), index + 1):
            self.items.append(self.fill_value)
        self.items.append(item)

    def __getitem__(self, index: int):
        return self.items[index]

    def __str__(self):
        return f"{self.items}"


super_list = InfiniteList(1, 2, 3, fill_value="*")
super_list[20] = "FIN🤓"
print(super_list)
