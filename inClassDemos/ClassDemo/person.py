class Person:
    # Set and get methods
    # Self is the object in the class Person
    # Name is the parameter passed to object 
    def set_name(self, name):
        self.name = name
    
    # the get method has get in the name, only a self (object) parameter and just returns self.attribute. 
    def get_name(self):
        return self.name
    
    # Methods to do stuff
    def greet(self):
        print(f"Hello, my name is {self.name}")

# The class doesn't do anything until you instantiate an object from the class. 
# The are 2 people "objects" from the person class
person1 = Person()
person2 = Person()
# by calling these person objects, we get access the getter and setter methods from the class "Person()"
person1.set_name("Luke Skywalker")
person1.greet()