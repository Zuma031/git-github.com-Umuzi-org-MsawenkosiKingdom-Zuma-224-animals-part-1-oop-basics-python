class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
    
        return f"{self.name} eats"

    def sound(self):
        return "sound..."


class Dog(Animal):
    def __init__(self, name = "Rax"):
        self.name = name

    def sound(self):
        return "Bark"


class Cat(Animal):
    def __init__(self, name = "Stormy"):
        self.name = name

    def sound(self):
        return "Meow"


class Home:
    def __init__(self):
        self.animal = []

    def adopt_pet(self, animal):
        if animal in self.animal:
            raise Exception("Cannot adopt the same pet twice!")
        else:
            self.animal.append(animal)
        return len(self.animal)

    def make_all_sounds(self):
        sound_list = []
        sound = ""
        for animal in self.animal:
            sound_list.append(animal.sound())
        for animal in sound_list:
            sound = "\n".join(str(animal) for animal in sound_list)
        return sound


if __name__ == "__main__":

    dog1 = Dog()
    dog2 = Dog("Simba")

    dog1.eat()
    dog1.sound()

    dog2.eat()
    dog2.sound()

    cat1 = Cat()
    cat2 = Cat("Smokey")

    cat2.eat()
    cat2.sound()

    home = Home()
    dog1 = Dog()
    dog2 = Dog()
    cat1 = Cat()

    home.make_all_sounds()
    print(home.adopt_pet(dog1))

    home.make_all_sounds()
    print(home.adopt_pet(cat1))

    home.make_all_sounds()
    home.adopt_pet(dog2)

    print(home.make_all_sounds())
