from dice import D6

class Hand(list):
    def __init__(self, size=0, die_class=None, *args, **kwargs):
        if not die_class:
            raise ValueError('You must provide a die class.')
        super().__init__()

# die_class is an argument that will hold the class that all of the dice will be.
# We can pass around classes just like we do variables or functions, in this way future
# developers can give our constructor a class for the dice that they want to roll

        for _ in range(size):
            self.append(die_class())
            # this should create how many dice we need
        self.sort()


    def _by_value(self, value):
        dice = []
        for die in self:
            if die == value:
                dice.append(die)
        return dice
# this is a method that will allow us to get all of the dice of a certain value
# single underscore at the beginning of _by_value():
# this is a thing you probably shouldn't use if you're just playing with a hand instance,
# this is the thing you would use in subclasses of hand or inside of hand itself

# in console: import dice, hands
# hand = hands.Hand(size=5, die_class=dice.D6) -- this is not calling the class it's simply passing the class

# Breakdown of the code from the top:
# We're using the class that's being passed in, in this case D6, and then we're instantiating some number of that class.
# Here in that loop, we're creating five D6 instances, that's a really cool way to handle this pluggable class requirement.


class RollHand(Hand):
    def __init__(self, *args, **kwargs):
        super().__init__(size=5, die_class=D6, *args, *kwargs)

    # all of these properties are a convinient way of getting all of the dice of a certain value
    # this is useful because it will allow you to score multiple dice of the same value

    @property
    def ones(self):
        return self._by_value(1)

    @property
    def twos(self):
        return self._by_value(2)

    @property
    def threes(self):
        return self._by_value(3)

    @property
    def fours(self):
        return self._by_value(4)

    @property
    def fives(self):
        return self._by_value(5)

    @property
    def sixes(self):
        return self._by_value(6)


    # making another property that returns a 'dict' where the keys are the die values and the values are how many of that die exist in the hand
    @property
    def _sets(self):
        return {
            1: len(self.ones)
            2: len(self.twos)
            3: len(self.threes)
            4: len(self.fours)
            5: len(self.fives)
            6: len(self.sixes)
        }
