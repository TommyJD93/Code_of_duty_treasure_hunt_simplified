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

def is_directory_empty(directory):
    # Check if the directory is empty
    return not os.listdir(directory)

def check_script(directory, files):
    files = directory + "/" +files

    if os.path.isfile(files) == False :
        print(RED + "file does not exist" + RESET)
        exit()

    if os.path.isdir("Cetus") :
        subprocess.run(['bash', '-c', 'rm -r Cetus'])

    dir_name = "verify_folder"
    os.makedirs(dir_name, exist_ok=True)

    # Creazione dei file all'interno della directory
    for i in range(1, 11):
        file_name = f"file{i}"
        file_path = os.path.join(dir_name, file_name)
        with open(file_path, 'w') as file:
            pass

    subprocess.run(['bash', files], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    out = subprocess.run(['bash', '-c', 'diff Cetus/ verify_folder/'], capture_output=True)

    if os.path.isdir("verify_folder") :
        subprocess.run(['bash', '-c', 'rm -r verify_folder'])

    if os.path.isdir("Cetus") :
        subprocess.run(['bash', '-c', 'rm -r Cetus'])

    if out.returncode == 0 :
        print(GREEN + "Found and verified the script, GJ :D" + RESET)
        return True
    return False
    
def check_presence_of_script(directory):
    dir_list = os.listdir(directory)
    script_files = [file for file in dir_list if file.endswith(".sh")]
    check = False

    if script_files:
        for files in script_files :
            if check_script(directory, files) == True:
                check = True
                break
    else:
        print(RED + "Non sono stati trovati script all'interno della repo :/" + RESET)
        print(YELLOW + "NOTA: lo script deve trovarsi all'interno della root della tua repo!")
        return False

    return check

def main():
    #cambiare il nome
   
    # https://github.com/TommyJD93/Notes.git
    url_repository = input(MAGENTA + "Inserisci l'URL della tua repo: " + YELLOW)
    cloned_folder = os.path.basename(url_repository.split('/')[-1].split('.')[0])
    print(RESET)

    if os.path.isdir(cloned_folder):
        subprocess.run(['bash', '-c', 'rm -rf ' + cloned_folder])

    comando_clone = ["git", "clone", url_repository]
    rm_dir = ["rm", "-fr", cloned_folder]

    try:
        subprocess.run(comando_clone, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        if os.path.exists(cloned_folder) and os.listdir(cloned_folder):

            if check_presence_of_script(cloned_folder) == False:
                print(RED + "Script didn't match the expected result :I" + RESET)
                subprocess.run(['bash', '-c', 'rm -rf ' + cloned_folder])
                exit()

        else:
            print(RED + "La cartella clonata è vuota o non esiste." + RESET)
            exit()
        
        print(GREEN + "Livello completato con successo!" + RESET)
        subprocess.run(['bash', '-c', 'rm -rf ' + cloned_folder])

    except subprocess.CalledProcessError as e:
        print(RED + "Errore durante il cloning del repository: " + str(e) + RESET)
        exit()

main()