if [[ "$1" == "" || "$2" == "" ]]; then
    echo
    echo "Errore: numero di parametri invalido"
    echo "utilizzo previsto dello script: \"sh decifratura.sh <stringa da decifrare> <chiave di decifratura>\""
    echo
    exit 1
fi

str=$1
key=$2
if ! [[ "$str" =~ [^a-zA-Z] && "$key" =~ [^0-9] ]]; then
    echo
    printf "stringa decifrata: \"  "
    while read -n 1 letter
    do
        case $letter in
        '')
            printf ' '
        ;;
        ' ')
            printf ' '
        ;;
        '.')
            printf '.'
        ;;
        *)
            asci=$(printf %d \'$letter)
            ((asci-=key))
            fwd_letter=$(printf "\\$(printf "%03o" $asci)")
            printf "$fwd_letter"
        ;;
        esac
    done <<< $str
    echo "  \""
    echo
else
    echo
    echo "Errore: i parametri inseriti non sono validi"
    echo "utilizzo previsto dello script: \"sh decifratura.sh <stringa da decifrare> <chiave di decifratura>\""
    echo
    exit 1
fi
