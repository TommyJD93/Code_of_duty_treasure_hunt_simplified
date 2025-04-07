import os
import subprocess
import paramiko
from paramiko import RSAKey
from base64 import decodebytes

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RESET = "\033[0m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

def check_key_validity(key_path):
    try:
        key_path = os.path.expanduser(key_path)
        key= RSAKey.from_private_key_file(key_path)
        paramiko.RSAKey(data=key.asbytes())
        return True
    except (IOError, paramiko.SSHException) as e:
        return False

def main():

    new_folder_path = "../Octocat"

    path = os.path.expanduser("~/.ssh/id_rsa.pub")
 
    if not os.path.isfile(path) :
        print(RED + f"il file {path} non esiste" + RESET)
        exit()

    path = os.path.expanduser("~/.ssh/id_rsa")

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

    if check_key_validity(path):
        print(GREEN + "chiave valida" + RESET)

        new_folder_path = "../Octocat/"

        url_repository = "https://github.com/TommyJD93/Octocat.git"
        try:
            comando_clone = ["git", "clone", url_repository, new_folder_path]
            subprocess.run(comando_clone, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(GREEN + "Livello completato con successo!" + RESET)
            print("Troverai il prossimo livello in " + MAGENTA + new_folder_path + RESET)

        except subprocess.CalledProcessError as e:
            print(RED + "Errore durante il cloning del repository: " + e + RESET)

    else:
        print(RED + "chiave non valida" + RESET)
        exit()

if __name__ == "__main__":
    main()