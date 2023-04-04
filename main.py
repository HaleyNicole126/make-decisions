import random

# initializing list
# test_list = [1, 4, 5, 2, 7]
choices = input("What are the options? (put a space between each option)")

test_list = choices.split()
# printing original list
print("Original list is : " + str(test_list))

# using random.choice() to
# get a random number
random_ch = random.choice(test_list)
 
# printing random number
print("Random selected choice is : " + str(random_ch))
