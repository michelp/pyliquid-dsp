

class lazy_property(object):
    """Decorator, a @property that is only evaluated once per instance."""

    def __init__(self, fn):
        self.fn = fn
        self.__name__ = fn.func_name
        self.__doc__ = fn.__doc__

    def __get__(self, obj, cls):
        if obj is None:
            return None
        obj.__dict__[self.__name__] = result = self.fn(obj)
        return result
