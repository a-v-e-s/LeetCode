import time
import threading
import _thread
import sys


def count_executions_of(return_executions=False):
    """ counts executions of decorated function """

    executions = 0

    def inner(function):

        def wrapper(*args, **kwargs):
    
            nonlocal executions
            ret = function(*args, **kwargs)
            executions += 1
            print(f'{function.__name__} executed {executions} times!')
            
            if return_executions:
                return ret, executions
            else:
                return ret
    
        return wrapper
    
    return inner


def exit_after(s):
    """ decorator function to exit decorated function after s seconds: """
    
    def quit_function(f_name):
        """ kill main thread, informing user that it timed out. """
        print(f'{f_name} took too long.', file=sys.stderr)
        sys.stderr.flush()
        _thread.interrupt_main()
    
    def outer(fn):
    
        def inner(*args, **kwargs):
            timer = threading.Timer(s, quit_function, args=[fn.__name__])
            timer.start()
            try:
                result = fn(*args, **kwargs)
            finally:
                timer.cancel()
    
            return result
    
        return inner
    
    return outer


def timer(return_time=False):
    """ times a function """

    def inner(function):

        def wrapped_f(*args, **kwargs):

            start = time.perf_counter()
            result = function(*args, **kwargs)
            elapsed = time.perf_counter() - start
            print('Time Elapsed:\t'+str(elapsed)+' seconds')

            if return_time:
                return result, elapsed
            else:
                return result
        
        return wrapped_f
    
    return inner


class recursive_timer:
    """ singleton-like class-based timer decorator for recursive functions """

    def __init__(self, f):
        self.f = f
        self.active = False
        self.return_time = False
    
    def __call__(self, *args, **kwargs):
        
        if self.active:
            return self.f(*args, **kwargs)
        
        try:
            self.active = True
            start = time.perf_counter()
            val = self.f(*args, **kwargs)
            elapsed = time.perf_counter() - start
            print(f'Elapsed time:\t{elapsed} seconds')
            if self.return_time:
                return val, elapsed
            else:
                return val
        
        finally:
            self.active = False