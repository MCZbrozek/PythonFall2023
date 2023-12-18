sentence = "With a moo-moo here and a moo-moo there"
inex_of_moo = sentence.find('moo')
print(f"The location of moo in the sentence is {inex_of_moo}")

sentence2 = "Monty Python's Flying Circus"
index_of_monty = sentence2.find('Monty')
print(f"Location of Monty is {index_of_monty}.")

index_of_python = sentence2.find('Python')
print(f"Location of Python is {index_of_python}")

index_of_nothing = sentence.find("Python")
print(f"Location of Python is {index_of_nothing}")

subject = '$$$ Get Rich now!!! $$$'
index_of_dollars = subject.find('$$$')
print(f"The index of the $$$ is: {index_of_dollars}")

index_of_second_dollars = subject.find('$$$',1)
print(f"The index of the $$$ is: {index_of_second_dollars}")