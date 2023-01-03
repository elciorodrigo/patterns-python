#Oo
class Person(object):
    
    def __init__(self, name, age): # construtor
        self.name = name
        self.age = age
    
    def get_person(self,): # member-function
        return "<Person (%s, %s)>" % (self.name, self.age)

p = Person("John", 32) # p é um objecto do tipo Person
#print("Type of Object:", type(p), "Memory Address:", id(p))

#polimorfismo
a = "John" # string
b = (1, 2, 3) # tupla
c = [3, 4, 5, 6] # lista

print(a[1], b[2], c[3])


         