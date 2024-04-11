#!/bin/sh

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
WHITE='\033[0;37m'
RESET='\033[0m'

UNKNOWN="[????]"
MARVIN="[MaRViN]"

clear

print_animated() {
    local message="$1"
    local color="$2"
    printf "%b" "$color"
    while IFS= read -r -n1 var;
    do
        printf '%s' "$var"
        sleep 0.015
    done <<< "$message"
    printf "%b" "$RESET"
}

print_animated "$UNKNOWN" "$RED"

str=": Saluti umano, io sono MaRViN. Il mio creatore mi ha programmato per aiutare creature come te a navigare la complessa struttura del nostro alveare. Il mio creatore sta cercando un nuovo assistente umano per il suo laboratorio, pertanto le tue abilità adesso verranno testate... Se ti stai chiedendo se puoi rifiutarti, la risposta è no, non puoi rifiutarti."
print_animated "$str" "$WHITE"

echo
sleep 0.5
echo

print_animated "$MARVIN" "$GREEN"

str=": Il test al quale sarai sottoposto consiste in una caccia al tesoro, dovrai trovare la chiave del laboratorio. Avrai bisogno di tutte le conoscenze che hai acquisito fino ad ora, e forse qualcuna in più :)"
print_animated "$str" "$WHITE"

echo
sleep 0.5
echo

print_animated "$MARVIN" "$GREEN"

str=": Per trovare la chiave dovrai chiedere e cercare indizi dai vari membri dell'alveare."
print_animated "$str" "$WHITE"

echo
sleep 0.5
echo

print_animated "$MARVIN" "$GREEN"

str=": Prima di cominciare con l'effettivo test, direi di fare un piccolo riscaldamento. Ti chiedo quindi di andare nella cartella chiamata "
print_animated "$str" "$WHITE"

print_animated "practice" "$YELLOW"

str=", crearci una cartella chiamata "
print_animated "$str" "$WHITE"

print_animated "MaRViN_stuff" "$YELLOW"
 
str=" e di eliminarne un'altra già al suo interno chiamata "
print_animated "$str" "$WHITE"

print_animated "MaRViN_secrets" "$YELLOW"

printf "."

echo
sleep 0.5
echo

print_animated "$MARVIN" "$GREEN"

str=": Una volta fatto ciò dovrai lanciare lo script solution.py in questo modo: "
print_animated "$str" "$WHITE"

echo
sleep 0.5
echo

solution="python3 solution.py"

print_animated "$solution" "$PURPLE"

echo
sleep 0.5
echo

print_animated "$MARVIN" "$GREEN"

str=": Ricorda che questo comando dovrà essere ripetuto in tutti i livelli per verificare le soluzioni."
print_animated "$str" "$WHITE"

echo
sleep 0.5
echo

print_animated "$MARVIN" "$GREEN"

str=": Buona fortuna! Divertiti! Non morire!"
print_animated "$str" "$WHITE"

echo
sleep 0.5
echo
