class GF:

    def car(self):
        return "old car"

class f(GF):

        def car(self):
            return "honda civic"

class s(f):

            def car(self):
                return "Lambo"

            son = f()
            print(son.car())


