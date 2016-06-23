'''
Final project Hackbright Academy - by Erika Freiha - 2016
Version 1

Genius Memory Game Manager

Info about the game: https://en.wikipedia.org/wiki/Simon_(game)
'''
# Import modules
#import random

# Import personal modules
from genius_game_class import*
from print_menu import show_menu, show_info, clean_screen, show_pause_message
from play_sounds import play_sound
from color_text_screen import change_color
from random import randint

# List of Players
players_list = []
scores_list = []


def show_colored_game_name():
	# Print Game Name in diferent colors
	# Variable to change the colors of the letters
	color_number = randint(1, 4) #1
	# Count how many blank spaces to centralize the Game Name
	spaces_between_text = ( (79 - len(game_name)) /5)
	# Print the spaces before the Game Name
	print (" " * spaces_between_text) ,

	# Loop for take the letters
	for game_letter in game_name:
		if game_letter == " ":
			# Change to the color of the game
			change_color(game_color)
		else:
			# Change to the color number
			change_color(sound_color[color_number])
		# Print the colored letter
		print game_letter + " " ,
		# Change the color number for the next letter
		if color_number == 4:
			color_number = 1
		else:
			color_number += 1
	# Change back the color of the game
	change_color(game_color)
	# Print the spaces after the Game Name
	print "\n"


def show_info_game(play_sound = False):
	# Default 33 lines, 79 columns at screen
	# # show the game info
	# show_info(game_info, pause_screen = False)
	
	# # Verify if needs to play the sounds
	# if play_sound:
	# 	# Play the sounds
	# 	try:
	# 		for loop_number in range(40):
	# 			sound_number = randint(1, 4)
	# 			# Play the sound and show the colored number
	# 			play_sound_color(sound_number, game_color, sound_color[sound_number], 1000)
	# 	except KeyboardInterrupt:
	# 		pass
	# else:
	# 	# Show pause message to pause the screen
	# 	show_pause_message()
	# show the game info

	# new version
	# Print name in colors
	# Convert the game info in a list of lines
	list_game_info = game_info.split("\n")
	
	# Count how many lines between all text
	lines_between = ( (39 - len(list_game_info) -13) /2)
	
	# Print lines before info
	print ("\n" * lines_between)

	# Print the Game Name in different colors
	show_colored_game_name()

	# Print the game info centralized
	for line_info in list_game_info:
		print line_info.center(79)

	# Print the Game Name in different colors
	print "\n"
	show_colored_game_name()

	# Print lines after info
	print ("\n" * lines_between)
	
	# Verify if needs to play the sounds
	if play_sound:
		# Play the sounds
		try:
			for loop_number in range(40):
				sound_number = randint(1, 4)
				# Play the sound and show the colored number
				play_sound_color(sound_number, game_color, sound_color[sound_number], 1000)
		except KeyboardInterrupt:
			pass
	else:
		# Show pause message to pause the screen
		show_pause_message()


def show_bye_game():
	# Option 0 - Exit
	# Print lines before info
	print ("\n" * 10)

	# Print the Game Name in different colors
	show_colored_game_name()

	print "\n"
	print "Thank you for playing!".center(79)
	print "\n"
	print "See you again soon.".center(79)
	
	# Print the Game Name in different colors
	print "\n"
	show_colored_game_name()

	# Print lines after info
	print ("\n" * 8)


def create_main_menu():
	'''Create the Text for the Main Menu'''
	menu = ("\n+-----------------------+"+
		 	"\n|  **  Genius Game  **  |"+
		 	"\n+-----------------------+"+
		 	"\n|       Main Menu       |"+
		 	"\n+-----------------------+"+
		 	"\n|  1 - Start Game       |"+
		 	"\n|  2 - Show Game Info   |"+
			#"\n|  2 - Show Scores      |"+
			"\n|  3 - Config Players   |"+
		 	"\n|  4 - Change Level     |"+
		 	"\n+-----------------------+"+
		 	"\n|  0 - Exit             |"+
		 	"\n+-----------------------+")
	return menu


def create_level_menu():
	'''Create the Text for the Level Menu'''
	menu = ("\n+-----------------------+" +
		    "\n|  **  Genius Game  **  |" +
		    "\n+-----------------------+" +
		    "\n|     Level Options     |" +
		    "\n+-----------------------+" +
		    "\n|  1 - %s|" +
		    "\n|  2 - %s|" +
		    "\n|  3 - %s|" +
		    "\n|  4 - %s|" +
		    "\n+-----------------------+" +
		    "\n|  0 - Return           |" +
		    "\n+-----------------------+"
		    ) % (game_level_name(1).ljust(17),
		         game_level_name(2).ljust(17),
		         game_level_name(3).ljust(17),
		         game_level_name(4).ljust(17))
	return menu


