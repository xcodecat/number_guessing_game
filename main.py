import random
from colorama import init, Fore, Back, Style

init(autoreset=True)

turn = 0
active = True
number_to_guess = random.randint(0, 100)

while active:
    turn = turn+1
    print()
    print(Back.YELLOW + Fore.BLACK + "Turn " + str(turn))
    userinput = int(input(Fore.BLUE + "Please insert number: " ))

    if userinput == number_to_guess:
        print()
        print(Fore.CYAN + "You won!")
        active = False
        break
    elif userinput > number_to_guess:
        print(Fore.RED + Style.BRIGHT + "your guessed number is too big :c")
    elif userinput < number_to_guess:
        print(Fore.RED + Style.BRIGHT + "your guessed number is too small :|")
    
    if turn == 7:
        print()
        print(Fore.RED + "Too bad! Lost :(")
        print(Fore.WHITE + "It was " + Fore.GREEN + str(number_to_guess))
        active = False
print()
print(Style.BRIGHT + Back.BLACK + "The End.")