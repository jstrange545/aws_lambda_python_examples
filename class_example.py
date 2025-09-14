class Dog:
    # Class attribute (shared by all instances of the class)
    species = "Canis familiaris"

    # The __init__ method is the constructor, called when a new object is created
    def __init__(self, name, breed):
        # Instance attributes (unique to each object)
        self.name = name
        self.breed = breed
        self.is_hungry = True

    # Instance method (defines behavior of objects)
    def bark(self):
        return f"{self.name} says Woof!"

    # Another instance method
    def eat(self):
        if self.is_hungry:
            self.is_hungry = False
            return f"{self.name} is now full!"
        else:
            return f"{self.name} is not hungry right now."

# Create objects (instances) of the Dog class
my_dog = Dog("Buddy", "Golden Retriever")
your_dog = Dog("Lucy", "Labrador")

# Access class attributes
print(f"Buddy's species: {my_dog.species}")
print(f"Lucy's species: {your_dog.species}")
print(f"General dog species: {Dog.species}")

# Access instance attributes
print(f"My dog's name: {my_dog.name}")
print(f"Your dog's breed: {your_dog.breed}")

# Call instance methods
print(my_dog.bark())
print(your_dog.eat())
print(your_dog.eat()) # Calling again when not hungry