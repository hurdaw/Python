"""This module contains a code example related to
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com
Copyright 2015 Allen Downey
License: http://creativecommons.org/licenses/by/4.0/
"""

from __future__ import print_function, division

# here is a mostly-straightforward solution to the
# two-by-two version of the grid.


def do_twice(f):
    f()
    f()


def do_four(f):
    do_twice(f)
    do_twice(f)


def print_beam():
    print('+ - - - -', end=' ')


def print_post():
    print('|        ', end=' ')


def print_beams():
    do_twice(print_beam)
    print('+')


def print_posts():
    do_twice(print_post)
    print('|')


def print_row():
    print_beams()
    do_four(print_posts)


def print_grid():
    do_twice(print_row)
    print_beams()


print_grid()


comment = """
After writing a draft of the 4x4 grid, I noticed that many of the
functions had the same structure: they would do something, do
something else four times, and then do something else once.
So I wrote one_four_one, which takes three functions as arguments; it
calls the first one once, then uses do_four to call the second one
four times, then calls the third.
Then I rewrote print1beam, print1post, print4beams, print4posts,
print_row and print_grid using one_four_one.
Programming is an exploratory process.  Writing a draft of a program
often gives you insight into the problem, which might lead you to
rewrite the code to reflect the structure of the solution.
--- Allen
"""

print(comment)
