class Dog:
    name = ""
    coat_color = ""


Phu_Quoc = Dog()
Phu_Quoc.name = "Phu Quoc"
Phu_Quoc.coat_color = "yellow"
# print(Phu_Quoc.coat_color)
Husky = Dog()
Husky.name = "Husky"
Husky.coat_color = "white"


class Flower:
    color = 'unknown'


rose = Flower()
rose.color = "red"
violet = Flower()
violet.color = "violet"
this_pun_is_for_you = Flower()
# print("Roses are {},".format(rose.color))
# print("violets are {},".format(violet.color))
# print(this_pun_is_for_you)


class Birds:
    color = ""
    number = [2, 4, 5, 2, 1, 4, 2, 4]

    def count(self, target):
        return self.number.count(target)


birds = Birds()
# print(birds.count(2))


# “If you have an apple and I have an apple and we exchange these apples then
# you and I will still each have one apple. But if you have an idea and I have
# an idea and we exchange these ideas, then each of us will have two ideas.”
# George Bernard Shaw

class Person:
    apples = 0
    ideas = 0


johanna = Person()
johanna.apples = 1
johanna.ideas = 1

martin = Person()
martin.apples = 2
martin.ideas = 1


def exchange_apples(you, me):
    # Here, despite G.B. Shaw's quote, our characters have started with       #different amounts of apples so we can better observe the results.
    # We're going to have Martin and Johanna exchange ALL their apples with #one another.
    # Hint: how would you switch values of variables,
    # so that "you" and "me" will exchange ALL their apples with one another?
    # Do you need a temporary variable to store one of the values?
    # You may need more than one line of code to do that, which is OK.
    tmp = you.apples
    you.apples = me.apples
    me.apples = tmp

    return you.apples, me.apples


def exchange_ideas(you, me):
    # "you" and "me" will share our ideas with one another.
    # What operations need to be performed, so that each object receives
    # the shared number of ideas?
    # Hint: how would you assign the total number of ideas to
    # each idea attribute? Do you need a temporary variable to store
    # the sum of ideas, or can you find another way?
    # Use as many lines of code as you need here.
    total_of_ideas = you.ideas+me.ideas
    you.ideas = total_of_ideas
    me.ideas = total_of_ideas
    return you.ideas, me.ideas


# exchange_apples(johanna, martin)
# print("Johanna has {} apples and Martin has {} apples".format(
#     johanna.apples, martin.apples))
# exchange_ideas(johanna, martin)
# print("Johanna has {} ideas and Martin has {} ideas".format(
#     johanna.ideas, martin.ideas))
# define a basic city class


# The City class has the following attributes: name, country (where the city is located), elevation (measured in meters),
# and population (approximate, according to recent statistics). Fill in the blanks of the max_elevation_city function
# to return the name of the city and its country (separated by a comma), when comparing the 3 defined instances
# for a specified minimal population.
# For example, calling the function for a minimum population of 1 million: max_elevation_city(1000000) should return "Sofia, Bulgaria".
class City:
    # name = ""
    # country = ""
    # elevation = 0
    # population = 0
    def __init__(self):
        self.name = ""
        self.country = ""
        self.elevation = 0
        self.population = 0


    # create a new instance of the City class and
    # define each attribute
city1 = City()
city1.name = "Cusco"
city1.country = "Peru"
city1.elevation = 3399
city1.population = 358052

# create a new instance of the City class and
# define each attribute
city2 = City()
city2.name = "Sofia"
city2.country = "Bulgaria"
city2.elevation = 2290
city2.population = 1241675

# create a new instance of the City class and
# define each attribute
city3 = City()
city3.name = "Seoul"
city3.country = "South Korea"
city3.elevation = 38
city3.population = 9733509


