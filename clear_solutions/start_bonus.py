import subprocess
import os

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RESET = "\033[0m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

def main():
    

    # cambiare il nome
    new_folder_path = "../Konzu/"

    # cambiare la repo
    url_repository = "https://github.com/giacominho3/Konzu.git"

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
                print(YELLOW + "inavlid option, aborting" + RESET)
                exit()

    try:
        comando_clone = ["git", "clone", url_repository, new_folder_path]
        subprocess.run(comando_clone, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(CYAN + "Troverai il prossimo livello in " + MAGENTA + new_folder_path + RESET)
    except subprocess.CalledProcessError as e:
        print(RED + "Errore durante il cloning del repository: " + e + RESET)

main()