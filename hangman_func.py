import subprocess as sp
import platform as pltf
import re

# def play_game(num_of_lives, secret_phrase, hidden_phrase):

#     while not game_is_over(num_of_lives, hidden_phrase, secret_phrase):

#         guess = make_a_guess()
#         made_correct_guess = compare_guess(guess, secret_phrase)
#         update_hidden_phrase(guess, num_of_lives, hidden_phrase, secret_phrase, made_correct_guess)
#         num_of_lives = update_num_of_lives()
#         clear_screen()
#         show_gallow(num_of_lives)
#         show_hidden_phrase(hidden_phrase)


def display_result(num_of_lives, hidden_phrase, secret_phrase):
    clear_screen()
    show_gallow(num_of_lives)
    print_outcome_of_game(hidden_phrase,secret_phrase,num_of_lives)
    print_secret_phrase(secret_phrase)


def play_again():

    exit_prompt = False
    output = False

    while not exit_prompt:
        response = input("Would you like to play again (y|n): ").strip()
        
        if not (response == 'y' or response == 'n'):
            print("Error: please make sure the registered input is either y or n")
        else:
            exit_prompt = True

    if(response == 'y'):
        output = True

    return output


def create_secret_phrase():

    exit_prompt = False
    response = ""

    while not exit_prompt:
        user_input = (input("Enter secret phrase: ")).strip()
        
        if not is_secret_phrase_valid(user_input):
            print("Error: Make sure the input is a phrase of letters")
        else:
            exit_prompt = True


    return [x.lower() for x in user_input]


def is_secret_phrase_valid(secret_phrase):

    pattern = r"[^a-zA-Z]"
    match = re.match(pattern, secret_phrase)

    if match:
        return False
    else:
        return True

def generate_hidden_phrase(secret_phrase):

    output = []

    for i in secret_phrase:
        if not (i == ' '):                      
            output.append('-')      
        else:
            output.append(' ')

    return output

def clear_screen():

    if pltf.system() == "Linux" or pltf.system == "Darwin": # if the operating system is Linux or Mac OS
        sp.call("clear", shell = True)

    else: #if the operating system is windows
        sp.call('cls')

def show_gallow(num_of_lives):

    gallow = ''

    if num_of_lives == 6:
        
        gallow = r"""   
            +-----+
            |     | 
            |      
            |    
            |    
            |      
            |       
         +-----+ """

    elif num_of_lives == 5:

        gallow = r"""
            +-----+ 
            |     | 
            |     O 
            |     
            |    
            |      
            |       
         +-----+ """


    elif num_of_lives == 4:

        gallow = r"""
            +-----+ 
            |     | 
            |     O 
            |     |
            |    
            |      
            |       
         +-----+ """

    elif num_of_lives == 3:
        gallow = r"""
            +-----+ 
            |     | 
            |     O 
            |    /|
            |    
            |      
            |       
         +-----+ """

    elif num_of_lives == 2:
        gallow = r"""
            +-----+ 
            |     | 
            |     O 
            |    /|\
            |    
            |      
            |       
         +-----+ """

    elif num_of_lives == 1:

        gallow = r"""   
            +-----+ 
            |     | 
            |     O 
            |    /|\
            |    /
            |      
            |       
         +-----+ """

    elif num_of_lives == 0: 


        gallow = r"""   
            +-----+ 
            |     | 
            |     O 
            |    /|\
            |    / \
            |      
            |       
         +-----+ """

    print(gallow)


def show_hidden_phrase(hidden_phrase):

    output = ''.join(hidden_phrase)

    print(output)


def make_a_guess():

    exit_prompt = False
    guess = ''

    while not exit_prompt:
        guess = (input("Enter a guess (a-z): ")).strip()

        if not (len(guess) == 1):
            print("Error: Please make sure the entered input has only one character.")
            continue

        if not (ord(guess) >= 97 and ord(guess) <= 122):
            print("Error: Please make sure the entered input is a lowercase letter (a-z)")
            continue

        exit_prompt = True

    return guess


def compare_guess(guess, secret_phrase):

    made_correct_guess = False

    for character in secret_phrase:
        if character == guess:
            made_correct_guess = True
            break 

    return made_correct_guess

def update_game(guess, num_of_lives, hidden_phrase, secret_phrase, made_correct_guess):

    if made_correct_guess :
        i = 0
        n = len(secret_phrase)
        while i < n:
            if secret_phrase[i] == guess:
                hidden_phrase[i] = guess
            i += 1
    else:
        num_of_lives -= 1

def update_hidden_phrase(made_correct_guess, guess, secret_phrase, hidden_phrase):
    if made_correct_guess :
        i = 0
        n = len(secret_phrase)
        while i < n:
            if secret_phrase[i] == guess:
                hidden_phrase[i] = guess
            i += 1

def update_num_of_lives(made_correct_guess, num_of_lives):

    if not made_correct_guess:

        num_of_lives -= 1

    return num_of_lives


def game_is_over(num_of_lives, hidden_phrase, secret_phrase):

    result = False

    if num_of_lives == 0 or hidden_phrase == secret_phrase:
        result = True

    return result


def play_game_again():

    exit_prompt = False
    output = False

    while not exit_prompt:
        response = input("Would you like to play again (y|n): ").strip()
        
        if not (response == 'y' or response == 'n'):
            print("Error: please make sure the registered input is either y or n")
        else:
            exit_prompt = True

    if response == 'y':
        output = True

    return output
        

def print_outcome_of_game(hidden_phrase,secret_phrase,num_of_lives):

    if num_of_lives == 0:
        print("You lose!")
    else:
        print("You win!")


def print_secret_phrase(secret_phrase):
    print("The secret phrase is: %s" % ''.join(secret_phrase))