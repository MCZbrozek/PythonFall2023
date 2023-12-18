class FooBar:
    def __init__(self, value=42): #Default value
        self.somevar = value

some_default_object = FooBar()
some_object = FooBar(400)
some_other_object = FooBar(500)

print(some_default_object.somevar)
print(some_object.somevar)
print(some_other_object.somevar)