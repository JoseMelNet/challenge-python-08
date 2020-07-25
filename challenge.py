import time


def finish_date(function):
    def wrapper(*args, **kwargs):
        import time
        captured_time = time.gmtime()
        print_time = time.strftime("Execution time: %d/%m/%Y - %H:%M:%S", captured_time)
        function(*args, **kwargs)
        print(print_time)
        return function(*args, **kwargs)
    return wrapper


@finish_date
def palindrome(string):
    string = string.replace(' ', '').lower()
    return string == string[::-1]


@finish_date
def long_function():
    for _ in range(1000000):
        pass


def run():
    palindrome('Ana')
    long_function()


if __name__ == '__main__':
    run()
