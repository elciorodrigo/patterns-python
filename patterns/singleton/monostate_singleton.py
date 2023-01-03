class Borg:
    __shared_state = {'1': '2'}
    
    def __init__(self):
        self.x = 1
        print(type(self.__shared_state))
        self.__dict__ = self.__shared_state

b = Borg()
b1 = Borg()
b.x = 4
print("borg object 'b':", b) ## b e b1 são objetos distintos
print("borg object 'b1':", b1)
print("Object state 'b':", b.__dict__) ##b e b1 compartilham o mesmo estado
print("Object state 'b':", b1.__dict__)