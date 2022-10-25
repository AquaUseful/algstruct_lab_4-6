import time


def measure_time(func,
                 args: tuple,
                 kwargs: dict,
                 repeats: int,
                 divider: int):
    start = time.time()
    result = func(*args, **kwargs)
    for _ in range((repeats // divider) - 1):
        func(*args, **kwargs)
    exec_time = time.time() - start
    return (result, exec_time * divider)
