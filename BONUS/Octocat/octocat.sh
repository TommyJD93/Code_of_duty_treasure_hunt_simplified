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
CAT="[Octocat]"

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
str=": Ciao io sono Octocat, la mascot di GitHub :)"
print_animated "$str" "$WHITE"

echo
sleep 0.3
echo

print_animated "$CAT" "$GREEN"
str=": Come prossimo test andrai a creare una tua repository su GitHub e ci caricherai lo script creato con Konzu..."
print_animated "$str" "$WHITE"

echo
sleep 0.3
echo

print_animated "$CAT" "$GREEN"
str=": Dal tuo sguardo sembra quasi che tu non conosca GitHub hahahahahahaha"
print_animated "$str" "$WHITE"

echo
sleep 0.3
echo

print_animated "$CAT" "$GREEN"
str=": Ma sono sicuro che tu lo conosca vero?"
print_animated "$str" "$WHITE"

echo
sleep 0.3
echo

print_animated "$CAT" "$GREEN"
str=": ..."
print_animated "$str" "$WHITE"

echo
sleep 0.3
echo

print_animated "$CAT" "$GREEN"
str=": vero?"
print_animated "$str" "$WHITE"

echo
sleep 0.3
echo

print_animated "$CAT" "$GREEN"
str=": Anche se mi hai lasciato un pochino di sasso non ti preoccupare, adesso ti spiego di cosa si parla..."
print_animated "$str" "$WHITE"

echo
sleep 0.3
echo

print_animated "$CAT" "$GREEN"
str=": GitHub è una piattoaforma per sviluppatori che permette a questi ultimi di creare, conservare, gestire e condividere il proprio codice."
print_animated "$str" "$WHITE"

echo
sleep 0.3
echo

print_animated "$CAT" "$GREEN"
str=": La piattaforma nasce per essere utilizzata da sviluppatori ma ormai viene utilizzata per salvare file di ogni tipo, vedila come una sorta di cloud pubblico."
print_animated "$str" "$WHITE"

echo
sleep 0.3
echo

print_animated "$CAT" "$GREEN"
str=": Mi fermerò qui con la spiegazione, ma sappi che ha moltissime altre funzioni che tornano comodissime per lo sviluppo, quindi se sei interessato ti consiglio fortemente di darci un occhiata."
print_animated "$str" "$WHITE"

echo
sleep 0.3
echo

print_animated "$CAT" "$GREEN"
str=": Tornando a noi... per questo test dovrai fare le seguenti cose: "
print_animated "$str" "$WHITE"

echo
sleep 0.3
echo

printf "\t"
str="1. Creare un account github direttamente dal sito (https://github.com)"
print_animated "$str" "$WHITE"

echo
sleep 0.3
echo

printf "\t"
str="2. Generare una chiave SSH ed inserirla all'interno delle tue chiavi SSH del profilo"
print_animated "$str" "$WHITE"

echo
sleep 0.3
echo

printf "\t"
str="3. Creare una repository sul sito"
print_animated "$str" "$WHITE"

echo
sleep 0.3
echo

printf "\t"
str="4. Creare una cartella in cui verrà inizializzata la repository creata"
print_animated "$str" "$WHITE"

echo
sleep 0.3
echo

printf "\t"
str="5. Spostare lo script da Konzu nella cartella in cui inizializzare la repository"
print_animated "$str" "$WHITE"
echo
sleep 0.3
echo

printf "\t"
str="6. Inizializzare la repository"
print_animated "$str" "$WHITE"

echo
sleep 0.3
echo

printf "\t"
str="7. Pushare lo script su github"
print_animated "$str" "$WHITE"

echo
sleep 0.3
echo

print_animated "$CAT" "$GREEN"
str=": Ora come ora ti sembrerà tantissima roba da fare, ma fidati di me, è più semplice di ciò che sembra."
print_animated "$str" "$WHITE"

echo
sleep 0.3
echo

print_animated "$CAT" "$GREEN"
str=": Comunque... arrivati a questo punto per procedere hai due opzioni: Cercare tutte queste cosa su internet in completa autonomia, oppure consultare la breve documentazione che ti lascio (ti cosniglio la prima)."
print_animated "$str" "$WHITE"


echo
sleep 0.3
echo

print_animated "$CAT" "$GREEN"
str=": Un'ultima cosa prima di lasciarti, gran parte del materiale che troverai online ti spiegherà, tra le varie cose, come installare git, su questi pc git è già installato quindi puoi saltare quella parte."
print_animated "$str" "$WHITE"

echo
echo