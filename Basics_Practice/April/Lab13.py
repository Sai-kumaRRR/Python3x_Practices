# factorial numbers

# n = 5
# 5 * 4* 3* 2*1 = 120

# n= 3
# 3* 2* 1 = 6

number = int(input("Enter the factorial number\n"))
if number < 0:
    print("factorial")
elif number == 0:
    print("fact", 1)
else:
    fact = 1

    for i in range(1, number + 1):
        fact = fact * i

        print("fact ->", fact)
