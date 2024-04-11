#!/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
WHITE='\033[0;37m'
RESET='\033[0m'
ORANGE='\033[38;5;208m'

UNKNOWN="[????]"
CAESAR="[CaesarBot]"

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

case "$1" in
    "")
        print_animated "$UNKNOWN" "$RED"
        str=": Jmv~mv}|i {quxi|qki kzmi|}zi4 qw {wvw Kim{iz m y}m{|w qt uqw i{{q{|mv|m Rw{mxp"
        print_animated "$str" "$WHITE"

        echo
        sleep 0.3
        echo

        print_animated "$UNKNOWN" "$RED"
        str=": *Ahem* *ahem* devi scusarmi, non sono abituato a parlare la vostra lingua, ad ogni modo..."
        print_animated "$str" "$WHITE"

        echo
        sleep 0.3
        echo

        print_animated "$CAESAR" "$GREEN"
        str=": Piacere di conoscerti, curiosa creatura. Il mio nome è Kim{iz e sono incaricato della cifratura dei dati del laboratorio."
        print_animated "$str" "$WHITE"

        echo
        sleep 0.3
        echo

        print_animated "$CAESAR" "$GREEN"
        str=": Anche se dovrei dire ex-incaricato della cifratura, visto che a breve verrò sostituito da una mia versione più aggiornata ç.ç"
        print_animated "$str" "$WHITE"

        echo
        sleep 0.3
        echo

        print_animated "$CAESAR" "$GREEN"
        str=": Ma non perdiamo tempo in chiacchiere, il mio test consiste nella decifratura di una parola che è stata divisa e nascosta nei precedenti test. Se non sbaglio, dovresti avere le due parti con te..."
        print_animated "$str" "$WHITE"

        echo
        sleep 0.3
        echo

        print_animated "$CAESAR" "$GREEN"
        str=": Assieme alle due parti della parola, dovresti anche avere una chiave con te, giusto?"
        print_animated "$str" "$WHITE"

        echo
        sleep 0.3
        echo

        print_animated "$CAESAR" "$GREEN"
        str=": Bene, come prima cosa direi di mettere insieme quello che hai, per poi passare al vero e proprio test..."
        print_animated "$str" "$WHITE"

        echo
        sleep 0.3
        echo

        print_animated "$CAESAR" "$GREEN"
        str=": Prima di andare, lasciami spiegare in cosa consisterà."
        print_animated "$str" "$WHITE"

        echo
        sleep 0.3
        echo

        print_animated "$CAESAR" "$GREEN"
        str=": Con l'aiuto degli script che ti ho lasciato "
        print_animated "$str" "$WHITE"
        print_animated "(hex.py, cifratura.sh e decifratura.sh) " "$YELLOW"
        str="dovrai mettere insieme e decifrare i due pezzi di parola che hai."
        print_animated "$str" "$WHITE"

        echo
        sleep 0.3
        echo

        print_animated "$CAESAR" "$GREEN"
        str=": Una volta fatto ciò, chiama pure lo script "
        print_animated "$str" "$WHITE"
        print_animated "solution_Caesar.py" "$YELLOW"
        str=". Quando avrai trovato la soluzione corretta, rivolgiti pure al mio assistente e lui ti dirà come procedere..."
        print_animated "$str" "$WHITE"

        echo
        sleep 0.3
        echo

        print_animated "[Kim{iz]" "$ORANGE"
        str=": Umano, questo è il mio ultimo enigma! Prendilo!"
        print_animated "$str" "$WHITE"

        echo
        echo
    ;;
    *)
        echo
        echo "Errore: numero di argomenti non valido."
        echo "Puoi chiamare CaesarBot solamente"
    ;;
esac