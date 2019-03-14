import random

class Die:
    def __init__(self, sides=2, value=0):
        if not sides >= 2:
            raise ValueError('Your dice must have more than two sides')
        if not isinstance(sides, int):
            raise ValueError('Your dice sides needs to be a whole number')
        self.value = value or random.randint(1, sides)

    # always return an integer    
    def __int__(self):
        return self.value

    # Defining 6 magic methods: if playing a lot of dice games it is needed to have the sum total of the dice.
    #  Be able to compare dice to each other, or to another number too,
    # find all the dice that have a value over for example four

    # 1. Equal
    def __eq__(self, other):
        return int(self) == other

    # 2. Not equal
    def __ne__(self, other):
        return int(self) != other
        # return not int(self) == other

    # 3. Grater than
    def __gt__(self, other):
        return int(self) > other

    # 4. Less than
    def __lt__(self, other):
        return int(self) < other

    # 5. Grater then and equal to
    def __ge__(self, other):
        return int(self) > other or int(self) == other

    # 6. Less than and equal to
    def __le__(self, other):
        return int(self) < other or int(self) == other

    # Add
    def __add__(self, other):
        return int(self) + other

    # Reverse add
    def __radd__(self, other):
        return int(self) + other

    def __repr__(self):
        return str(self.value)


class D6(Die):
    def __init__(self, value=0):
        super().__init__(sides=6, value=value)
