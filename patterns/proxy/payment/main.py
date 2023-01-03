from proxy import DebitCard

class You:
    def __init__(self):
        print("You:: Lets buy the shirt")
        self.debitCard = DebitCard()
        self.isPurcharsed = None

    def make_payment(self):
        self.isPurcharsed = self.debitCard.do_pay()

    def __del__(self):
        if self.isPurcharsed:
            print("You:: Wow! Shirt is Mine!")
        else:
            print("You:: I should eran more")
        

you = You()
you.make_payment()