def max_elevation_city(min_population):
    # Initialize the variable that will hold
    # the information of the city with
    # the highest elevation
    return_city = City()

    # Evaluate the 1st instance to meet the requirements:
    # does city #1 have at least min_population and
    # is its elevation the highest evaluated so far?
    if city1.population >= min_population and city1.elevation > return_city.elevation:
        return_city = city1
    # Evaluate the 2nd instance to meet the requirements:
    # does city #2 have at least min_population and
    # is its elevation the highest evaluated so far?

    if city2.population >= min_population and city2.elevation > return_city.elevation:
        return_city = city2
    # Evaluate the 3rd instance to meet the requirements:
    # does city #3 have at least min_population and
    # is its elevation the highest evaluated so far?
    if city3.population >= min_population and city3.elevation > return_city.elevation:
        return_city = city3
    # Format the return string
    if return_city.name:
        return "{}, {}".format(return_city.name, return_city.country)
    else:
        return ""


# print(max_elevation_city(100000))  # Should print "Cusco, Peru"
# print(max_elevation_city(1000000))  # Should print "Sofia, Bulgaria"
# print(max_elevation_city(10000000))  # Should print ""

class City:
    def __init__(self, name, country, elevation, population):
        self.name = name
        self.country = country
        self.elevation = elevation
        self.population = population


# create a new instance of the City class and
# define each attribute
city1 = City("Cusco", "Peru", 3399, 358052)
# create a new instance of the City class and
# define each attribute
city2 = City("Sofia", "Bulgaria", 2290, 1241675)
# create a new instance of the City class and
# define each attribute
city3 = City("Seoul", "South Korea", 38, 9733509)


def max_elevation_city(min_population):
    # Initialize the variable that will hold
    # the information of the city with
    # the highest elevation
    return_city = City("", "", 0, 0)

    # Evaluate the 1st instance to meet the requirements:
    # does city #1 have at least min_population and
    # is its elevation the highest evaluated so far?
    if city1.population >= min_population and city1.elevation > return_city.elevation:
        return_city = city1
    # Evaluate the 2nd instance to meet the requirements:
    # does city #2 have at least min_population and
    # is its elevation the highest evaluated so far?

    if city2.population >= min_population and city2.elevation > return_city.elevation:
        return_city = city2
    # Evaluate the 3rd instance to meet the requirements:
    # does city #3 have at least min_population and
    # is its elevation the highest evaluated so far?
    if city3.population >= min_population and city3.elevation > return_city.elevation:
        return_city = city3
    # Format the return string
    if return_city.name:
        return "{}, {}".format(return_city.name, return_city.country)
    else:
        return ""


# print(max_elevation_city(100000))  # Should print "Cusco, Peru"
# print(max_elevation_city(1000000))  # Should print "Sofia, Bulgaria"
# print(max_elevation_city(10000000))  # Should print ""

# class Furniture:
#     color = ""
#     material = ""


# table = Furniture()
# table.color = "brown"
# table.material = "wood"

# couch = Furniture()
# couch.color = "red"
# couch.material = "leather"


# def describe_furniture(piece):
#     return ("This piece of furniture is made of {} {}".format(piece.color, piece.material))


# print(describe_furniture(table))
# # Should be "This piece of furniture is made of brown wood"
# print(describe_furniture(couch))
# # Should be "This piece of furniture is made of red leather"


class Furniture:
    def __init__(self, color, material):
        self.color = color
        self.material = material


table = Furniture("brown", "wood")
couch = Furniture("red", "leather")


def describe_furniture(piece):
    return (f"This piece of furniture is made of {piece.color} {piece.material}")


# print(describe_furniture(table))
# # Should be "This piece of furniture is made of brown wood"
# print(describe_furniture(couch))
# # Should be "This piece of furniture is made of red leather"


class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

    def __str__(self):
        return f"This apple is {self.color} and its flavor is {self.flavor}"


gold = Apple("Yellow", "Sour")
# print(gold)


class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        # Should return "hi, my name is " followed by the name of the Person.
        return f"hi, my name is {self.name}"


# Create a new instance with a name of your choice
some_person = Person("Thang")
# Call the greeting method
# print(some_person.greeting())

help(Apple)
