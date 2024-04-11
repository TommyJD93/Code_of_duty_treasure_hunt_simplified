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
BOTIFY="[Botify]"

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

if [ $# -ge 0 ] && [ $# -le 1 ]; then
    case "$1" in
        "")
            for i in {1..3}; do
                print_animated "$UNKNOWN" "$RED"
                print_animated ": ..." "$WHITE" 
                sleep 0.5
                echo
                echo
            done

            print_animated "$UNKNOWN" "$RED"

            str=": Hey, scusa se non ti ho sentito arrivare, avevo il volume troppo alto... "
            print_animated "$str" "$WHITE"

            sleep 0.2

            str="io sono Botify, piacere! Sei qui per il test, giusto?"
            print_animated "$str" "$WHITE"

            echo
            sleep 0.5
            echo

            print_animated "$BOTIFY" "$GREEN"
            str=": Che domanda stupida... Che altra motivazione avrebbe una creatura come te per essere qui? Hahahaha ;)"
            print_animated "$str" "$WHITE"

            echo
            sleep 0.3
            echo

            print_animated "$BOTIFY" "$GREEN"
            str=": Come avrai intuito dal mio nome, gestisco le playlist del nostro creatore."
            print_animated "$str" "$WHITE"

            echo
            sleep 0.3
            echo
            
            print_animated "$BOTIFY" "$GREEN"

            str=": Per valutare le tue abilità, ti affiderò uno dei compiti più semplici che svolgo quotidianamente: ordinare le canzoni nelle playlist."
            print_animated "$str" "$WHITE"

            echo
            sleep 0.3
            echo

            print_animated "$BOTIFY" "$GREEN"
            str=": Ti ho lasciato una cartella chiamata "
            print_animated "$str" "$WHITE"
            print_animated "media" "$YELLOW"
            str=" con all'interno alcuni file. Ti chiedo di creare una playlist "
            print_animated "$str" "$WHITE"
            print_animated "Rock" "$YELLOW"
            str=" e una playlist "
            print_animated "$str" "$WHITE"
            print_animated "Rap" "$YELLOW"
            str=". Le due cartelle delle playlist devono essere chiamate ESATTAMENTE in questo modo."
            print_animated "$str" "$WHITE"

            echo
            sleep 0.3
            echo

            print_animated "$BOTIFY" "$GREEN"
            str=": Nel caso in cui non conoscessi i generi delle canzoni che ho selezionato per te (il che sarebbe veramente deludente), puoi consultarmi quando vuoi per ottenere una lista delle canzoni con il relativo genere! :D"
            print_animated "$str" "$WHITE"

            echo
            sleep 0.3
            echo

            print_animated "$BOTIFY" "$GREEN"
            str=": Per vedere la lista delle canzoni per genere, usa "
            print_animated "$str" "$WHITE"
            print_animated "sh Botify.sh genere" "$PURPLE"

            echo
            sleep 0.3
            echo

            print_animated "$BOTIFY" "$GREEN"
            str=": Solo per essere chiari... le playlist che creerai dovranno essere inserite in una cartella di nome "
            print_animated "$str" "$WHITE"
            print_animated "playlists" "$YELLOW"
            print_animated "." "$WHITE"

            echo
            sleep 0.3
            echo

            print_animated "$BOTIFY" "$GREEN"
            str=": Prima di lasciarti voglio darti un'ultimo consiglio... Dai un'occhiata ai testi delle canzoni in ordine alfabetico per altri eventuali indizi ;)."
            print_animated "$str" "$WHITE"

            echo
            sleep 0.3
            echo
        ;;
        "genere")
            print_animated "$BOTIFY" "$GREEN"
            str=": Sono molto deluso..."
            print_animated "$str" "$WHITE"

            echo
            sleep 0.3
            echo

            print_animated "$BOTIFY" "$GREEN"
            str=": Eccoti la lista :/"
            print_animated "$str" "$WHITE"

            sleep 0.5

            echo
            sleep 0.3
            echo

            echo "- Hotel California - Eagles | Rock"
            echo "- Hysteria - Muse | Rock"
            echo "- Alien Blues - Vundabar | Rock"
            echo "- Brain Stew - Green Day | Rock"
            echo "- The Real Slim Shady - Eminem | Rap"
            echo "- Many Men - 50 Cent | Rap"
            echo "- What's The difference - Dr.Dre | Rap"
            echo "- All Eyez On Me - 2Pac | Rap"
        ;;
        *)
            echo
            echo "Errore: argomento non valido."
            echo "Puoi chiamare Botify solamente con: \"sh Botify.sh\" o \"sh Botify.sh genere\""
            echo
            exit 1
        ;;
    esac
else
    echo
    echo "Errore: numero di argomenti non valido."
    echo "Puoi chiamare Botify solamente con: \"sh Botify.sh\" o \"sh Botify.sh genere\""
    echo
    exit 1
fi
