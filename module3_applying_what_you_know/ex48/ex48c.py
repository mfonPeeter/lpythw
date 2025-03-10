# Alter before or after

class Parent(object):

    def altered(self):
        print("PARENT altered()")
    
class Child(Parent):

    def altered(self):
        print("CHILD, BEFORE PARENT ALTERED()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.altered()
son.altered()