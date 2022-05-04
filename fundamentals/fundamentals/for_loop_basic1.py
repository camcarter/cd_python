#1 Basic - Print all integers from 0 to 150.
for i in range (1, 151):
    print (i)

#2 Multiples of Five - Print all the multiples of 5 from 5 to 1,000.
for i in range(1, 1001):
    if(i % 5==0):
        print(i)

#3 Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
def divisible():
    for i in range (1, 101):
        if i % 5==0:
            print("Coding")
        if i % 10==0:
            print("Coding Dojo")
divisible()
#4 Add odd integers from 0 to 500,000, and print the final sum.
minimum = 0
maximum = 500000
oddtotal = 0

for number in range(minimum, maximum+1):
    if(number % 2 != 0):
        print("{0}".format(number))
        oddtotal = oddtotal + number
print("the sum of odd numbers from {0} to {1} = {2}".format(minimum, maximum, oddtotal))
# 4 cont. the sum of odd numbers from 0 to 500000 = 62500000000

#5 Print positive numbers starting at 2018, counting down by fours.
def count_down_four():
    number = 2018
    while number > 0:
        print(number)
        number = number - 4
count_down_four()

#6 Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. 
# For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines).
def flex_countdown(low, high, mult):
    for i in range(low, high):
        if i % mult==0:
            print(i)
flex_countdown(2, 9, 3)