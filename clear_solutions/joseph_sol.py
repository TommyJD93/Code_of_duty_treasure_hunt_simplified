import os
import subprocess

# RICORDA DI USARE OPENSSL

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RESET = "\033[0m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

def verify_permissions(file_path, user, group, other):
    try:
        mode = os.stat(file_path).st_mode
    except OSError:
        print(RED + f"Impossibile trovare il file {file_path}" + RESET)
        exit()

    if ((mode >> 6) & 0b111) != user:
        return 1

    if ((mode >> 3) & 0b111) != group:
        return 2

    if (mode & 0b111) != other:
        return 3
    return 0

# check permissions for files inside the data folder, returns 0 if evrything is correct
def check_all():
    var = verify_permissions("data/first_op/1_op_*", 7, 7, 7)
    if var != 0:
        return 1

    var = verify_permissions("data/first_op/2_op_+", 2, 1, 2)
    if var != 0:
        return 2

    var = verify_permissions("data/first_op/3_op_-", 0, 0, 0)
    if var != 0:
        return 3

    var = verify_permissions("data/first_op/4_op_:", 0, 0, 1)
    if var != 0:
        return 4

    var = verify_permissions("data/first_op/5_op_=", 1, 0, 1)
    if var != 0:
        return 5

    #_________________________________________________________________#

    var = verify_permissions("data/second_op/1_op_+", 7, 5, 3)
    if var != 0:
        return 11

    var = verify_permissions("data/second_op/2_op_*", 4, 1, 2)
    if var != 0:
        return 12

    var = verify_permissions("data/second_op/3_op_-", 2, 2, 1)
    if var != 0:
        return 13

    var = verify_permissions("data/second_op/4_op_:", 4, 3, 3)
    if var != 0:
        return 14

    var = verify_permissions("data/second_op/5_op_=", 0, 1, 1)
    if var != 0:
        return 15
    return 0

def main():
    # check that permissions are set correctly in the data fodler
    var = check_all()
    if (var != 0):
        print(RED + "I permessi dei file nella cartella data sembrano essere errati, ritenta :(" + RESET)
        exit(0)

    # cambiare il nome
    new_folder_path = "../BONUS/Loid"

    # cambiare la repo
    url_repository = "https://github.com/TommyJD93/Loid.git"
    solution = "42"

    if os.path.isdir(new_folder_path):
        print(CYAN + f"I cannot copy the new exercise in {new_folder_path} since there's another dir/file with the same name" + RESET)

        answer = input(MAGENTA + "do you want to remove it? (y/n) [n] " + RESET)
        if answer.lower() == "yes" or answer.lower() == "y":
            remove_dir = ["rm", "-rf", new_folder_path]
            subprocess.run(remove_dir, check=True)
            print(GREEN + "folder removed" + RESET)

        else:
            if answer.lower() == "no" or answer.lower() == "n" or answer.strip() == "":
                print(YELLOW + "please move the folder and run the script again to clone the next exercise" + RESET)
                exit()
            else:
                print(YELLOW + "invalid option, aborting" + RESET)
                exit()

    print(GREEN + "\nHINT: verifica l'ordine dei calcoli e delle operazioni o controlla meglio la tabella ascii :)" + "\n" + RESET)
    mysolution = input(MAGENTA + "Inserisci la soluzione: " + YELLOW)
    print(RESET)

    if (mysolution == solution):
        comando_clone = ["git", "clone", url_repository, new_folder_path]
        try:

            if not os.path.isfile(".sol_k"):
                print(GREEN + "La soluzione è corretta!" + RESET)
                print(YELLOW + "Tuttavia prima di passare al prossimo livello devi trovare anche la soluzione di Caesar."+ RESET)
                print(YELLOW + "una volta fatto avvia nuovamente questa solution e inserisci un'altra volta la risposta corretta" + RESET)
                exit()

            print(GREEN + "Livello completato con successo!" + RESET)
            subprocess.run(comando_clone, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print("Troverai il prossimo livello in " + MAGENTA + new_folder_path + RESET)
        except subprocess.CalledProcessError as e:
            print(RED + "Errore durante il cloning del repository: " + str(e) + RESET)
    else:
        print(RED + "La soluzione che mi hai dato sembra non essere quella giusta, ritenta :(" + RESET)
        exit()

main()