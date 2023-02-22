def find_item(data: tuple, item: int) -> tuple:

    """Returns number of occurrences of item in he provided tuple.

    :param data: tuple of numbers
    :type data: tuple
    :param item: number to find in the tuple
    :type item: int

    :return: number of ocurrences of item
    :rtype: tuple
    """
    result = len([val for val in data if val == item])
    return result


data = (1, 2, 3, 1, 2, 3, 4, 1, 2)

print(find_item(data, 1))
