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

def check_ls(cartella, expected):
    content = set(os.listdir(cartella))
    expected_set = set(expected)

    if content == expected_set:
        return True
    else:
        return False

def main():

    new_folder_name = "../GeoBot"

    if os.path.isdir(new_folder_name):
        print(CYAN + f"I cannot copy the new exercise in {new_folder_name} since there's another dir/file with the same name" + RESET)
        
        answer = input(MAGENTA + "do you want to remove it? (y/n) [n] " + RESET)
        if answer.lower() == "yes" or answer.lower() == "y":
            remove_dir = ["rm", "-rf", new_folder_name]
            subprocess.run(remove_dir, check=True)
            print(GREEN + "folder removed" + RESET)
        else:
            if answer.lower() == "no" or answer.lower() == "n" or answer.strip() == "":
                print(YELLOW + "please move the folder and run the script again to clone the next exercise" + RESET)
                exit()
            else:
                print(YELLOW + "inavlid option, aborting" + RESET)
                exit()
    try:
        url_repository = "https://github.com/giacominho3/GeoBot.git"

        if (check_ls(to_check, expected)):

            print(GREEN + "Livello completato con successo!" + RESET)

            comando_clone = ["git", "clone", url_repository, new_folder_name]
            try:
                subprocess.run(comando_clone, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                print("Troverai il prossimo livello in " + MAGENTA + new_folder_name + RESET)
                exit()
            except subprocess.CalledProcessError as e:
                print(RED + "Errore durante il cloning del repository: " + e + RESET)
        else:
            print(RED + "Le cartelle in \"practice\" sembrano essere quelle sbagliate, ritenta :(" + RESET)

    except subprocess.CalledProcessError as e:
        print(RED + "Errore durante il cloning del repository: " + str(e) + RESET)


main()

