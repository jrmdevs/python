from getpass import getpass as input

print('E P I C  rock-paper-scissors  B A T T L E\n')

print('Select your move (R, P or S)\n')

player_1 = input('Player 1 > ')
player_2 = input('Player 2 > ')

if player_1 == 'R':
    player1_move= "rock"
elif player_1 == 'P':
    player1_move= "paper"
elif player_1 == 'S':
    player1_move= "scissors"
else:
    print('Wrong move, try again')
    exit

if player_2 == 'R':
    player2_move= "rock"
elif player_2 == 'P':
    player2_move= "paper"
elif player_2 == 'S':
    player2_move= "scissors"
else:
    print('Wrong move, try again')
    exit


if player_1 == 'R':
    if player_2 == 'P':
        print("Player1's ",player1_move, " win player2's",player2_move)
    elif player_2 == 'S':
        print("Player1's ",player1_move, " loose player2's",player2_move)
    else:
        print("Player1's ",player1_move, " tie player2's",player2_move)

if player_1 == 'P':
    if player_2 == 'P':
        print("Player1's ",player1_move, " tie player2's",player2_move)
    elif player_2 == 'S':
        print("Player1's ",player1_move, " loose player2's",player2_move)
    else:
        print("Player1's ",player1_move, " win player2's",player2_move)

if player_1 == 'S':
    if player_2 == 'P':
        print("Player1's ",player1_move, " win player2's",player2_move)
    elif player_2 == 'S':
        print("Player1's ",player1_move, " tie player2's",player2_move)
    else:
        print("Player1's ",player1_move, " loose player2's",player2_move)