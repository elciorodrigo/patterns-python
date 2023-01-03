class Singleton:
    __instance = None
    def __init__(self):
        if not Singleton.__instance:
            print("__init__ method called..")
        else:
            print("Instance already created:", self.getInstance())

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance
     
s = Singleton() # inicialized class, but object not created
print('inicialized class, but object not created:', s)

print(Singleton.getInstance()) # object created here
print(Singleton.getInstance())
print(Singleton())
print(Singleton())
print(Singleton.getInstance())

#singleton() usa o mesmo objeto em local de memoria diferente
#getIntance() retorna o objeto no mesmo local de memória                                                                                                                                                          
        