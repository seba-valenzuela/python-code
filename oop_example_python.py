
class Dog:
    # this is called "overriding the constructor" which is __init__
    # self is always the 1st argument because it points to the specific object created with class Dog
    def __init__(self, name):
        # This is assigning attirbute "name" to this specific object
        self.name = name

    def bark(self):
        print("woof!")
    
    def dog_add(self, x):
        print(str(x + 1))

# Instantiating an OBJECT of type DOG
d = Dog("Pablo")

d.bark()
d.dog_add(3)
# Printing the attribute "name" of the object "d"
print(d.name)