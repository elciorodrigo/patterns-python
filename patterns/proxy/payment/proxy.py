from payment import Payment, Bank

class DebitCard(Payment):
    
    def __init__(self):
        self.bank = Bank()

    def do_pay(self):
        card = input("Proxy:: Punch in Card Number:")
        self.bank.setCard(card)
        return self.bank.do_pay()
