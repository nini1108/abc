# Using your preferred programming or scripting language, write 
# a function that takes a number as an argument and returns the 
# string “aunty” if that number is divisible by 3 and returns 
# “uncle” otherwise.

print('Enter a number greater than 0:')
num = int(input())

def my_func(arg):
    if arg == 0:
        print ('Please enter another number greater than 0')
    elif (arg % 3) == 0:
        result = 'aunty'
        return result
    else:
        result = 'uncle'
        return result

print (my_func(num))