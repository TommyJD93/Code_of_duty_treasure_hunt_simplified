# Abstract

This repo is meant as a Manual for the treasure hunt and it's used for testing/developing.
You can find the first level of the hunt in [this repo](https://github.com/giacominho3/MaRViN).

The treasure hunt is divided in levels, the user cannot proceed to the next level before passing the current one.

The cloning of the next levels is automated by the python scripts.

# Level order w/solutions

### mandatory

- 1 MaRViN
- 2 GeoBot
- 3 Botify
- 4 DataGrip
- 5 Caesar

### bonus
- Loid
- Konzu
- San_Pietro_bot
- Octocat

# Mandatory

## MaRViN

user, inside the 'practice' folder, should delete the 'MaRViN_sercrets' dir and create a dir named 'MaRViN_stuff'

final result should look like this

``` 
practice/
    └── MaRViN_stuff/
```

## Geobot
user should search the files in the directory 'continenti/' to find the first part of the hidden word (50 64)

the letters are located in the following dirs

```
.
└── continenti/
    ├── Africa/
    │   ├── Egitto/
    │   │   └── Piramidi_di_Giza.txt (5)
    │   ├── Kenya/
    │   │   └── Kilimangiaro.txt
    │   └── Sudafirca/
    │       └── Table_Mountain.txt
    ├── Americhe/
    │   ├── Brasile/
    │   │   └── Cristo_Redentore.txt
    │   ├── Messico/
    │   │   └── Chichen_Itza.txt
    │   └── USA/
    │       └── Statua_della_Libertà.txt (0)
    ├── Asia/
    │   ├── Giappone/
    │   │   └── Monte_Fuji.txt
    │   ├── India/
    │   │   └── Taj_Mahal.txt
    │   └── Russia/
    │       └── Piazza_Rossa.txt
    ├── Europa/
    │   ├── Francia/
    │   │   └── Torre_Eiffel.txt
    │   ├── Italia/
    │   │   └── Colosseo.txt (6)
    │   └── Spagna/
    │       └── Sagrada_Familia.txt
    └── Oceania/
        ├── Australia/
        │   └── Opera_House.txt (4)
        ├── Nuova Zelanda/
        │   └── Fiordland.txt
        └── Samoa/
            └── To_Sua_Ocean_Trench.txt
```

## Botify

user should search for the second piece of the key inside the lyrics files. Then he should create 3 folders:'Rock', 'Rap', inside the 'playlist' folder to obtain something like this:

``` 
.
└── media/
    └── playlist/
        ├── Rock/
        │   ├── alien_blues.txt
        │   ├── brain_stew.txt
        │   ├── cloud_9.txt
        │   ├── dumb.txt
        │   ├── gumshield.txt
        │   ├── hotel_california.txt
        │   ├── hysteria.txt
        │   └── king_park.txt
        └── Rap/
            ├── all_eyez_on_me.txt
            ├── big_poppa.txt
            ├── fear.txt
            ├── humble.txt
            ├── many_man.txt
            ├── straight_outta_compton.txt
            ├── the_real_slim_shady.txt
            └── whats_the_difference.txt
```

the second piece of the key is hidden in these files

```
.
└── media/
    ├── alien_blues.txt (55)
    ├── all_eyez_on_me.txt
    ├── brain_stew.txt (59)
    ├── hotel_california.txt (6C)
    ├── hysteria.txt 
    ├── many_men.txt(51)
    ├── the_real_slim_shady.txt
    └── whats_the_difference.txt
```

## DataGrip

user should perform 'grep *search_param* *file_to_search*| wc -l' on 'simaris_data1.txt' and 'simaris_data2.txt'. In the first file the user should execute 'grep 2 simaris_data1.txt| wc -l' to find all the lines with the occurrences of the number '2', the output should be 25; In the second file he should execute 'grep connessione simaris_data2.txt | wc -l' to find all the occurrences of the word 'connessione', the output should be 22. At this point the user should subtract the second result to the first one and obtain 3 which is the key to use to decypher the word obtained form the previous 2 exercises. 

## CaesarBot

This exercise is divided in 2 parts.

part 1:
- at this point the user should have 2 'items': the cyphered word (506455596C51) and the key to decypher it (3). To do that he should use the script named 'decifratura.sh', but before doing that he should notice that the word obtained is in hex format, and he should convert it to ascii, to do that he can use the 'hex.py' script. At this point he can use the 'decifratura.sh' script and he should obtain the word 'MaRViN' (with this exact capital letters).

part 2:
- for the second part the user should find another hidden key. 
To do that he will perform some chomod in the files present in the directories 'data/first_op' and 'data/second_op'. In each dir the user will find a file named 'documentazione.sh' he should execute this script to get the permissions to set for each file present in the dir.
Once the user has set all the permissions correctly he should sum the numbers of the permissions of a file (e.g -rw-r--r-- 1_op_* is 6 + 4 + 4 = 14, if it isn't clear yet watch the chmod man page). 
Once he has all the permissions summed up he should perform the operations specified in the name of the file (in the order top to down) using 
the sum of the pemissions of the 'current file' (the file of the operation he is performing) and the sum of permissions of the 'next file' (e.g i have 1_op_* with value 14 and 2_op_+ with value 2, the operation i need to do is 14 * 2, then I will use the result for the sum with the third operation: 14 + 3_op_-, if it isn't clear yet idk what to say...).
<br>
<br>The first operation should be: 
<br>```21 * 5 + 0 - 1 / 2 = 52```
<br>The second operation should be:
<br>```15 + 7 * 5 - 10 / 2 = 50```
<br>
<br>
At this point the user should check the ascii table to find the character associated with the numbers he got from the 2 operation set.
The result should be 52 = 4 and 50 = 2, the final answer is 42.

# Bonus

## Loid

Introduction level, let the user know that there's a bonus part if he want to do it

## Konzu

user should create a bash script that creates a dir named 'Cetus' and then creates and move 10 files 
named: file1, file2, ... file10. The only constraint for this exercise is:
- user must use one or more for cycle/s

The script should look like this:
```bash
mkdir Cetus
pwd=$(pwd)

pwd="$pwd/Cetus"

for i in $(seq 1 10); do
    name="file$i"
    touch $name
    mv $name $pwd
done
```

## San_Pietro_bot

user should create a SSH key to use in the next exercise. Use the following command

```$> ssh-keygen```

## Octocat

user should create a github account, create a new repository, add the ssh key from the prev. exercise to either 
the repo itself or the github account and then push the script made in the exercise "Konzu" onto the repo.

<br>
<br>
<br>

# Other utils

## Python scripts doesn't work?

Here are some steps to understand why a python script doens't work:

<br>
<br>

### 1) Check python version

All these script are developed using Python 3.9.6, make sure that you have installed **at least** this version.

**Note:** always check if an higher version could cause problems

<br>
<br>

### 2) pip3

The scripts should automatically install all the pip3 packages they require, but in case of failure of this installation they won't work.
To check if you have all the packages they require run one of these commands:
```bash
$> pip3 list
$> pip3 show <package_name>
```
The only packages that is required should be pycryptodome (currently using Version: 3.20.0) and requests(currently using Version: 2.31.0).

If you want to make sure that this is the only package required from the script just open up the script and look for this variable
```python
package_name = "pycryptodome"
```

**Note:** the scripts do not install requests since it should be installed by default (at least on 42Rome machines)

<br>
<br>

### 3) Disable warking silencing

Since the scripts could throw some warnings due to SSL versions I've disabled them in each script. If you think that the issue is due to the SSL version just comment this line

```python
warnings.filterwarnings("ignore", category=Warning)
```

### 4) Code obfuscation

The code obfuscation shouldn't cause any problem by default but if you think that this could be the case, you can find all the scripts in the folder 'clear_solutions/'

<br>
<br>

### 5) Open an issue

If you still experiencing issues with the scripts open an issue I will fix it asap

<br>
<br>

# Custom scripts

If you want to make your own custom scripts but you don't know how to automatically install all the required pip3 packages or how to obfuscate the code here is how I did it

## Installations with pip3

```python
import subprocess

def check_installation(package):
    try:
        subprocess.run(["pip3", "show", package], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        return True 
    except subprocess.CalledProcessError:
        return False

package_name = "pycryptodome"

if not check_installation(package_name):
    subprocess.run(["pip3", "install", package_name], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
```

<br>
<br>

## Silencing warnings

```python

import warnings
warnings.filterwarnings("ignore", category=Warning)
```

**Note:** This will silence **ALL** warnings and it's not best practice

<br>
<br>

## Obfuscating the code

To obfuscate the code I've used this simple tool: https://pyobfuscate.com/

<br>
<br>

## Silencing tracebacks

Executing the scripts without wrapping the obfuscated code in a try - execpt block you will end up having some tracebacks if
 the solution is wrong, to avoid that do this

```python

try:
    # obfuscated code goes here
except Exception as e:
    exit()
```

<br>
<br>


# Encryption Steps for the Key: "MaRViN"

MaRViN = 50 64 55 59 6C 51

clear key: MaRViN --caesar(3)--> PdUYlQ --hex--> 50 64 55 59 6C 51

## first part of the key (GeoBot)

Ma = 50 64

## seconda parte della chiave (contenuta in botify)

RVIN = 55 59 6C 51

## chiave di decriptazione (contenuta in DataGirp)

key = 10 

## seconda chiave (contenuta in joseph/Rw{mpx)

key = 42

## commands for joseph permissions

### first_op
```bash
chmod 777 1_op_*
chmod 212 2_op_+
chmod 000 3_op_-
chmod 001 4_op_:
chmod 101 5_op_=
```
### second_op
```bash
chmod 753 1_op_+
chmod 412 2_op_\*
chmod 221 3_op_-
chmod 433 4_op_: 
chmod 011 5_op_= 
```
# CMD list
```bash 
$> cd
$> ls -la
$> rm -rf
$> pwd
$> touch
$> vim
$> mkdir
$> cat -e
$> chmod -XXX
$> grep
$> wc -l
$> ssh-keygen
$> git init
$> git add
$> git commit
$> git push 
```
<br>
<br>
<br>
<br>

# Random stuff for the development

<br>
<br>

# TODO
- reworking solutions to make so that the user is asked if he wants to delete or remove manually a folder or file that has the same name of the repo that has to be cloned, done for now:
- botify
- geobot
- joseph
- konzu
- marvin
- san_pietro
- loid

- noted a typo in te new cloning verification, look for this line "print(YELLOW + "inavlid option, aborting" + RESET)"

<br>
<br>

# Flow

1. geobot, darà la prima parte di una chiave cifrata
2. Botify, darà la seconda parte di una chiave cifrata
3. Simaris, darà la chiave di cifratura
4. Cesar, chiede di creare un file con il nome cifrato, la chiave per questa cifratura andrà trovata all'interno dello script del bot stesso. All'interno del file creato andrà messa la chiave decifrata ottenuta dai primi 3 livelli.
5. Dopo la decifratura della chiave Caeasar reindirizzerà verso il suo assitente che darà la seconda parte della chiave per il lab., la chiave sarà cifrata sempre con il cifrario di cesare. 
note: non mi ricordo se questa cosa effettivamente è così "La chiave di decriptazione sarà nascosta all'interno dello script di Caesar."
6. idk_bot, La frase così ottenuta potrebbe essere usata per risolvere un altro livello riguardante chmod