def create_players_menu():
	'''Create the Text for the Players Menu'''
	menu = ("\n+-----------------------+"+
		 	"\n|  **  Genius Game  **  |"+
		 	"\n+-----------------------+"+
		 	"\n|     Players  Menu     |"+
		 	"\n+-----------------------+"+
		 	"\n|  1 - Show Players     |"+
		 	"\n|  2 - Add Player       |"+
		 	"\n|  3 - Change Name      |"+
		 	"\n|  4 - Remove Player    |"+
		 	"\n+-----------------------+"+
		 	"\n|  0 - Return           |"+
		 	"\n+-----------------------+")
	return menu


def menu_change_level():
	# Create the change level menu
	level_menu = create_level_menu()

	# Loop to keep showing the menu
	while True:
		# Show the level menu formatted and centralized
		# The Level Menu prints 3 lines after, so 31 lines at screen - 3 message lines = 28
		show_menu(level_menu, empty_top_lines = 6, botton_msg_lines = 4)
		# Level Options:
		# 1 - Beginner
		# 2 - Intermediate
		# 3 - Advanced
		# 4 - Challenge

		try:
			# Show the actual level
			print actual_level()
			# Change the level of the game
			level_choice = int(raw_input("\nType the number of the level you would like to play: "))
		except Exception:
			# Exception in case of empty choice or invalid number
			level_choice = None

		# Verify the user choice
		if level_choice == 0:
			# Stop the loop, go back to Main Menu
			break
		elif level_choice in (1,2,3,4):
			# Verify if the level is the same
			if actual_level_number() == level_choice:
				show_pause_message("You are already at this level!",
					           	   "Press <Enter> to select another level.")
			else:
				# Change the user's level
				change_game_level(level_choice)
				# Show the new level
				show_pause_message("Level changed!  %s" % (actual_level()),
				                   "Press <Enter> to go back to Main Menu.")
				# Stop loop, go back to Main Menu
				break
		else:
			show_pause_message("Invalid level!  Please try again.")


def show_list_players(pause_screen):
	'''Print the actual list of players'''
	# TO DO:  In case of bigger names, limit the size of number or change the way to print
	# Count how many players are in the list
	num_players = len(players_list)
	
	# Verify how many players has the list
	if num_players == 0:
		# Initialize a new player
		add_player("Player 1")	
		
		# Count again how many players are in the list
		num_players = len(players_list)
	
	# Verify how many players has the list
	if num_players == 1:
		# Show the info with a pause
		show_info("Actual player name is %s" % (players_list[0].player_name),
				  pause_screen = pause_screen)
	elif num_players > 1:
		# Create the string with the list of players
		players_info = "\nList of actual players:"
		count_title = len(players_info)
		# Loop to read the list
		for index in range(num_players):
			players_info += "\n" + (" #" + str(index+1) + " - " + players_list[index].player_name).ljust(count_title)

		# Show the info with a pause
		show_info(players_info, pause_screen = pause_screen)
	else:
		show_pause_message("Invalid number of players!  Please try again.")


def player_name_exist(player_name):
	'''Check if the name already exist'''
	# Verify if the name is empty
	if len(player_name.strip(" ")) > 0 and len(players_list) > 0:
		# Loop to check the list
		for player_obj in players_list:
			# Compare the names
			if player_obj.player_name.lower()  == player_name.lower() :
				return True #player_obj
				# stop the loop
				break


def add_player(player_name):
	'''Add a new player for the game'''
	# Initialize a new player
	new_obj_game = GeniusGame(player_name = player_name.title())
	
	# Insert the player on the list
	players_list.append(new_obj_game)
	# Confirm the player was added
	return True


def change_player_name(list_player_number):
	new_name = raw_input("\nEnter the new name for " + 
						 players_list[list_player_number].player_name +
						 " or blank to cancel change: ")
	
	# Check if the name already exist
	if len(new_name.strip(" ")) > 0:
		if player_name_exist(new_name) == True:
			# Show a pause message
			show_pause_message("There is already a player called " + 
				               players_list[list_player_number].player_name +
				               ".  Please try another name.")
		else:
			# Change player name
			players_list[list_player_number].player_name = new_name.title()

			# Print the list of players
			show_list_players(False)

			# Show a pause message
			show_pause_message("Player name changed!  Press <Enter> to continue.")


