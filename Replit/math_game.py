print("Math Game!")
print()
fails = 0
multiple = int(input("Name your multiples: "))
for i in range(1,11):
    print(i," X ",multiple,"= ")
    result = int(input())
    if result == i*multiple:
        print("Great work!")
    else:
        print("Nope. The answer was ",i*multiple)
        fails += 1
print("You scored ",fails," out of ",10)
