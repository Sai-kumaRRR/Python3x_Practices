# public- variable-don't mention anything.
# protected
# private
# variable and function


class person:

    def __init__(self, name, age):
        self._name = name
        self._age = age

        def print_details(self):
            print("You details", self._name, self._age)


         #   person.print_details()

            # print(person_name) # Private ?
            # How to change it get and set ?
            # fetch - Get
            # set the value - constructor
            person.set_name("Amit")
            name = person.set_name()
            print(name)
