# f , m  -> 5 , 5 from both


class father:

    def father_money(self):
        return "5"

class mother:

        def mother_money(self):
            return "5"


class son(father,mother):
    pass


    son = son()
print(son.father_money())
print(son.mother_money())
