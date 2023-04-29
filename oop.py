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


exchange_apples(johanna, martin)
print("Johanna has {} apples and Martin has {} apples".format(
    johanna.apples, martin.apples))
exchange_ideas(johanna, martin)
print("Johanna has {} ideas and Martin has {} ideas".format(
    johanna.ideas, martin.ideas))
