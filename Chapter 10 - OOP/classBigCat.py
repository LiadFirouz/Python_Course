from classBigThing import BigThing


class BigCat(BigThing):
    def __init__(self, thing, weight):
        super(BigCat, self).__init__(thing)
        self.weight = weight

    def size(self):
        if 15 < self.weight < 20:
            return 'Fat'
        elif self.weight > 20:
            return 'Very Fat'
        else:
            return 'ok'
