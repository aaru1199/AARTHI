# Take input from user
num = int(input("Enter any number : "))

temp= num
p= 1;

while(t != 0):

    p = p*(t % 10);

    # Remove last digit from temp.
    t= int(t / 10)

print("Product of all digits in", num, ":", p)
