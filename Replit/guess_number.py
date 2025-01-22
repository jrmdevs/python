print("One Million to One")
print()

number = int(500000)
attempt = 1
while True:
    guess = int(input("What is your guess?: "))
    if guess < 0 :
        print("Only positive numbers. Bye")
        exit()
    else:
        if guess < number :
            print("Too low")
            attempt += 1
            continue
        elif guess > number :
            print("Too high")
            attempt += 1
            continue
        else:
            print("Correct number! It took you a total of", attempt, "attempts to get the correct answer.")
            break
        exit()
