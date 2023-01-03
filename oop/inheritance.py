class A: #base class
    def a1(self): #meber-function
        print("a1")

class Aa: #base class
    def aa1(self): #meber-function
        print("a1")

class B(A): #inheritence
    def b(self):
        print("b")

class C(B, Aa): #multiple-inheritance
    def b(self):
        print("b")

b = B()
b.a1()
b.aa1()

c = C()
c.b()
c.a1()
c.aa1
