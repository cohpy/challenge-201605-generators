def multiples(n):
    while n > 0:
        if n % 3 == 0 or n % 5 == 0:
            yield n
        n -= 1

def get_number_from_user():
    while True:
        try:
            input_number = int(input('Please enter a positive number:  '))
            if 0 < input_number: 
                return input_number
            print ("The number entered is not a positive number.\n"
                   'Please try again.')
        except ValueError:
            print ('That was not a whole number.  Please try again.')
			
def euler_one_generator(n):
    result = 0
    for i in multiples(n):
        result += i
    return result
