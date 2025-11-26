# Integer
number_five = 5
print("Variable:" + str(number_five) + " with class:" + str(type(number_five)))

# Float
one_dot_two = 1.2
print("Type: ", type(one_dot_two))

# String
text = "Some text"
print("'" + text + "'" + " has type: " + str(type(text)))

# Boolean
is_true = True
print("Value: " + str(is_true) + " has type: " + str(type(is_true)))

# List
days = ['Monday', "Wednesday", 'Friday']
print(days, " has type: ", str(type(days)))

# Tuple (immutable list that can contain duplicates)
immutable_list = (1, 2, 3)
print(immutable_list, " has type: ", str(type(immutable_list)))

# Dictionary
words_meaning = {"Hello": "A greeting", "Bye": "A farewell"}
print(words_meaning.get("Bye"))

# Set
unique_numbers = {1, 2, 3, 4, 5, 1}
print(unique_numbers, " has type: ", str(type(unique_numbers)))

# None
print(type(None))

# classes and objects
class Person:
    pass

instance_of_class = Person()
print("Class has type:" , type(instance_of_class))
