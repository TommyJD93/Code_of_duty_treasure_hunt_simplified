#!/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
WHITE='\033[0;37m'
RESET='\033[0m'

UNKNOWN="[????]"
KONZU="[Konzu]"

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

clear

print_animated "$UNKNOWN" "$RED"
str=": Swazdo-lah umano, benvenuto nel laboratorio, siediti. Io sono Konzu."
print_animated "$str" "$WHITE"

echo
sleep 0.3
echo

print_animated "$KONZU" "$GREEN"
str=": Allora, come primo test, te devi fare uno script in sh che fa 'ste cose qua:"
print_animated "$str" "$WHITE"

echo
sleep 0.3
echo

printf "\t"
str="- fai na cartella chiamata Cetus"
print_animated "$str" "$WHITE"

echo
sleep 0.3
echo

printf "\t"
str="- fai 10 file da 1 a 10 (tipo file1, file2,... file10)"
print_animated "$str" "$WHITE"

echo
sleep 0.3
echo

printf "\t"
str="- butta li 10 file dentro la cartella che hai fatto"
print_animated "$str" "$WHITE"

echo
sleep 0.3
echo

print_animated "$KONZU" "$GREEN"
str=": Prima di iniziare, ci sono un paio di regole per sto test:"
print_animated "$str" "$WHITE"

echo
sleep 0.3
echo

printf "\t"
str="1. Non puoi fare i file uno per uno, devi usà un ciclo for."
print_animated "$str" "$WHITE"

echo
sleep 0.3
echo

printf "\t"
str="2. Fai le cose come vuoi (tipo prima fai i file e poi li butti, o li butti mentre li fai)."
print_animated "$str" "$WHITE"

echo
sleep 0.3
echo

print_animated "$KONZU" "$GREEN"
str=": Se hai problemi collo script o coi cicli, c'è na piccola documentazione che te può dare una mano."
print_animated "$str" "$WHITE"

echo
echo
