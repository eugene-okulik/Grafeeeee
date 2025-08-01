def finished(func):

    def wrapper(*args):
        result = func(*args)
        print("finished")
        return result

    return wrapper


@finished
def example(text):
    print(text)


example('example')
