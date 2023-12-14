def decorator(func):

    def wrapper(name):
        result = func(name)
        return result.upper()

    return wrapper


@decorator
def get_my_name(name):
    return name


result = get_my_name('Nicholas')
print(result)
