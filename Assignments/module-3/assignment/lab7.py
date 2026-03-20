# Single, Multilevel, Multiple, Hierarchical, and Hybrid inheritance in Python. 

# Example 1: Single Inheritance
print("\n>>> Single Inheritance Example <<<")
class BaseParent:
    def greet_parent(self):
        print("Hello from the Parent class!")
class SingleChild(BaseParent):
    def greet_child(self):
        print("Hello from the Child class!")
obj1 = SingleChild()
obj1.greet_parent()
obj1.greet_child()


# Example 2: Multilevel Inheritance

print("\n>>> Multilevel Inheritance Example <<<")
class GrandParent:
    def greet_grandparent(self):
        print("Greetings from Grandparent!")
class ParentLevel(GrandParent):
    def greet_parent(self):
        print("Greetings from Parent!")
class ChildLevel(ParentLevel):
    def greet_child(self):
        print("Greetings from Child!")
obj2 = ChildLevel()
obj2.greet_grandparent()
obj2.greet_parent()
obj2.greet_child()


# Example 3: Multiple Inheritance
print("\n>>> Multiple Inheritance Example <<<")
class ParentA:
    def method_a(self):
        print("Method from ParentA")
class ParentB:
    def method_b(self):
        print("Method from ParentB")
class MultiChild(ParentA, ParentB):
    def method_child(self):
        print("Method from Child inheriting A & B")

obj3 = MultiChild()
obj3.method_a()
obj3.method_b()
obj3.method_child()

# Example 4: Hierarchical Inheritance
print("\n>>> Hierarchical Inheritance Example <<<")
class CommonParent:
    def parent_message(self):
        print("Message from Parent class")
class ChildOne(CommonParent):
    def child1_message(self):
        print("Message from Child One")
class ChildTwo(CommonParent):
    def child2_message(self):
        print("Message from Child Two")

c1 = ChildOne()
c2 = ChildTwo()
c1.parent_message()
c1.child1_message()
c2.parent_message()
c2.child2_message()

# Example 5: Hybrid Inheritance
print("\n>>> Hybrid Inheritance Example <<<")
class Root:
    def root_msg(self):
        print("Root class message")
class Branch1(Root):
    def branch1_msg(self):
        print("Branch1 class message")
class Branch2(Root):
    def branch2_msg(self):
        print("Branch2 class message")
class Leaf(Branch1, Branch2):
    def leaf_msg(self):
        print("Leaf class message")

leaf_obj = Leaf()
leaf_obj.root_msg()
leaf_obj.branch1_msg()
leaf_obj.branch2_msg()
leaf_obj.leaf_msg()


# Example 6: Using super() function
print("\n>>> Using super() Example <<<")

class ParentSuper:
    def show_message(self):
        print("ParentSuper class method called")

class ChildSuper(ParentSuper):
    def show_message(self):
        super().show_message()  
        print("ChildSuper class method called")

super_obj = ChildSuper()
super_obj.show_message()