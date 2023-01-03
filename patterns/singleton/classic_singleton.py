class Singleton(object):
    def __new__(cls): #overload method to instanciate objects
        if not hasattr(cls, 'instance'): # method to verify if object has some attribute, if object has "instace"
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

s = Singleton()
print("Object created", s)

s1 = Singleton()
print("Object created", s1)