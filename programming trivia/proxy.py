class Xxx:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        if self.validate(*args, **kwargs):
            self.func(*args, **kwargs)
        else:
            raise Exception("Invalid params")

    def validate(self, *args, **kwargs):
        pass

