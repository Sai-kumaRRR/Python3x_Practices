# Overriding - same name in the parent and child .
# child always  override the parent functions.

# super means call my parent function

class Animal:
    def __init__(self):
        pass

    def sound(self):
        print("Animal sound")

class Dog(Animal):

    def __init__(self):
        pass

    def sound(self):
        super().sound()
        print("Dog Sound")

        # animal = Animal()
        # animal.sound()

