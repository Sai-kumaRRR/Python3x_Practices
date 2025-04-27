# Polymorphism
# ABC
# Exception


# polymorphism- object- oriented programming -> OOPs


# Object -> behave differently based on the string.

# person -> Amit , sonu -> speak() , Amit can talk in hindi and sonu can talk in english.


class shape:

    def area(self):
        print("Area of shape")


class retangle(shape):

    def __init__(self, length, width):
        self.width = width

        def area(self):
            return self.length * self.width


class circle(shape):

    def __init__(self, radius):
        self.radius = radius


def area(self):
    return 3.14 * self.radius * self.radius


shape1 = retangle(length3, width4)
print(shape1,area())
shape2 = circle(10)
print(shape2.area())

shape3 = shape()
print(shape3.area())



