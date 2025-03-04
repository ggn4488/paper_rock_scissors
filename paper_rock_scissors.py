import random
import os

# Shows score
def show_score():
    print("\nSCORE:")
    print("You: {}".format(your_score))
    print("CPU: {}".format(cpu_score))

# Plays
def play(your_score, cpu_score):
    bets = ['Paper', 'Rock', 'Scissors']
    print("\nPlace your bet: ")
    print("0 - Paper | 1 - Rock | 2 - Scissors")
    your_bet = int(input())
    cpu_bet = random.randint(0,2)
    print("Your bet: {}".format(bets[your_bet]))
    print("CPU's bet: {}".format(bets[cpu_bet]))

    if your_bet == cpu_bet:
        print("It's a draw")
        
    elif your_bet == 0 and cpu_bet == 1:
        print("You won!")
        your_score += 1 
    
    elif your_bet == 0 and cpu_bet == 2:
        print("You lose!")
        cpu_score += 1

    elif your_bet == 1 and cpu_bet == 0:
        print("You lose!")
        cpu_score += 1

    elif your_bet == 1 and cpu_bet == 2:
        print("You won!")
        your_score += 1

    elif your_bet == 2 and cpu_bet == 0:
        print("You won!")
        your_score += 1

    elif your_bet == 2 and cpu_bet == 1:
        print("You lose!")
        cpu_score += 1

    return(your_score, cpu_score)

your_score = 0
cpu_score = 0

print("===================================")
print("Welcome to paper, rock and scissors")
print("===================================")

wish = 1

while wish == 1:
    
    show_score()
    your_score, cpu_score = play(your_score, cpu_score)
    print("Wish to play again? 1 - Sim | 0 - No")
    wish = int(input())
    os.system('cls')

print("Final score:")
print("You: {}".format(your_score))
print("CPU: {}".format(cpu_score))