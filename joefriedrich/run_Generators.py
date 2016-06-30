#If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. 
#The sum of these multiples is 23.
#
#Find the sum of all the multiples of 3 or 5 below 1000.

from Generators import get_number_from_user
from Generators import euler_one_generator

print(euler_one_generator(get_number_from_user()))
