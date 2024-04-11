RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RESET = "\033[0m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

def hex_to_chars(hex_string):
    chars = ""
    print(MAGENTA + "La conversione finale della soluzione che hai trovato è da esadecimale a carattere seguendo la tabella ASCII" + RESET)
    for i in range(0, len(hex_string), 2):
        hex_byte = hex_string[i:i+2]
        char = chr(int(hex_byte, 16))
        print(RED + hex_byte + RESET + " => " + GREEN + char + RESET)
        chars += char
    return chars

def main():
    hex_string = input("inserisci il tuo hex per convertirlo in testo: ")
    hex_to_chars(hex_string)
    #print("LA SOLUZIONE È: " + MAGENTA + hex_to_chars(hex_string) + RESET)
main()