#!/bin/sh
clear

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
WHITE='\033[0;37m'
RESET='\033[0m'

UNKNOWN="[????]"
LOID="[Loid]"

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

str=$1

if ! [[ "$1" =~ [^a-zA-Z] ]] && [ "$2" == "" ] && [ $# -ge 0 ] && [ $# -le 1 ]; then
    case "$1" in
        "")
            clear

            print_animated "$UNKNOWN" "$RED"
            str=": Hey!!!, finalmente è arrivato il nuovo assistente! Era ora...."            
            print_animated "$str" "$WHITE"

            echo
            sleep 0.3
            echo

            print_animated "$LOID" "$GREEN"
            str=": Saluti, umano. Io sono Loid, e sono lieto di darvi il benvenuto nel laboratorio. Suppongo che sarete stanco dopo il test..."
            print_animated "$str" "$WHITE"

            echo
            sleep 0.3
            echo

            print_animated "$LOID" "$GREEN"
            str=": Beh, sarete ancora più stanco dopo aver completato la parte bonus del test! Hahahahaha"
            print_animated "$str" "$WHITE"

            echo
            sleep 0.1
            echo

            print_animated "$LOID" "$GREEN"
            str=": *ahem* *ahem* stavo dicendo, prima di essere interrotto... presumo che sarete stanco..."
            print_animated "$str" "$WHITE"

            echo
            sleep 0.3
            echo

            print_animated "$LOID" "$GREEN"
            str=": Tuttavia, devo chiedervi se vi piacerebbe fare un ultimo piccolo sforzo..."
            print_animated "$str" "$WHITE"

            echo
            sleep 0.3
            echo

            print_animated "$LOID" "$GREEN"
            str=": Per ottenere una visione ancora più chiara delle vostre reali abilità, vogliamo farvi fare altro lavoro, bla bla bla..."
            print_animated "$str" "$WHITE"

            echo
            sleep 0.3
            echo

            print_animated "$LOID" "$GREEN"
            str=": blah blab blah..."
            print_animated "$str" "$WHITE"

            echo
            sleep 0.3
            echo

            print_animated "$LOID" "$GREEN"
            str=": Dai Loid saltiamo divertamente alla parte divertente, I TEST!! :D"
            print_animated "$str" "$WHITE"

            echo
            sleep 0.3
            echo

            print_animated "$LOID" "$GREEN"
            str=": Comunque, come dicevo, questa parte è completamente opzionale, potete tranquillamente rifiutare e prendervi un po' di tempo per riposare."
            print_animated "$str" "$WHITE"

            echo
            sleep 0.3
            echo

            print_animated "$LOID" "$GREEN"
            str=": Tuttavia, se desiderate continuare, potete chiamarmi quando volete con \"sh Loid.sh bonus\" per iniziare questa parte bonus del test."
            print_animated "$str" "$WHITE"

            echo
            echo
        ;;
        "bonus")
            python3 start_bonus.py
        ;;
        *)
            print_animated "$LOID" "$GREEN"
            str=": Credo che intendiate \"sh Loid.sh bonus\", riprovate il comando."
            print_animated "$str" "$WHITE"

            echo
            echo
        ;;
    esac
else

    print_animated "$LOID" "$GREEN"
    str=": *mmmmmh* no, questo proprio non lo conosco.... la stanchezza ti ha dato alla testa."
    print_animated "$str" "$WHITE"

    while IFS= read -r -n1 var; do
        printf '%s' "$var"
        sleep 0.015
    done <<< "$str"

    echo
    echo
fi
