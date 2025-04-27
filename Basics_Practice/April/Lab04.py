# Single Inheritance

#  use the properties , variables and methods of your base class or parent class by the sub class.

class father:
    bank_bal = 100

    def one_bhk(self):
        print("use it son")

        class son(father):
            pass  # I will write the code in future !!!

        s = son()
        s.one_bhk()
        print(s.bank_bal)




