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
			hidden_phrase = generate_hidden_phrase(secret_phrase)
			clear_screen()
			show_gallow(num_of_lives)
			show_hidden_phrase(hidden_phrase)
			

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

					guess = make_a_guess()
					result = compare_guess(guess, secret_phrase, hidden_phrase, num_of_lives)
					show_gallow(num_of_lives)
					show_hidden_phrase(hidden_phrase)


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

'''




