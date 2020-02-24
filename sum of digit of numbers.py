Num = int(input("Please Enter any Number: "))
Sum = 0

while(Num > 0):
    Reminder = Num % 10
    Sum = Sum + Reminder
    Num = Num //10

print(" Sum of the digits of Given Number =" %Sum)
