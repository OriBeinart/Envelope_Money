import random #in order to cast a random sum of money for each envelope
class Envelope():
    def __init__(self, money):
        self.money =money #integer defining the sum of money the envelope contains
        self.used = False #boolian variable which states if the envelope was opened or not
    """Defines the values of Envelopes's properties.
        """


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



class N_max_strategy(BaseStrategy):
    def __init__(self, envelope_arr, N):
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



e1 = Envelope(1)
e2 = Envelope(23)
e3 = Envelope(88)
e4 = Envelope(60)
e5 = Envelope(14)
e6 = Envelope(67)
e7 = Envelope(9)
e8 = Envelope(62)
e9 = Envelope(11)
e10 = Envelope(10)


envelopes = [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10]

x = N_max_strategy(envelopes,3)
print(x.play().money)
