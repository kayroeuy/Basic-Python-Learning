x = int(input('What you want to order this product? '))
avaraible = 5
i = 1

while i <= x:
    if i > avaraible:
        print("Product out of stock !")
        break
    print('Candy')
    i += 1


# Continue: keep execute statement

for i in range(1,100):
    if i % 3 != 0:
        continue
    print(i)

#Pass

for i in range(1, 10):
    if (i%2 != 0):
        pass
    else:
        print(i)

