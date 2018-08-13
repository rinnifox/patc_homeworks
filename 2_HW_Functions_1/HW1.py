import inspect


def partial(func, *fixated_args, **fixated_kwargs):

    def wrapper(*args, **kwargs):
        nonlocal fixated_args
        fixated_args = fixated_args + args
        fixated_kwargs.update(kwargs)
        return func(*fixated_args, **fixated_kwargs)

    arg_names = inspect.getcallargs(func, *fixated_args, **fixated_kwargs)

    wrapper.__name__ = 'partial_{}'.format(func.__name__)
    wrapper.__doc__ = """ 
    A partial implementation of {} with pre-applied arguements being: {}
    """.format(func.__name__, arg_names)

    return wrapper


# TESTS

def avg(*args):
    return sum(args)/2


_avg = partial(avg, 2, 3)
print(_avg.__name__)
print(_avg.__doc__)
print(_avg())

_avg = partial(avg, 2)
print(_avg.__name__)
print(_avg.__doc__)
print(_avg())

_avg = partial(avg, 2, 3, 5)
print(_avg.__name__)
print(_avg.__doc__)
print(_avg())

_avg = partial(avg, 2, 3, 5)
print(_avg.__name__)
print(_avg.__doc__)
print(_avg(3, 4))