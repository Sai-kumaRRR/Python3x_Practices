# Hierarchical Inheritance

class vehicle:

    def info(self):
        return " This is a vehicle"

class car(vehicle):

        def info(self):
            return "this is car"

        class Bicycle(vehicle):

            def info(self):
                return "This is a bicycle"

            car = car()
