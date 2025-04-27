# Multilevel Inheritance

class grandparent:

    def grandparent_method(self):
        return "grandfather_method"


class parent(grandparent):

    def parent_method(self):
        return "parent's method"


class child(parent):

    def child_method(self):
        return "parent's method"


child = child()
print(child.grandparent_method())
print(child.parent_method())
print(child.child_method())
