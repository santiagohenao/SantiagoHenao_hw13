import numpy as np
import sys

try:
    n=int(sys.argv[1])
except IndexError:
    n=100
except ValueError:
    try:
        n=int(sys.argv[2])
    except IndexError:
        n=100

silent="-s" in sys.argv

def init():
    '''
    Function that initializes monty hall problem simulation.

    returns a list with randomly ordered door's content.
    '''
    return np.random.permutation(["goat","goat","car"])

def first_choice():
    '''
    Emulates the initial choice.
    '''
    return np.random.choice([0,1,2])

def reveal_goat(doors_list,initial_choice):
    '''
    In answer to the initial choice, the machine reveals a door (index of) where is a goat, randomly.
    '''
    possible_indexes=[]
    for i in [0,1,2]:
        if( i!=initial_choice and doors_list[i]=="goat" ):
            # It is not fair to reveal the first goat. Here are considered all scenarios.
            possible_indexes.append(i)
    return np.random.choice(possible_indexes)


def second_choice(change,initial_choice,goat_index):
    '''
    Emulates the second choice, according to the rules of the game.
    '''
    if(change):
        choice=-1;
        for i in [0,1,2]:
            if( i!=goat_index and i!=initial_choice ):
                choice=i
        return choice
    else:
        return initial_choice

def MontyHall(change_arg):
    '''
    Simulates a Monty Hall game, with the changing choice given by the boolean "change".

    Returns True if win the car, False if win a goat.
    '''
    doors=init()
    n1=first_choice()
    goat=reveal_goat(doors,n1)
    n2=second_choice(change_arg,n1,goat)
    if doors[n2]=="goat":
        return False
    if doors[n2]=="car":
        return True

# Set up of several simulations

# Change option, n games

CH_win=0
CH_lose=0

for i in range(n):
    result=MontyHall(True)
    if(result):
        CH_win+=1
    else:
        CH_lose+=1

# Non-change option, n games

N_win=0
N_lose=0

for i in range(n):
    result=MontyHall(False)
    if(result):
        N_win+=1
    else:
        N_lose+=1

# Print the results:

if silent:
    print(round(N_win/n*100,3),round(CH_win/n*100,3))
else:
    print("There was a ",round(N_win/n*100,3),"%  of probabilities to win if one chooses not to change the selected door")
    print("There was a ",round(CH_win/n*100,3),"%  of probabilities to win if one chooses to change the selected door")
