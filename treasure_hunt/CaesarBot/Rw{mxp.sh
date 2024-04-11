RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
WHITE='\033[0;37m'
RESET='\033[0m'
ORANGE='\033[38:5:208m'

UKNOWN="[????]"
JOSEPH="[Joseph]"

print_animated() {
    local message=$1
    local color=$2
    printf "%b" "$color"
    while IFS= read -r -n1 var;
    do
        printf '%s' "$var"
        sleep 0.015
    done <<< "$message"
    printf "%b" "$RESET"
}

case $1 in
    "")
        clear
        print_animated "$UKNOWN" "$RED"
        str=": Salve, io sono Joseph, l'assitente di Caesar."
        print_animated "$str" "$WHITE"

        echo
        sleep 0.3
        echo

        print_animated "$JOSEPH" "$GREEN"
        str=": Dal momento che Caesar sta per essere congedato e io dovrò prendere il suo posto, il creatore mi ha incaricato di sottoporre il prossimo test per dimostrare le mie abilità."
        print_animated "$str" "$WHITE"

        echo
        sleep 0.3
        echo

        print_animated "$JOSEPH" "$GREEN"
        str=": Per cui ascoltami attentamente adesso. Nella cartella "
        print_animated "$str" "$WHITE"
        print_animated "data" "$YELLOW"
        str=" troverai due set di operazioni: "
        print_animated "$str" "$WHITE"
        print_animated "first_op" "$YELLOW"
        print_animated " e " "$WHITE"
        print_animated "second_op" "$YELLOW"
        print_animated "." "$WHITE"

        echo
        sleep 0.3
        echo

        print_animated "$JOSEPH" "$GREEN"
        str=": Il tuo compito sarà di modificare i permessi di ciascuno dei file come ti verrà detto dalla documentazione che ti ho lasciato per ciascuna cartella."
        print_animated "$str" "$WHITE"

        echo
        sleep 0.3
        echo

        print_animated "$JOSEPH" "$GREEN"
        str=": Una volta fatto questo dovrai fare la somma di tutti permessi di ciascun file."
        print_animated "$str" "$WHITE"

        echo
        sleep 0.3
        echo

        print_animated "$JOSEPH" "$GREEN"
        str=": Arrivati a questo punto avrai sicuramente notato che i file sono numerati con un certo ordine e ciascuno di essi termina con un simbolo di un'operazione."
        print_animated "$str" "$WHITE"

        echo
        sleep 0.3
        echo

        print_animated "$JOSEPH" "$GREEN"
        str=": Devi quindi andare ad eseguire queste operazioni nell'ordine in cui sono disposte usando come numeri i risultati della somma dei permessi del file in questione."
        print_animated "$str" "$WHITE"

        echo
        sleep 0.3
        echo

        print_animated "$JOSEPH" "$GREEN"
        str=": Ti faccio un piccolo esempio: poni che tu abbia "
        print_animated "$str" "$WHITE"
        print_animated "1_op_*" "$YELLOW"
        print_animated ", " "$WHITE"
        print_animated "2_op_+" "$YELLOW"
        print_animated ", " "$WHITE"
        print_animated "3_op_-" "$YELLOW"
        print_animated ", " "$WHITE"
        print_animated "4_op_:" "$YELLOW"
        print_animated " e " "$WHITE"
        print_animated "5_op_=" "$YELLOW"
        print_animated "." "$WHITE"

        echo
        sleep 0.3
        echo

        print_animated "$JOSEPH" "$GREEN"
        str=": In questo caso farai la moltiplicazione del totale dei permessi di "
        print_animated "$str" "$WHITE"
        print_animated "1_op_*" "$YELLOW"
        print_animated " e " "$WHITE"
        print_animated "2_op_+" "$YELLOW"
        str=". Al risultato sommerai il totale dei permessi di "
        print_animated "$str" "$WHITE"
        print_animated "3_op_-" "$YELLOW"
        print_animated "." "$WHITE"

        echo
        sleep 0.3
        echo

        print_animated "$JOSEPH" "$GREEN"
        str=": Al nuovo risultato sottrarrai il totale dei permessi di "
        print_animated "$str" "$WHITE"
        print_animated "4_op_:" "$YELLOW"
        str=" ed infine andrai a dividere il risultato per il totale dei permessi di "
        print_animated "$str" "$WHITE"
        print_animated "5_op_=" "$YELLOW"
        print_animated "." "$WHITE"

        echo
        sleep 0.3
        echo

        print_animated "$JOSEPH" "$GREEN"
        str=": Una volta arrivato a questo punto prova a scrivere "
        print_animated "$str" "$WHITE"
        print_animated "man ascii" "$PURPLE"
        str=" e cerca di capire cosa rappresentano quei due numeri (usa le freccette per scorrere verso l'alto e il basso)"
        print_animated "$str" "$WHITE"

        echo
        sleep 0.3
        echo

        print_animated "$JOSEPH" "$GREEN"
        str=": Nel caso in cui volessi rileggere questa spiegazione chiamami pure con "
        print_animated "$str" "$WHITE"
        print_animated "sh Rw{mxp.sh help" "$PURPLE"

        echo
    ;;

    "help")
        print_animated "$JOSEPH" "$GREEN"
        str=": Poni che tu abbia "
        print_animated "$str" "$WHITE"
        print_animated "1_op_*" "$YELLOW"
        print_animated ", " "$WHITE"
        print_animated "2_op_+" "$YELLOW"
        print_animated ", " "$WHITE"
        print_animated "3_op_-" "$YELLOW"
        print_animated ", " "$WHITE"
        print_animated "4_op_:" "$YELLOW"
        print_animated " e " "$WHITE"
        print_animated "5_op_=" "$YELLOW"
        print_animated "." "$WHITE"

        echo
        sleep 0.3
        echo
    ;;
esac
