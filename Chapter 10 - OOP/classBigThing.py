class BigThing:
    def __init__(self, thing):
        self.thing = thing

    def size(self):
        if isinstance(self.thing, int) or isinstance(self.thing, float):
            return self.thing
        else:
            return len(self.thing)
