import random
from colorama import init, Fore, Back, Style

init(autoreset=True)

turn = 0
active = True
rate_number = random.randint(0, 100)

while active:
    turn = turn+1
    print()
    print(Back.YELLOW + Fore.BLACK + "Turn " + str(turn))
    userinput = int(input(Fore.BLUE + "Please insert number: " ))

    if userinput == rate_number:
        print(Fore.CYAN + "You won!")
        active = False
        break
    elif userinput > rate_number:
        print(Fore.RED + Style.BRIGHT + "your guessed number is too big :c")
    elif userinput < rate_number:
        print(Fore.RED + Style.BRIGHT + "your guessed number is too small :|")
    
    if turn == 7:
        print(Fore.RED + "Too bad! Lost :(")
        print(Fore.WHITE + "It was " + Fore.GREEN + str(rate_number))
        active = False

print(Style.BRIGHT + Back.BLACK + "The End.")