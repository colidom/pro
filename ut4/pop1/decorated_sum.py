# ****************************
# DECORANDO LA SUMA DE VALORES
# ****************************


def result_as_status(func):
    def wrapper(*args, **kwargs):
        status, result = func(*args, **kwargs)
        return dict(status=status, result=result)

    return wrapper


@result_as_status
def run(values: list) -> dict:
    result = 0
    for value in values:
        if not isinstance(value, int):
            return False, "Not int value found"
        result += value
    return True, result
