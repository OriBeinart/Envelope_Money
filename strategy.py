import random


class BaseStrategy:
    def __init__(self, envelope_arr):
        self.envelopes = envelope_arr  # array of envelopes on which the strategy is performed
        self.count = 0  # integer stating the number of envelopes opened and used to access the next envelope tha array
        self.chosen_envelope = None  # Variable from type Envelope that contains the envelope that has been chosen as
        # part of the strategy
        self.continue_strategy = True  # boolean variable which informs if the strategy should be continued

    """Defines the values of BaseStrategy's properties.
        :param envelope_arr: self.envelopes value
        :type envelope_arr: Envelope[]
        """

    def play(self):
        while self.continue_strategy and (self.count < len(self.envelopes)):
            self.perform_strategy(self.envelopes[self.count])
        if self.chosen_envelope is None:
            self.chosen_envelope = self.envelopes[self.count - 1]
            print('No suitable envelope found. The last envelope is the one selected:')
        print(
            f'Sum of Money: {self.chosen_envelope.money} Index in array: {self.envelopes.index(self.chosen_envelope)}')
        return self.chosen_envelope

    """Activates perform_strategy() for each envelope in the array until one is chosen.
        :return: The chosen envelope (self.chosen_envelope)
        :rtype: Envelope
        """

    def perform_strategy(self, envelope):
        print('the sum in this envelope is ' + str(envelope.money))
        envelope.used = True  # states that the envelope was opened
        choice = input(f'if you would like to keep it press u (use) if not press c (continue)')
        if choice == 'c':
            self.count = self.count + 1
        else:
            self.continue_strategy = False  # informs that the strategy shouldn't be continued
            self.chosen_envelope = envelope

        """ Presents the user with the amount of money in the envelope and lets him choose if he wants to keep it or continue.
            :param envelope: envelope value
            :type envelope: Envelope
            """

    def display(self):
        return "Base strategy - you open the envelopes one after the other and stop whenever you feel like it"

    """Short description of class strategy
    :return: string that describe the class purpose"""


class Automatic_BaseStrategy(BaseStrategy):
    # inherits the __init__ function from the BaseStrategy

    def perform_strategy(self, envelope):
        envelope.used = True  # states that the envelope was opened
        self.chosen_envelope = self.envelopes[random.randint(0, 100)]  # chooses a random envelope from the array
        self.continue_strategy = False  # informs that the strategy shouldn't be continued

        """ Automatic strategy- chooses a random envelope
            :param envelope: envelope value
            :type envelope: Envelope
            """

    def display(self):
        return "automatic strategy- chooses a random envelope"

    """Short description of class strategy
    :return: string that describe the class purpose"""


class More_then_N_percent_group_strategy(BaseStrategy):
    def __init__(self, envelope_arr, percent):
        super().__init__(envelope_arr)  # inherits the __init__ function from the BaseStrategy
        self.percent = percent  # float variable which represents how many percents of the envelopes we need to open
        # in order to find the one with max amount of money
        self.Maxmoney = 0  # the envelope contains the biggest amount of money

    """Defines the values of More_then_N_percent_group_strategy's properties.
        :param envelope_arr: self.envelopes value
        :param percent: self.percent value
        :type envelope_arr: Envelope[]
        :type percent: float
        """

    def perform_strategy(self, envelope):
        envelope.used = True  # states that the envelope was opened
        self.percent = float(self.percent)
        if self.count < self.percent * 100:
            if envelope.money > self.Maxmoney:
                self.Maxmoney = envelope.money
        elif envelope.money > self.Maxmoney:
            self.chosen_envelope = envelope
            self.continue_strategy = False  # informs that the strategy shouldn't be continued
        self.count += 1

    """
    Opening X% of the envelopes and searching for the envelope
    with maximum money. Then in the remaining envelopes look for the first envelope with a sum of money"
    higher than the maximum and set it as self.chosen_envelope
    :param envelope: envelope value
    :type envelope: Envelope
    """

    def display(self):
        return ("More_then_N_percent_group_strategy- Opening X% of the envelopes and searching for the envelope"
                " with maximum money. Then in the remaining envelopes look for the first envelope with a sum of money"
                " higher than the maximum")

    """Short description of class strategy
    :return: string that describe the class purpose"""


class N_max_strategy(BaseStrategy):
    def __init__(self, envelope_arr, N=3):
        super().__init__(envelope_arr)
        self.N = N  # int Variable, the number of max the user choose
        self.lastMax = 0  # int Variable, saves the last max that was opened
        self.countMax = 0  # int Variable, counts the maxs envelopes

    """Defines the values of More_then_N_percent_group_strategy's properties.
        :param envelope_arr: self.envelopes value
        :param N: self.N value (default 3)
        :type envelope_arr: Envelope[]
        :type N: int
        """

    def perform_strategy(self, envelope):
        envelope.used = True  # states that the envelope was opened

        if self.lastMax < envelope.money:
            self.lastMax = envelope.money
            self.countMax += 1
            if self.countMax == self.N:
                self.chosen_envelope = envelope
                self.continue_strategy = False  # informs that the strategy shouldn't be continued
        self.count += 1

    """
        Gets num of max N as an argument and choose the N max envelope - set it as self.chosen_envelope
        :param envelope: envelope value
        :type envelope: Envelope
        """

    def display(self):
        return "N max strategy- gets num of max N as an argument and choose the N max envelope"

    """Short description of class strategy
    :return: string that describe the class purpose"""

