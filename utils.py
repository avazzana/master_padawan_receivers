import time
from functools import wraps

class TimeoutException(Exception):
    pass

def wait_until_true(wait=0.1, max_wait=10):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            while True:
                print("waiting for", func.__name__)
                if time.time() - start_time > max_wait:
                    raise TimeoutException(f"Function '{func.__name__}' exceeded maximum wait time of {max_wait} seconds")
                
                result = func(*args, **kwargs)
                if result:
                    print("Completed!", func.__name__)
                    return result
                time.sleep(wait)
        return wrapper
    return decorator
