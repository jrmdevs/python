# while True:
#     print('Hola qué tal')
#     continua = input('continuo?')
#     if continua == 'no':
#         break
# print('Adios')

print('Fill in the blank lyrics!')
print('Type in the blank lyrics and see if you are as cool as me.')

attempts = 0
while True:
    print('Never going to ______ you up.')
    answer = input('')
    if answer == 'give':
        break
    else:
        print('Nope, try again.')
        attempts += 1
print('Well done! It only took you',attempts,'attempts.')