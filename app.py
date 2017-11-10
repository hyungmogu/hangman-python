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



	step 1
	------

		play_game = True

		while(play_game): 

			initialize game

			play game

			display result

			if(!play again):
				play_game = False 







'''




