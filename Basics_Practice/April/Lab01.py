class my_class:

    def __init__(self):
        self.private_var = 10
        self.protected_var = 15
        self.public_var = 18

        def public_method(self):
            print("This is public method")
            obj = my_class()
            obj.public_var = 34
            print(obj.public_var)
            obj.public_method()

            # obj_protected_var = 90
            # print(obj_protected_var)


