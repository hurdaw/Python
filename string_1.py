# to replace domain
def replace_old_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@"+old_domain)
        new_email = email[:index]+"@"+new_domain
        return new_email
    return email
# print(replace_old_domain("tn133931@gmail.com", "gmail.com", "yahoo.com"))
# def replace(old, new):
# name = "tn133931@gmail.com"
# print(name.replace(old, new))
# replace("gmail.com", "yahoo.com")


def method_string():
    ten = " Nguyen Hoang Thang "
    print(ten.upper())
    print(ten.lower())
    print(ten.strip())
    print(ten.lstrip())
    print(ten.rstrip())
    print(ten.count("n"))
# check whether the string ends with a certain substring.
    print(ten.endswith("Thang "))
    print(ten.isnumeric())  # check whether the string is numberic
# in earlier lesson I've learnt how to concatenate string by use "+"
# In this lesson, there is a method help me do it
    print(" ".join(["Nguyen", "Hoang", "Thang"]))
    print(ten.split())
    print(" ".join(ten.split()))
    name = "Thang"
    number = len(name)*3
    print("Hello {}, your lucky number is {}".format(name, number))
    print("your lucky number is {number}, {name}".format(
        name=name, number=len(name)*3))
    price = 8.5
    with_tax = price*2.9
    print(price, with_tax)
    print("Base price is: ${:.2f}, with tax is: ${:.2f}".format(
        price, with_tax))
    print(round(price, 2), round(with_tax, 2))


# method_string()


def to_Cencius(x):
    return (x-32)*5/9
# for x in range(0, 101, 10):
# print("{:>3} F | {:>.2f} C".format(x, to_Cencius(x)))
# code skill 1 : Kiểm tra string thuan va dao co bang nhau khong ?


def mirror_string(my_string):
    forwards = ""
    backwards = ""
    for character in my_string:
        if character.isalpha():
            forwards += character
            backwards = character+backwards
    if forwards.lower() == backwards.lower():
        return True
    return False


# print(mirror_string("thang"))


def weight_convert(kilogram):
    pound = 2.20462262*kilogram
    print("{} Kg = {} Pound".format(kilogram, pound))


def weight_conver_table():
    for kilogram in range(1, 101, 10):
        pound = 2.20462262*kilogram
        print("{} Kg = {:.2f} Pound".format(kilogram, pound))


def username(First_name, birth_year):
    print("{}{}".format(First_name[0:3], birth_year))


def replace_date(schedule, old_date, new_date):
    if schedule.endswith(old_date):
        p = len(old_date)
        new_schedule = schedule[:-p] + \
            schedule[-p:].replace(old_date, new_date)
        print(new_schedule)
    else:
        print(schedule)


# replace_date(
#     "Last year's annual report will be released in March 2023", "2023", "2024")
# # Should display "Last year’s annual report will be released in March 2024"
# replace_date("In April, the CEO will hold a conference", "April", "May")
# # Should display "In April, the CEO will hold a conference"
# replace_date("The convention is scheduled for October", "October", "June")
# # Should display "The convention is scheduled for June"


def is_palindrome(input_string):
    # Two variables are initialized as string date types using empty
    # quotes: "reverse_string" to hold the "input_string" in reverse
    # order and "new_string" to hold the "input_string" minus the
    # spaces between words, if any are found.
    new_string = ""
    reverse_string = ""

    # Complete the for loop to iterate through each letter of the
    # "input_string"
    for letter in input_string:

        # The if-statement checks if the "letter" is not a space.
        if letter != " ":

            # If True, add the "letter" to the end of "new_string" and
            # to the front of "reverse_string". If False (if a space
            # is detected), no action is needed. Exit the if-block.
            new_string = new_string+letter
            reverse_string = letter+reverse_string

    # Complete the if-statement to compare the "new_string" to the
    # "reverse_string". Remember that Python is case-sensitive when
    # creating the string comparison code.
    if new_string.lower() == reverse_string.lower():

        # If True, the "input_string" contains a palindrome.
        return True

    # Otherwise, return False.
    return False


def is_palindrome_2(input_strings):
    new_strings = ""
    reverse_strings = ""
    for letter in input_strings:
        if letter != " ":
            new_strings = new_strings+letter
            reverse_strings = letter+reverse_strings
    if new_strings.lower() == reverse_strings.lower():
        return True
    return False
# print(is_palindrome_2("Never Odd or Even"))  # Should be True
# print(is_palindrome_2("abc"))  # Should be False
# print(is_palindrome_2("kayak"))  # Should be True


def replace_ending(sentence, old, new):
    # Check if the old substring is at the end of the sentence
    if sentence.endswith(old):
        # Using i as the slicing index, combine the part
        # of the sentence up to the matched string at the
        # end with the new string
        i = old
        new_sentence = sentence[:-len(old)] + \
            sentence[-len(old):].replace(i, new)
        return new_sentence

    # Return the original sentence if there is no match
    return sentence


# print(replace_ending("It's raining cats and cats", "cats", "dogs"))
# # Should display "It's raining cats and dogs"
# print(replace_ending("She sells seashells by the seashore", "seashells", "donuts"))
# # Should display "She sells seashells by the seashore"
# print(replace_ending("The weather is nice in May", "may", "april"))
# # Should display "The weather is nice in May"
# print(replace_ending("The weather is nice in May", "May", "April"))
# # Should display "The weather is nice in April"

