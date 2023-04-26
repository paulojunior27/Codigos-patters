class Animal:
    def speak(self):
        pass
    
class Angola(Animal):
    def speak(self):
        return "Tô fraco, tô fraco!"
    
class Vaca(Animal):
    def speak(self):
        return "Muuuu!"

class AnimalFactory:
    def create_animal(self, animal_type):
        if animal_type == "angola":
            return Angola()
        elif animal_type == "vaca":
            return Vaca()
        else:
            return None

factory = AnimalFactory()

angola = factory.create_animal("angola")
print(angola.speak())

vaca = factory.create_animal("vaca")
print(vaca.speak())