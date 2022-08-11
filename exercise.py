# do exercise here
# upload to github for portfolio
# thank me later when your git graph is as green as the python money u gonna earn


# Task 1

for i in range(3):
    num = int(input("Please Enter a Number to check odd or even: "))
    if (num%2) != 0:
        print("This is an odd number.")
    else:
        print("This is an even number.")


# Task 2 printing numbers with `range()` function (start, stop, step)

num = int(input("Please enter a number to print the range: "))
for i in range(0, num, 2):
    print(i)


#  Task 3 - finding factors of a number

num = int(input("please enter the number to check factors: "))
for i in range (1,num+1):
    if num % i == 0:
        print (i)

# Task 4 - checking for prime number

num = int(input("Please enter a number to check prime number: "))
if num > 1:
        for i in range(2, num//2):
            if (num%i)==0:
                print(num, "is not a prime number")
        else:
            print(num, "is a prime number")

# Task 5 FizzBuzz




