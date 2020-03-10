num = int(input("Please Enter any Number: "))

i= num
while (i>= 10):
    i = i// 10

print("The First Digit from a Given Number {0} = {1}".format(num, i))
number = int(input("Please Enter any Number: "))

last = number % 10

print("The Last Digit in a Given Number %d = %d" %(number, last))
