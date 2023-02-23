def find_item(data: tuple, item: int) -> int:

    """Returns number of occurrences of item in he provided tuple.

    :param data: numeric data to look for in
    :type data: tuple

    :param item: value to be counted
    :type item: int

    :return: number of ocurrences of item in data
    :rtype: int
    """
    result = len([val for val in data if val == item])
    return result


data = (1, 2, 3, 1, 2, 3, 4, 1, 2)

print(find_item(data, 1))