def change_game_players():
	'''Change the players of the game'''
	players_menu = create_players_menu()

	while True:
		# Show Menu formatted and centralized
		show_menu(players_menu, empty_top_lines = 6, botton_msg_lines = 1)

		try:
			# Save the user's choice in a variable
			menu_option = int(raw_input("Select an option and press <Enter>: "))
		except Exception:
			# Exception in case of empty choice or invalid number
			menu_option = None

		# Verify the user options
		if menu_option == 0:
			# Option 0 - Return
			# Stop loop and go back to Main Menu
			break
		elif menu_option == 1:
			# Option 1 - Show Players
			show_list_players(True)
		elif menu_option == 2:
			# Option 2 - Add Player
			player_name = raw_input("\nType the name of the New Player,\nor leave empty to use a default name: ")
			
			# Verify if the name is empty
			if player_name.strip(" ") == "":
				# Define the default name
				player_name = "Player " + str(len(players_list)+1)
				# Add a new player with a default name
				if add_player(player_name):
					# Show a pause message
					show_pause_message("New player %s added!" % (player_name))
			else:
				# Check if the name already exist
				if player_name_exist(player_name) == True:
					# Show a pause message
					show_pause_message("There is already a player called %s.  Please try another name." % (player_name))
				else:
					# Add a new player using the new name
					if add_player(player_name):
						# Show a pause message
						show_pause_message("New player %s added!" % (player_name))
		elif menu_option == 3:
			# Option 3 - Change Name
			# Verify if exist more than 1 player
			if len(players_list) == 1:
				# Change the player's name
				change_player_name(0)
			else:
				# Print the list of players
				show_list_players(False)
				
				try:
					player_number = int(raw_input("\nEnter the player number you want to change the Name: "))

					# Verify if the player number is valid
					if 0 < player_number <= len(players_list):
						# Change the player's name
						change_player_name(player_number-1)
					else:
						# Show a pause message
						show_pause_message("Invalid player number!  Please try again.")
				except Exception:
					# Exception in case of empty choice or invalid number
					player_number = None
		elif menu_option == 4:
			# Option 4 - Remove Player
			# Verify if exist more than 1 player
			if len(players_list) > 1:
				# Print the list of players
				show_list_players(False)

				try:
					player_number = int(raw_input("\nEnter the player number you want to remove: "))

					# Verify if the player number is valid
					if 0 < player_number <= len(players_list):
						confirm_remove = raw_input("\nDo you really want to remove " + 
							                       players_list[player_number-1].player_name + "? " +
												   "\nEnter  Y  for yes or any other key to cancel: ")

						if confirm_remove.lower() == "y":
							players_list.pop(player_number-1)
							# Print the list of players
							show_list_players(False)
							
							# Show a pause message
							show_pause_message("Player removed!  Press <Enter> to continue.")
					else:
						# Show a pause message
						show_pause_message("Invalid player number!  Please try again.")
				except Exception:
					# Exception in case of empty choice or invalid number
					player_number = None
			else:
				# Show a pause message
				show_pause_message("Sorry, no extra players to remove.")			
		else:
			# Show a pause message
			show_pause_message("Invalid option! Please try again.")


def main():
	# Initialize a new player
	add_player("Player 1")

	# Change the color of the screen and text
	change_color(game_color)

	# Print game info
	show_info_game(True)

	# Create the main menu
	main_menu = create_main_menu()

	# Loop to keep running the code
	while True:
		# Show Menu formatted and centralized
		show_menu(main_menu, empty_top_lines = 6, botton_msg_lines = 1)

		try:
			# Save the user's choice in a variable
			menu_option = int(raw_input("Select an option and press <Enter>: "))

		except Exception:
			# Exception in case of empty choice or invalid number
			menu_option = None

		# Verify the user options
		if menu_option == 0:
			# Option 0 - Exit
			show_bye_game()

			# Show pause message to pause the screen
			show_pause_message("Press <Enter> to finish the game.")

			# Stop the game
 			break
		elif menu_option == 1:
			# Option 1 - Start Game
			if len(players_list) == 0:
				# No players on the list
				# Add a player
				add_player("Player 1")
				# Verify again if the list has a player
				if len(players_list) > 0:
					# Start the game
					players_list[0].play_game()
				else:
					# Show a pause message
					show_pause_message("There are no players to start the game!" +
						               "\nPlease add players choosing the option 3 - Change Players.")
			else:
				# Loop to start the game for each player
				for player in players_list:
					# Start the game
					player.play_game()
		elif menu_option == 2:
			# Option 2 - Show Game Info
			show_info_game()
		elif menu_option == 3:
			# Option 3 - Change Players
			change_game_players()
		elif menu_option == 4:
			# Option 4 - Change Level
			menu_change_level()
		else:
			# Show a pause message
			show_pause_message("Invalid option! Please try again.")
	
	# Change back to black and white the color of the screen and text before finish the program
	change_color(terminal_color)


if __name__ == '__main__':
	main()