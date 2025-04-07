import subprocess
import os

# RICORDA DI USARE OPENSSL

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RESET = "\033[0m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

to_check = './practice'
expected = ['MaRViN_stuff']

def check_redirect(url):

    response = request.get(url, allow_redirects=False)

    if response.status_code == 301:
        redirect_url = response.headers.get('Location')
        return redirect_url
    else:
        return url

def clone_repo(url_repository, new_folder_path):

    url_to_clone = check_redirect(url_repository)

    comando_clone = ["git", "clone", url_to_clone, new_folder_path]

    try: 
        subprocess.run(comando_clone, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(GREEN + "Livello completato con successo!" + RESET)
        print("Troverai il prossimo livello in " + MAGENTA + new_folder_path + RESET)
    except subprocess.CalledProcessError as e:
        print(RED + "Errore durante il cloning del repository: " + str(e) + RESET)


def check_ls(cartella, expected):
    try:
        content = set(os.listdir(cartella))
    except OSError as e:
        return False

    expected_set = set(expected)

    if content == expected_set:
        return True
    else:
        return False

def main():
    # cambiare il nome
    new_folder_path = "../DataGrip"

    # cambiare la repo
    url_repository = "https://github.com/TommyJD93/DataGrip.git"
    solution = "55596C51"

    expected = ['hotel_california.txt',
                'hysteria.txt',
                'alien_blues.txt', 
                'brain_stew.txt',]

    if (check_ls('./media/playlists/Rock', expected) == False):
        print("Ho trovato un errore nelle playlist da te create :(")
        exit()

    expected = ['the_real_slim_shady.txt',
                'many_man.txt', 
                'whats_the_difference.txt',
                'all_eyez_on_me.txt',]

    if (check_ls('./media/playlists/Rap', expected) == False):
        print("Ho trovato un errore nelle playlist da te create :(")
        exit()

    expected = ['playlists']

    if (check_ls('./media', expected) == False):
        print("Ho trovato un errore nelle playlist da te create :(")
        exit()

    expected = ['Rock', 'Rap']

    if (check_ls('./media/playlists', expected) == False):
        print("Ho trovato un errore nelle playlist da te create :(")
        exit()

    new_folder_name = "../DataGrip"
    if os.path.isdir(new_folder_name):
        print(CYAN + f"I cannot copy the new exercise in {new_folder_name} since there's another dir/file with the same name" + RESET)

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
                print(YELLOW + "inavlid option, aborting" + RESET)
                exit()

    print(GREEN + "\nHINT: " + "Ricorda l'ordine di inserimento dei caratteri della soluzione :)\n" + RESET)
    mysolution = input("Inserisci la soluzione del livello: " + YELLOW)
    print(RESET)

    if (mysolution == solution):
        clone_repo(url_repository, new_folder_path)
    else:
        print(RED + "La soluzione che hai dato sembra essere errata, ritenta :(" + RESET)
        exit()

main()