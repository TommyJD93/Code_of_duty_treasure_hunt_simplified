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
PIETRO="[San_Pietro_bot]"

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
str=": Ecco qui il nuovo arrivato..."
print_animated "$str" "$WHITE"

echo
sleep 0.3
echo

print_animated "$UNKNOWN" "$RED"
str=": Io sono San Pietro bot, il custode di tutte le chiavi SSH utilizzate per il trasferimento dei dati all'interno del laboratorio."
print_animated "$str" "$WHITE"

echo
sleep 0.3
echo

print_animated "$PIETRO" "$GREEN"
str=": Visto che non abbiamo molto tempo andiamo subito alla spiegazione del test."
print_animated "$str" "$WHITE"

echo
sleep 0.3
echo

print_animated "$PIETRO" "$GREEN"
str=": Tutto quello che dovrai fare in questo test è creare una chiave SSH."
print_animated "$str" "$WHITE"

echo
sleep 0.3
echo

print_animated "$PIETRO" "$GREEN"
str=": Nel caso non conoscessi il protocollo SSH ti ho lasciato della documentazione a riguardo nel file doc.txt. Troverai anche altre risorse utili."
print_animated "$str" "$WHITE"

echo
sleep 0.3
echo

print_animated "$PIETRO" "$GREEN"
str=": Per questo test puoi usare quelle oppure cercare da solo informazioni a riguardo, ma nota che per questo test non avrai bisogno di usare nessuna flag assieme al comando per generare la chiave SSH."
print_animated "$str" "$WHITE"

echo
echo
