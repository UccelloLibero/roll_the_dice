import random

class Die:
    def __init__(self, sides=2, value=0):
        if not sides >= 2:
            raise ValueError('Your dice must have more than two sides')
        if not isinstance(sides, int):
            raise ValueError('Your dice sides needs to be a whole number')
        self.value = value or random.randint(1, sides)


class D6(Die):
    def __init__(self, value=0):
        super().__init__(sides=6, value=value)
