# understand lists ,[]<<< this containts the list

numbers = [0,1,2,3,4,5,6,7,8,9]

print(numbers)

# a list also contain lengths so if we use the len() method we get amount of numbers aboive which is 10 

print(len(numbers))

# Now we inorder to get the last number "9" we use type. The first element in coding for example the above sequence will show that 1 = 0, 2= 1 and so on. 

print(numbers[1])

# now in order to get the number 9 we can use the len method however below will show 

print([len(numbers)-1])

# in order to list all the numbers we are going to use the "for loop" method it will assign the numbers to number varibale

for number in numbers:
  print(number)

# I am now going to multiply the list to the power of 2 

for number in numbers:
  print(number**2)

# we are going to use boolean - it decides whether something is True or False. We are figuring out if 5 is greater than 3. 

print(numbers)

greater_than_three = 5 > 3 
print(greater_than_three)

equal_to_five = 5 == 5
print (equal_to_five)

# here I used the boolean method to check if all the numbers in the list were greater than 5

print(numbers)

# we are using the "if" statement to get another form of responses. 

for number in numbers:
  print(number > 5)

if 5 > 3:
  print("Five is greater than three")

if 3 < 5 :
  print("this should not happen")

# now to get the numbers printed that are greater than 5 with the boolean expression within in

for number in numbers:
  if number > 5 :
    print(number)

# we are going to look at "in" keyword 

print(10 in numbers)

# we are going to create out magic numbers app 

magic_numbers = [3,9]
user_number = 4 

if user_number in [3,9]:
  print("okay")
else:
  print("try again ")

# we imported a package called random which enables the user type any number and still get it wrong basically.

import random

# used the random method to pick out what would be the smallest number in value against 100 or against the list of random values. 

minimum = 100 

for index in range(10):
  random_number = random.randint(0,100)
  print("the number is {}". format(random_number))
  if random_number <= minimum:
    minimum = random_number
    
print(minimum)
