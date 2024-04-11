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
GEOBOT="[GeoBot_0773]"

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

str=": Salve esploratore, io sono GeoBot_0773. Creato per guidarti attraverso una straordinaria avventura intorno al mondo. Il mio compito è mettere alla prova la tua abilità di navigazione attraverso i continenti e le loro meraviglie nascoste."
print_animated "$str" "$WHITE"

echo
sleep 0.5
echo

print_animated "$GEOBOT" "$GREEN"

str=": La tua missione, se sceglierai di accettarla, sarà quella di trovare la Chiave del Mondo, una serie di numeri e lettere, suddivisa in alcuni dei luoghi più famosi sparsi per il globo. Per riuscirci, dovrai fare affidamento sulle tue conoscenze geografiche e sulla tua capacità di decifrare gli indizi che ti saranno forniti lungo il cammino."
print_animated "$str" "$WHITE"

echo
sleep 0.5
echo

print_animated "$GEOBOT" "$GREEN"

str=": Il primo passo di questa caccia al tesoro globale è consultare la directory dei continenti. Qui, nascosti in piena vista, troverai indizi che celano le parti della chiave. Ricorda: non tutti i continenti nascondono un pezzo del puzzle. Quando ti chiederò di inserire la soluzione, inserisci i caratteri seguendo l'ordine alfabetico dei continenti in cui li hai trovati."
print_animated "$str" "$WHITE"

# check this out " grep '[0-9]' <path_to_file> "

echo
sleep 0.5
echo

print_animated "$GEOBOT" "$GREEN"

str=": In bocca al lupo, e che la tua bussola interna ti guidi saggiamente!"
print_animated "$str" "$WHITE"

echo
sleep 0.5
echo

output=$(ls)
TARGET_FOLDER="continenti"

for item in $output; do
    sleep 0.5
    if [ "$item" = "$TARGET_FOLDER" ]; then
        printf "${PURPLE}-> %s <-  ${RESET}" "$item"
    else
        printf "%s  " "$item"
    fi
done

echo
sleep 0.5
echo
