from functools import wraps
from collections.abc import Callable
from time import time


def timer_dec(func: Callable):
    @wraps(func)
    def my_wrapper(*args, **kwargs):
        start_time = time()
        res = func(*args, **kwargs)
        end_time = time()
        time_of_ex = end_time - start_time
        print(f'Время выполнения: {time_of_ex}')
        return res
    return my_wrapper


@timer_dec
def my_func(rng):
    a = [x for x in range(rng)]
    return a


print(my_func(1000))
