import random  # in order to cast a random sum of money for each envelope


class Envelope:
    def __init__(self):
        self.money = random.randint(0, 100000)  # integer defining the sum of money the envelope contains
        self.used = False  # boolean variable which states if the envelope was opened or not

    """Defines the values of Envelopes's properties.
    """

        