def get_word(sentence, n):
    # Only proceed if n is positive
    if n > 0:
        words = sentence.split(" ")
        # Only proceed if n is not more than the number of words
        if n <= len(words):
            return (words[n-1])
    return ("")
# print(get_word("This is a lesson about lists", 4))  # Should print: lesson
# print(get_word("This is a lesson about lists", -4))  # Nothing
# print(get_word("Now we are cooking!", 1))  # Should print: Now
# print(get_word("Now we are cooking!", 5))  # Nothing


def fruit():
    fruits = ["pineapple", "Banana", "apple", "melon"]
    fruits.append("mango")
    print(fruits)
    fruits.insert(2, "kiwi")
    print(fruits)
    fruits.remove("mango")
    print(fruits)


def convert_seconds(seconds):
    hours = seconds//3600
    minutes = (seconds-hours*3600)//60
    remaing_seconds = seconds-hours*3600-minutes*60
    return hours, minutes, remaing_seconds


def file_size(file_info):
    file_name, file_type, file_size = file_info
    return ("{:.2f}".format(file_info / 1024))


# print(file_size(('Class Assignment', 'docx', 17875)))  # Should print 17.46
# print(file_size(('Notes', 'txt', 496)))  # Should print 0.48
# print(file_size(('Program', 'py', 1239)))  # Should print 1.21
def animals():
    animals = ["lion", "zebra", "dolphin", "monkey"]
    char = 0
    for animal in animals:
        char += len(animal)
    print("Total character: {}, everage length: {}". format(
        char, char / len(animals)))


def winner():
    winner = ["Wisley", "Thang", "Dylan"]
    for index, person in enumerate(winner):
        print("{} - {}".format(index+1, person))


def full_email(people):
    result = []
    for email, name in people:
        result.append("{} <{}>".format(email, name))
    return result


# print(full_email([("Thang", "tn133931@gmail.com"),
#       ("Linh", "ll12233@gmail.com")]))


def skip_elements(elements):
    # code goes here
    result = []
    for i, element in enumerate(elements):
        if i % 2 == 0:
            result.append(element)
    return result
# # Should be ['a', 'c', 'e', 'g']
# print(skip_elements(["a", "b", "c", "d", "e", "f", "g"]))
# # Should be ['Orange', 'Strawberry', 'Peach']
# print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach']))


def languages():
    languages = ["Python", "C", "Java", "Go"]
    lengths = [len(language) for language in languages]
    print(lengths)
    z = [x for x in range(0, 101) if x % 5 == 0]
    print(z)


def test():
    number = [2, 45, 3, 1]
    number_new = [s**2 for s in number]
    print(number_new)


def replace_year():
    years = ["January 2023", "May 2025", "April 2023",
             "August 2024", "September 2025", "December 2023"]
    new_year = []
    for year in years:
        if (year.endswith("2023")):
            new = year.replace("2023", "2024")
            new_year.append(new)
        else:
            new_year.append(year)
    print(new_year)


def square_list(start, end):
    square_number = [x*x for x in range(start, end+1)]
    print(square_number)


def replace_year_list_comprehension():
    years = ["January 2023", "May 2025", "April 2023",
             "August 2024", "September 2025", "December 2023"]
    new_uppdate = [year.replace("2023", "2024") if (
        year.endswith("2023")) else year for year in years]
    print(new_uppdate)


def change_string(given_string):
    new_string = ""
    new_list = []
    new_list = given_string.split()
    for elements in new_list:
        new_string += elements[1:]+"-"+elements[0]+" "
    print(new_string)
# change_string("1one 2two 3three 4four 5five")


def file_change():
    filenames = ["program.c", "stdio.hpp",
                 "sample.hpp", "a.out", "math.hpp", "hpp.out"]
    # Generate newfilenames as a list containing the new filenames
    # using as many lines of code as your chosen method requires.
    newfilenames = []
    for i in filenames:
        if i.endswith(".hpp"):
            new = i.replace(".hpp", ".h")
            newfilenames.append(new)
        else:
            newfilenames.append(i)
    print(newfilenames)


file_change()
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]


def pig_latin(text):
    say = ""
    # Separate the text into words
    words = text.split()
    for word in words:
        # Create the pig latin word and add it to the list
        say += word[1:]+word[0]+"ay"+" "
        # Turn the list back into a phrase
    return say
# print(pig_latin("hello how are you"))  # Should be "ellohay owhay reaay ouyay"
# # Should be "rogrammingpay niay ythonpay siay unfay"
# print(pig_latin("programming in python is fun"))


def group_list(group, users):
    members = (group+":", ','.join(users))
    return ' '.join(members)
# # Should be "Marketing: Mike, Karen, Jake, Tasha"
# print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"]))
# # Should be "Engineering: Kim, Jay, Tom"
# print(group_list("Engineering", ["Kim", "Jay", "Tom"]))
# print(group_list("Users", ""))  # Should be "Users:"


def guest_list(guests):
    for name, age, job in guests:
        print("{} is {} years old and works as {}".format(name, age, job))


# guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'),
#             ('Amanda', 25, "Engineer")])
"""
Output should match:
Ken is 30 years old and works as Chef
Pat is 35 years old and works as Lawyer
Amanda is 25 years old and works as Engineer
"""
