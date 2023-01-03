class Actor(object):
    def __init__(self):
        self.isBusy = True
    
    def occupied(self):
        self.isBusy = True
        print(type(self).__name__, "is occupied with current movie")

    def available(self):
        self.isBusy = False
        print(type(self).__name__, "is free for the movie")
    
    def getStatus(self):
        return self.isBusy


"""
    Agent is the proxy
"""
class Agente(object):
    def __init__(self):
        self.principal = None
    
    def work(self):
        self.actor = Actor()
        if self.actor.getStatus():
            self.actor.occupied()
        else:
            self.actor.available()

if __name__ == '__main__':
    r = Agente()
    r.work()
        