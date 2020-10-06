class BaseStrategy ():
    def __init__(self, envelope_arr):
        self.envelopes = envelope_arr #array of envelopes on which the strategy is performed
        self.count = 0 #integer stating the number of envelopes opened and used to access the next envelope tha array
        self.chosen_envelope = None #Variable from type Envelope that contains the envelope that has been chosen as part of the strategy
        self.continue_strategy = True #boolian variable which informs if the strategy should be continued
    """Defines the values of BaseStrategy's properties.
        :param envelope_arr: self.envelopes value
        :type envelope_arr: Envelope[]
        """

    def play(self):
        while ((self.continue_strategy)and(self.count<len(self.envelopes))):
            self.perform_strategy(self.envelopes[self.count])
        if (self.chosen_envelope == None):
            self.chosen_envelope = self.envelopes[self.count-1]
        return self.chosen_envelope
    """Activates perform_strategy() for each envelope in the array until one is chosen.
        :return: The chosen envelope (self.chosen_envelope)
        :rtype: Envelope
        """

    def perform_strategy(self, envelope):
        print ('the sum in this envelope is {envelope.money}')
        envelope.used = True
        choice = input(f'if you would like to keep it press u (use) if not press c (continue)')
        if (choice == 'c'):
            self.count = self.count + 1
        else:
            self.continue_strategy = False
            self.chosen_envelope = envelope
    """Presents the user with the amount of money in the envelope and lets him choose if he wants to keep it or continue.
        :param envelope: envelope value
        :type envelope: Envelope
        """

    def display(self):
        print("Base strategy - you open the envelopes one after the other and stop whenever you feel like it")
    """Prints out an explaination about the method"""

class Automatic_BaseStrategy(BaseStrategy):
    def __init__(self, enevelope_arr):
        super().__init__(envelope_arr) #inherits the __init__ function from the BaseStrategy
        
    def perform_strategy(self, envelope):
        envelope.used = True #states that the envelope was opened
        chosen_enevelope = self.enevelopes[random.radiant(100)] #chooses a random envelope from the array
        self.continue_strategy = False #informs that the strategy shouldn't be continued

    def display(self):
        print("automatic strategy- chooses a random envelope")
    """Prints out an explaination about the method"""

class N_max_strategy(BaseStrategy):
    def __init__(self, envelope_arr, N = 3):
        super().__init__(envelope_arr)
        self.N = N #int Variable, the number of max the user choose
        self.lastMax = 0 #int Variable, saves the last max that was opened
        self.countMax = 0 #int Variable, counts the maxs envelopes

    
    def perform_strategy(self, envelope):
        envelope.used = True
        
        if (self.lastMax < envelope.money):
            self.lastMax = envelope.money
            self.countMax += 1
            if(self.countMax == self.N):
                self.continue_strategy = False
                self.chosen_envelope = envelope
        self.count += 1

    def display(self):
        print("N max strategy- gets num of max N as an argument and choose the N max envelope")
    """Prints out an explaination about the method"""
