# create your zoop here

class Animal():

    def __init__(self, name, species, age, gender):
        self.name = name
        self.species = species
        self.age = age
        self.gender = gender

    def describe(self):
        print(f"{self.name} is a {self.species} that is age {self.age} & {self.gender}")

    def feed(self):
        print(f"{self.name} is eating")

    def make_sound(self):
        print(f"{self.name} is making a classic {self.species} sound.")
    
    def move(self):
        print(f"{self.name} is on the move")

muf = Animal("Mufasa", "Lion", 10, "Male")

# muf.describe()
# muf.feed()
# muf.make_sound()
# muf.move()

class Mammal(Animal):
    def __init__(taco, name, species, age, gender, fur_color):
        super().__init__(name, species, age, gender)
        taco.fur_color = fur_color

    def describe(taco):
        super().describe()
        print(f"{taco.name} has {taco.fur_color} colored fur.")

    def feed(taco):
        super().feed()
        print(f"{taco.name} drinks milk when feeding.")

    def move(taco):
        super().move()
        print(f"{taco.name} walks when moving.")

    def make_sound(taco):
        super().make_sound()
        print(f"{taco.name} growls when making sound.")

leo = Mammal("Leo", "Lion", 5, "Male", "Golden")
# leo.describe()
# leo.feed()
# leo.make_sound()
# leo.move()

class Zoo:
    
    def __init__(self, animals):
        self.animals = animals

    def add_animal(self, animal):
        self.animals.append(animal)

    def display_animals(self):
        for animal in self.animals:
            animal.describe()

    def feed_animals(self):
        for animal in self.animals:
            animal.feed()

    def listen_to_animals(self):
        for animal in self.animals:
            animal.make_sound()

    def watch_animals(self):
        for animal in self.animals:
            animal.move()

ahab = Mammal("Ahab", "Quokka", 27, "Male", "brown")
tony = Mammal("Tony", "Tiger", 35, "Male", "Striped")

animal_list = [ahab, tony]
    
zu = Zoo(animal_list)

gaz = Mammal("Gaz", "Gazelle", 4, "Male", "brownish orange")

zu.add_animal(gaz)

zu.display_animals()

