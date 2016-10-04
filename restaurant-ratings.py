
import sys
from random import choice

def add_restaurant(restaurant_ratings):
    """"Prompts user for additional restaurants"""

    new_restaurant = raw_input("Please add a restaurant: ").title()
    
    restaurant_ratings[new_restaurant] = \
                        int(raw_input("Review score for added restaurant: "))
    


def get_ratings(filename):
    """Return sorted list of restaurants and ratings.

    Reads in restaurants and ratings from file. Calls add_restaurant to
    prompts user for additional restaurants and ratings. Stores in dictionary 
    and prints alphabetically stored restaurant list with ratings.

    """

    restaurant_ratings = {}

    # Read in restaurants from file
    with open(filename) as openfile:
        for line in openfile:
            line = line.rstrip()
            review = line.split(':')
            restaurant, rating = review
            restaurant_ratings[restaurant] = rating
    
    keep_going = True

    while keep_going:

        decision = int(raw_input("Please enter a number.\n1. View ratings\n2. Add new restaurant\n3. Update restaurant rating\n4. Quit\n"))
        
        if decision == 1:
            for item in sorted(restaurant_ratings.keys()):
                print "{} is rated at {}.".format(item, restaurant_ratings[item])
        elif decision == 2:
            add_restaurant(restaurant_ratings)
        elif decision == 3:
            random_rest = choice(restaurant_ratings.keys())
            restaurant_ratings[random_rest] = int(raw_input("How would you like to score {}? ".format(random_rest)))
        elif decision == 4:
            keep_going = False
        else:
            print "Invalid input"


get_ratings(sys.argv[1])


