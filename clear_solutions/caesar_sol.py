RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RESET = "\033[0m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

print(GREEN + "Inserisci la chiave decifrata per verificate se sia corretta" + RESET)
val = input(MAGENTA + "Chiave in chiaro: " + YELLOW)

if (val != "MaRViN"):
    print( RED + "La chiave è incorretta, ritenta :(" + RESET)
    exit()

print(GREEN + "La chiave è corretta, adesso puoi procedere con la seconda parte :)" + RESET)

with open(".sol_k", "w") as file:
    pass