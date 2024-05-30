# Quiz Project and Object-Oriented Programming:
# Quiz Game (true/false) answering questions and keeping track of score completely in OOP.

# Creating Classes:
# Class is a Blueprint for creating an eventual object
# attributes are what an object has and methods are what it does.

#-----------------------------------------------------------------------------------------------------------------------------------------

# syntax is to type class keyword followed by the name:
# ex: building a website needing a class to model the website's users - what they HAVE and what they can DO
# remember PascalCase for class names
# use the keyword "pass" so that you can use an empty class when building the code to avoid indentation errors, same logic for ojects.

#step 1: writing the declaration.
class User:
    pass
#empty for now thanks to the "pass" keyword.

#-----------------------------------------------------------------------------------------------------------------------------------------

#step 2: building the object from the new class.
# creating the first object from User class:
# place parenthesis after class name when initializing an object
# snake_case for objects (camelCase isn't used often in Python for example)

user_1 = User()

#-----------------------------------------------------------------------------------------------------------------------------------------

#step 3: create an attribute for this class with syntax object_1.attribute_1 = "attribute" - remember attribute is a variable that is associated with an object
# tap into the object and create an attribute:

user_1.id = "001"
user_1.username = "chris"

print(user_1.username)

#-----------------------------------------------------------------------------------------------------------------------------------------

# now, with a ton of attributes and tons of users, assigning values manually for each user can make the code be prone to errors.
# here is where constructors come into play, these specify what should happen - also known as initializing an object:
# initializing an object = to set variables to their starting values at the beginning of a program or subprogram.
# using the __init__() function - rememebr the use double underscore on both sides of init

#Constructor:
class Car:
    def __init__(self):
        #initialize attributes 

# self is the actual object that is being created or initialized.
# add as many parameters as needed, separated by commas after self 
class Car:
    def __init__(self, seats):
        self.seats = seats 

# for example, creating a new car object called my_car and passing in data to ensure that this my_car has 5 seats.
my_car = Car(5)

# ex 2:
# it is conventional that the name of the parameter matches the name of the attribute, althought that is not required.
class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username

user_1 = User("001","chris")
user_2 = User("002","jose")

# so, whever a new user is created, they MUST have information (arguments) passed into all parameters in the __init__() function.

#-----------------------------------------------------------------------------------------------------------------------------------------

# think example of creating User class for instagram account, where the account starts out with zero followers as a default value.
# by setting followers attribute to zero, a value for this attribute does not need to be specified when creating a new user object.
 
class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0

#-----------------------------------------------------------------------------------------------------------------------------------------

# adding methods to a class (when a function is attached to an object it is called a method):
# ex for Car class. adding a method that will reduce the number of seats to be equal to 2, so the car is better suited for racing (less weight)
def enter_race_mode():
    seats = 2

# so, now creating a way for instagram follower counts to go up once self (object that the follow() fucntion is being called for) follow eachother:
# remember self in the follow function refers to the who is follow the username, which is the argument passed through the "user" parameter in the def statement to create this method:

class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
    
    def follow(self,user):
        user.followers += 1
        self.following += 1

# remember "self" is only used when writing code to create Classes, not when creating objects that call the Classes.

# now user_1 (chris), will follow user_2 (jose):
user_1.follow(user_2)

# these two print statements will show that user 1 has zero followers and is following 1 user:
print(user_1.followers)
print(user_1.following)

#these two print statements will show that user 1 has 1 follower and is following 0 users:
print(user_2.followers)
print(user_2.following)

