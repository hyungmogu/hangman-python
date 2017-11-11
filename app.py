'''
	hangman - requirements analysis

	- In the beginning of the game, it prompts user to enter secret phrase
	- after entering secret phrase, the current screen is cleared, and a gallow and hidden phrase are displayed
	- once the game is setup, it prompts user to enter a guess
	- for each incorrect guess, a body part is added to the gallow and is shown
	- for each correct guess, all matching letters are shown instead of hypens
	- the screen is cleared an updated for every guess
	- the game is lost if all 6 body parts are shown
	- the gane is won if all letters are correctly guessed before all body parts are shown
	- once the game is finished, secret phrase is displayed regardless of the outcome
	- after displaying the secret phrase, it prompts user to play again or not (y|n) 
	- if pressed 'y', then the game repeats from step 1
	- if pressed 'n', the program is exited 

	
	List of Necessary variables to create this game
	-----------------------------------------------

	- var secret_phrase to store secret phrase entered by a user
	- var hidden_phrase to display letters and/or hypens
	- var guess to store guess from a user
	- var response to store user's decision to play game again or not
	- var num_of_lives == 6, to use it for displaying gallow



	step 1
	------

		play_game = True

		while(play_game): 

			initialize game

			play game

			display result

			if(!play again):
				play_game = False 


	step 2
	------

		initialize game
		---------------
			- in the beginning of the pseudocode, user is prompted to enter secret phrase
			- after entering the secret phrase, hidden phrase is generated. It is secret phrase where all letters are replaced with hypens.
			- before displaying hidden phrase and gallow, the current screen is cleared
			- after clearing screen, gallow and hidden phrase are displayed
			- at the end of the pseudoce, the game is setup for user to play


			based on the requirements, the pseudocode can be refined to the following:

			num_of_lives = 6
			secret_phrase = create_secret_phrase()
			hidden_phrase = generate_hidden_phrase(secret_phrase) x
			clear_screen() x
			show_gallow(num_of_lives) x
			show_hidden_phrase(hidden_phrase) x
			

		play game
		---------
			- in the beginning of the pseudocode, user is prompted to enter a guess
			- after entering a guess, guess is compared with secret phrase
			- if user makes a correct guess, all matching letters are shown
			- if user makes an incorrect guess, a body part is added to the gallow, and num_of_lives is decremented 
			- the game repeats until num_of_lives == 0 or hidden_phrase == secret_phrase

			based on the requirement, the pseudocode can be refined to the following

			def play_game(num_of_lives, secret_phrase, hidden_phrase):

				while(game_is_not_over(num_of_lives, hidden_phrase, secret_phrase)):

					guess = make_a_guess() x
					made_correct_guess = compare_guess(guess, secret_phrase) x
					update_game(guess, num_of_lives, hidden_phrase, secret_phrase made_correct_guess) x
					show_gallow(num_of_lives) x
					show_hidden_phrase(hidden_phrase) x


		display result
		--------------
			- in the beginning of the pseudocode, the recentmost gallow is shown
			- after showing the gallow, it displays if the user has won or lost
			- after printing the outcome, it displays the secret phrase


			based on the requirement, the pseudocode can be refined to the following:

			- show gallow
			- print the outcome of the game (won/lost)
			- display secret phrase

			the above pseudocde can be turned into the following python syntax

			def display_result(num_of_lives, hidden_phrase, secret_phrase):
				show_gallow(num_of_lives)
				print_outcome_of_game(hidden_phrase,secret_phrase,num_of_lives)
				print_secret_phrase(secret_phrase)


		play again
		----------
			- in the beginning of the pseudocode, user is prompted to play game again or not
			- at the end of the pseudocode, it returns true if user wants to play again and false if user doesn't want to play again


			based on the requirements, the pseudocode can be refined to the following:

			- prompt user to play game again or not (y|n)
			- if 'y', return true
			- if 'n', return false

			the above pseudocode can be turned into the following python syntax


			def play_again():

				exit_prompt = False
				response = ''

				while(!exit_prompt): 
					response = input("Would you like to play game again? (y|n): ")
					
					if (!(response == 'y' or response == 'n')):
						print("Error: please make sure response is either y or n")
						continue

					exit_prompt = True

				if (response == "y"):
					return True

				elif (response == "n"):
					return False


	step 3
	------		

		initialize_game
		---------------

			create_secret_phrase() 
			----------------------
				- in the beginning of the function, it prompts user to enter the secret phrase
				- if the secret phrase is composed of something other than letters, then error is called and user is prompted to try again
				- at the end of the function, the secret phrase in the form of an array is returned
				- the array includes spaces

				given the requirements, the method can be subdivided into following sub-components

				create_secret_phrase():

					exit_prompt = False
					response = ""

					while(!exit_prompt):
						user_input = input("Enter Secret Phrase: ")
						
						if(!is_valid(user_input)):
							print("Error: Make sure the input is a phrase")
						else:
							exit_prompt = True

				
					return [x for x in user_input]
			
			
			generate_hidden_phrase(secret_phrase)
			-------------------------------------
				- the secret_phrase is an array of letters.
				- the size of array is greater than 1
				- at the end of the method, an array is returned with letters in secret phrase replaced with hypen

				given the requirements, the function can be written as the following


				def generate_hidden_phrase(secret_phrase):

					output = []

					for i in secret_phrase:
						if(i != ' '):						
							output.append('-')		
						else:
							output.append(' ')

					return output


			clear_screen()
			--------------
				- At the end of the function, the current screen on command prompt is cleared



				understanding cases:
				--------------------

				1. the os of the machine where this code is run is window

					1.1 clear screen using command based on window

				2. the os of the machine where this code is run is linux

					2.1 clear screen using command based on linux / mac os


				given the requirement and cases, the function can be written as the following


				import subprocess as sp
				import platform as pltf


				clear_screen()

					if pltf.system() == "Linux" or pltf.system == "Darwin": # if the operating system is Linux or Mac OS
						sp.call("clear", shell = True)

					else: #if the operating system is windows
						sp.call('cls')

				

				Note: the above solutions are referenced from the following sites:
					- https://stackoverflow.com/questions/18937058/clear-screen-in-shell 
					- https://stackoverflow.com/questions/16721940/why-when-use-sys-platform-on-mac-os-it-print-darwin 			



			show_gallow(num_of_lives)
				- at the end of the function, it prints a gallow with different set of body parts based on the nubmer of lives

					- if num lives == 6, no body parts are shown
					- if num_of_lives == 5, head is shown
					- if num_of_lives == 4, head and body are shown
					- if num_of_lives == 3, head, body and left arm are shwon
					- if num_of_lives == 2, head, body, left and right arm are shown
					- if num_of_lives == 1, head, body, left and right arm, and left leg are shown
					- if num_of_lives == 0, all body parts are shown


				given the requirement, the code can be written as the following: 



				show_gallow(num_of_lives):

					gallow = ''

					if (num_of_lives == 6):

                        gallow = r"""   +-----+ 
                                        |     | 
                                        |      
                                        |    
                                        |    
                                        |      
                                        |       
                                     +-----+ """

					elif (num_of_lives == 5):

                        gallow = r"""   +-----+ 
                                        |     | 
                                        |     O 
                                        |     
                                        |    
                                        |      
                                        |       
                                     +-----+ """


					elif (num_of_lives == 4):

                        gallow = r"""   +-----+ 
                                        |     | 
                                        |     O 
                                        |     |
                                        |    
                                        |      
                                        |       
                                     +-----+ """

					elif (num_of_lives == 3):

                        gallow = r"""   +-----+ 
                                        |     | 
                                        |     O 
                                        |    /|
                                        |    
                                        |      
                                        |       
                                     +-----+ """

					elif (num_of_lives == 2):

                        gallow = r"""   +-----+ 
                                        |     | 
                                        |     O 
                                        |    /|\
                                        |    
                                        |      
                                        |       
                                     +-----+ """

					elif (num_of_lives == 1):

                        gallow = r"""   +-----+ 
                                        |     | 
                                        |     O 
                                        |    /|\
                                        |    /
                                        |      
                                        |       
                                     +-----+ """

					elif (num_of_lives == 0): 


                        gallow = r"""   +-----+ 
                                        |     | 
                                        |     O 
                                        |    /|\
                                        |    / \
                                        |      
                                        |       
                                     +-----+ """

					print(gallow)


				Note: the idea of multiline string is referenced from here: 
				  https://stackoverflow.com/questions/10660435/pythonic-way-to-create-a-long-multi-line-string

			show_hidden_phrase(hidden_phrase)
			---------------------------------
				- All elements in hidden_phrase are of string data type
				- At the end of the function, the hidden phrase is displayed on screen


				based on the requirement, the function is defined as the following:

				show_hidden_phrase(hidden_phrase):

					output = ''.join(hidden_phrase)

					print(output)


				Note: the solution to the problem of joining elements in array is referenced from here:
					https://stackoverflow.com/questions/5618878/how-to-convert-list-to-string


			make_a_guess()
			--------------
				- At the end of the function, it returns the letter of guess made by user
				- if the guess is other than a letter, then the software prompts user to type again

				
				Understanding cases:
				--------------------

				1. User registers input other than lower case letters (i.e. integers and special symbols like @)
					
					1.1. Prompt user to type again

				2. User registers input of correct type

					2.1. There are more than one letters

						2.1.1. Prompt user to type again

					2.2. There is only one letter

						2.2.1. return guess

			
				based on the requirement and cases, the function can be defined as the following:


				def make_a_guess():
					
					exit_prompt = False
					guess = ''

					while(!exit_prompt)
						guess = (input("Enter a guess (a-z): ")).strip()

						if (len(guess) != 1):
							print("Error: Please make sure the entered input has only one character.")
							continue

						if (!(ord(guess) >= 97 and ord(guess) <= 122)):
							print("Error: Please make sure the entered input is a lowercase letter (a-z)")
							continue

						exit_prompt = True

					return guess


			compare_guess(guess, secret_phrase)
			-----------------------------------
				- At the end of the function, it returns boolean value
				- If correct guess is made, then the returned value is True 
				- If incorrect guess is made, then the returned value is False
				- A correct guess is made when the value in guess exists in secret phrase
				- An incorrect guess is made when there value in guess doesn't exist in secret phrase



				based on the requirements, the function can be defined as the following:


				def compare_guess(guess, secret_phrase):

					made_correct_guess = False


					for (character in secret_phrase):
						if(character == guess):
							made_correct_guess = True
							break 

					return made_correct_guess


			update_game(guess, num_of_lives, hidden_phrase, made_correct_guess)
			-------------------------------------------------------------------
				- At the end of the function, nothing is returned but values in hidden_phrase and num of lives is updated
				- If made_correct_guess == True, then hypens in hidden_phrase are replaced with the 
				  corresponding values of guess in secret_phrase
				- If made_correct_guess == False, then num_of_lives is decremented

				based on the requirement, the function is defined as the following:


				def update_game(guess, num_of_lives, hidden_phrase, secret_phrase, made_correct_guess):

					if(made_correct_guess):
						i = 0
						n = len(secret_phrase)
						while(i < n):
							if (secret_phrase[i] == guess):
								hidden_phrase[i] = guess
							i++
					else:
						num_of_lives--


			
'''




