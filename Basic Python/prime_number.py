num = 10

for i in range(2, num):
    print("Num", num)
    print("i", i)
    print("Num % i: ", num % i)
    if num % i == 0:
        print("Not Prime")
    else:
        print("Prime")
