class Animal:
    def falar(self):
        print("Este animal faz um som.")

class Cachorro(Animal):
    def falar(self):
        print("O cachorro fala.")

class Gato(Animal):
    def falar(self):
        print("O gato mia.")

c = Cachorro()
g = Gato()

c.falar()
g.falar()
