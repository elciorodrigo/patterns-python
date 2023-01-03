from eventmanager import EventManager

class You(object):
    def __init__(self):
        print("You:: Whoa! Marriage Arrangements??!!")

    def askEventManager(self):
        print("You:: Let's Contact the Event Manager\n\n")
        em = EventManager()
        em.arrange()
    
    def __del__(self):
        print("You:: Thanks to Event Manager, all preparations done! Prew!")


you = You()
you.askEventManager()