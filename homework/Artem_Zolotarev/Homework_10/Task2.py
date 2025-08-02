def repeat_me(count=1):
    def decorator(func):

        def wrapper(*args):
            for x in range(count):
                func(*args)
        return wrapper
    return decorator


@repeat_me(count=2)
def example(text):
    print(text)


example('print me')
