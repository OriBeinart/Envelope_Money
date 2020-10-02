class Base_Strategy ():
    def __init__(self, envelope_arr):
        self.envelopes = envelope_arr
        self.count = 0
        self.chosen_envelope = None
        self.continue_strategy = True

    def play(self):
        while ((self.continue_strategy)and(self.count<100)):
            self.perform_strategy(self.envelopes[self.count])
        if (self.chosen_envelope == None):
            self.chosen_envelope = self.envelopes[self.count]
        return self.chosen_envelope

    def perform_strategy(self, envelope):
        print ('the sum in this envelope is {envelope.money}')
        envelope.used = True
        choice = input(f'if you would like to keep it press u (use) if not press c (continue)')
        if (choice == 'c'):
            self.count = self.count + 1
        else:
            self.continue_strategy = False
            self.chosen_envelope = envelope


