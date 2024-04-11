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
SIMARIS="[Simaris]"

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
        clear
        print_animated "$UNKNOWN" "$RED"
        str=": Benvenuto nel mio santuario umano, sono Simaris. Sono incaricato della gestione e dell'analisi di tutti i dati che il laboratorio raccoglie. Immagino tu sia qui per il test, vero?"
        print_animated "$str" "$WHITE"

        echo
        sleep 0.3
        echo

        print_animated "$SIMARIS" "$GREEN"
        str=": Visto che non abbiamo tempo da perdere, andrò subito al punto. Per trovare il mio indizio, ossia la Chiave dei Dati, dovrai analizzare una serie di dati presenti nel santuario..."
        print_animated "$str" "$WHITE"

        echo
        sleep 0.3
        echo

        print_animated "$SIMARIS" "$GREEN"
        str=": In ciascuna di queste serie di dati, troverai un pezzo della chiave che poi dovrai comporre da solo..."
        print_animated "$str" "$WHITE"

        echo
        sleep 0.3
        echo

        print_animated "$SIMARIS" "$GREEN"
        str=": Per farlo, avrai bisogno di uno dei miei strumenti più potenti. Si tratta del comando "
        print_animated "$str" "$WHITE"
        print_animated "grep" "$PURPLE"
        str=" combinato con "
        print_animated "$str" "$WHITE"
        print_animated "wc -l" "$PURPLE"
        str=". Per unire questi due strumenti, dovrai utilizzare un terzo strumento, ovvero il carattere "
        print_animated "$str" "$WHITE"
        print_animated "|" "$PURPLE"
        print_animated "." "$WHITE"

        echo
        sleep 0.3
        echo

        print_animated "$SIMARIS" "$GREEN"
        str=": Visto che probabilmente non conosci questi strumenti, te li spiegherò io: "
        print_animated "$str" "$WHITE"
        print_animated "grep" "$PURPLE"
        str=" ti permetterà di trovare le occorrenze di una parola in un file, mentre "
        print_animated "$str" "$WHITE"
        print_animated "wc -l" "$PURPLE"
        str=" ti aiuterà a contare il numero totale di righe in cui l'occorrenza è presente."
        print_animated "$str" "$WHITE"

        echo
        sleep 0.3
        echo

        print_animated "$SIMARIS" "$GREEN"
        str=": Capisco che potresti essere un po' confuso, quindi ho preparato per te un piccolo esempio: "
        print_animated "$str" "$WHITE"
        print_animated "grep <cosa_vuoi_cercare> <file_in_cui_vuoi_cercare> | wc -l" "$PURPLE"
        str=". Se questo non fosse sufficiente, ho anche preparato un esempio pratico che puoi utilizzare in qualsiasi momento: basta eseguire "
        print_animated "$str" "$WHITE"
        print_animated "sh example.sh" "$PURPLE"
        print_animated "." "$WHITE"

        echo
        sleep 0.3
        echo

        print_animated "$SIMARIS" "$GREEN"
        str=": Una volta capito come usare questi strumenti, puoi cominciare a cercare 2 nei dataset che ho preparato appositamente per te, buona fortuna :)"
        print_animated "$str" "$WHITE"

        echo
        sleep 0.3
        echo

        print_animated "$SIMARIS" "$GREEN"
        str=": Giusto per essere chiari, i due dataset in questione sono: "
        print_animated "$str" "$WHITE"
        print_animated "simaris_data1.txt" "$YELLOW"
        print_animated " - " "$WHITE"
        print_animated "simaris_data2.txt" "$YELLOW"
        print_animated " ;)" "$WHITE"

        echo
        sleep 0.3
        echo

        print_animated "$SIMARIS" "$GREEN"
        str=": Se necessiti di ulteriori aiuti, posso darti qualche altro piccolo indizio. Nel caso in cui ti servisse, chiamami specificando il nome del dataset su cui hai difficoltà (esempio: "
        print_animated "$str" "$WHITE"
        print_animated "sh Simaris.sh 1" "$PURPLE"
        str="). Buona fortuna!"
        print_animated "$str" "$WHITE"

        echo
        echo
    ;;
    1)
        print_animated "$SIMARIS" "$GREEN"
        str=": Per capire cosa cercare nel primo dataset, ti consiglio di rileggere attentamente ciò che ti avevo scritto precedentemente nel mio penultimo messaggio."
        print_animated "$str" "$WHITE"

        echo
        echo
    ;;
    2)
        print_animated "$SIMARIS" "$GREEN"
        str=": Per capire cosa cercare nel secondo dataset, ti consiglio di comprendere l'argomento principale di cui si parla al suo interno."
        print_animated "$str" "$WHITE"

        echo
        echo
    ;;
    *)
        echo
        echo "Errore: argomento non valido."
        echo "Puoi chiamare Simaris solamente con: \"sh Simaris.sh\", \"sh Simaris.sh 1\" o \"sh Simaris.sh 2\""
        echo
        exit 1
    ;;
    esac

else
    echo
    echo "Errore: numero di argomenti non valido."
    echo "Puoi chiamare Simaris solamente con: \"sh Simaris.sh\", \"sh Simaris.sh 1\" o \"sh Simaris.sh 2\""
    #3
fi