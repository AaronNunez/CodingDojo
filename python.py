num1 = 42 # variable declaration, number intitialized
num2 = 2.3 # variable declaration, number intitialized
boolean = True # variable declaration, boolean intitialized
string = 'Hello World' # variable declaration, string intitialized

# variable declaration, list intitialized
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']

# variable declaration, dictionary intitialized
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}

# variable declaration, tuple intitialized
fruit = ('blueberry', 'strawberry', 'banana')

# print to console, type check
print(type(fruit))

# print to console, list access value
print(pizza_toppings[1])

# list add value
pizza_toppings.append('Mushrooms')

# print to console, access value
print(person['name'])

# dictionary changhe value
person['name'] = 'George'

# dictionary changhe value
person['eye_color'] = 'blue'

# print to console, tuple access data
print(fruit[2])

# conditional if, evaluation, print to console, conditional els, print to console
if num1 > 45:
    print("It's greater")
else:
    print("It's lower")

# conditional if - els, print to console
if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

# for loop start at 0 up to 5
for x in range(5):
    print(x)

# for loop start at 2 up t0 5
for x in range(2,5):
    print(x)

# for loop start at 2 up to 10, increments by 3
for x in range(2,10,3):
    print(x)

# while loop, variable declaration
x = 0
while(x < 5):
    print(x)
    x += 1

# list delete value  at end 
pizza_toppings.pop()

# list delete value at index
pizza_toppings.pop(1)

# print to console of dictionary 
print(person)

# dictionary delete value 
person.pop('eye_color')

# print console of dictionary
print(person)


# for loop through list
for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue

    # pritn to console
    print('After 1st if statement')

    # conditional if 
    if topping == 'Olives':

        # stops the loop
        break

def print_hello_ten_times():
    # for loop starts at 0 up to 10
    for num in range(10):

        # print to console
        print('Hello')

print_hello_ten_times()


# function declaration
def print_hello_x_times(x):

    # for loop up tp a given number
    for num in range(x):

        # print to console
        print('Hello')

# function call argument of 4
print_hello_x_times(4)

# function declaration with default parameter
def print_hello_x_or_ten_times(x = 10):

    # for loop until x
    for num in range(x):

        # print to console
        print('Hello')

# function call goes to 10 
print_hello_x_or_ten_times()

# function call goes to 4
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)