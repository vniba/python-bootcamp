def adding_emoji(fn: object) -> object:
    """
    Adds an emoji to the end of a function name.
    """

    def printing():
        print("come on")

    def wrapper():
        printing()
        fn()

    return wrapper


@adding_emoji
def danger():
    print("💀")


danger()
import time


def speed_calc_decorator(fn):
    def wrapper():
        start_time = time.time()
        fn()
        end_time = time.time()
        print(f"{fn.__name__} run speed: {end_time - start_time}s")

    return wrapper


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


fast_function()


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


slow_function()
