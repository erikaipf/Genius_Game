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
from print_menu import show_menu, show_info, clean_screen
#from play_sounds import play_sound
from color_text_screen import change_color

#List of Players
players_list = []

def show_info_game():#obj_game):
	# Default 33 lines, 79 columns at screen
	show_info(game_info) #obj_game.game_info)
	
	raw_input("Press <Enter> to go to the Main Menu.")

def create_main_menu():
	'''Create the Text for the Main Menu'''
	menu = ("\n+-----------------------+"+
		 	"\n|  **  Genius Game  **  |"+
		 	"\n+-----------------------+"+
		 	"\n|       Main Menu       |"+
		 	"\n+-----------------------+"+
		 	"\n|  1 - Start Game       |"+
		 	"\n|  2 - Show Scores      |"+
			"\n|  3 - Change Players   |"+
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
		    "\n+-----------------------+" +
		    "\n|  0 - Return           |" +
		    "\n+-----------------------+"
		    ) % (game_level_name(1).ljust(17),
		         game_level_name(2).ljust(17),
		         game_level_name(3).ljust(17))
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
		 	"\n|  3 - Remove Player    |"+
		 	"\n|  4 - Change Name      |"+
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

		try:
			# Show the actual level
			print actual_level()
			# Change the level of the game
			level_choice = int(raw_input("\nType the number of the level you would like to play: "))
		except ValueError:
			# Exception in case of empty choice or invalid number
			print "Invalid option!  Please try again."

		# Verify the user choice
		if level_choice == 0:
			# Stop the loop, go back to Main Menu
			break
		elif level_choice in (1,2,3):
			# Verify if the level is the same
			if game_level == level_choice:
				print "\nYou are already at the selected level!"
				# Message to pause the program for the user to read the message
				raw_input("\nPress <Enter> to select another level.")
			else:
				# Change the user's level
				change_game_level(level_choice)
				# Show the new level
				print "\nLevel changed!\n%s" % (actual_level())
				# Message to pause the program for the user to read the message
				raw_input("\nPress <Enter> to go back to Main Menu.")
				# Stop loop, go back to Main Menu
				break
		else:
			print "\nInvalid level!"
			# Message to pause the program for the user to read the message
			raw_input("\nPress <Enter> to try continue.")

def show_list_players():
	'''Print the actual list of players'''
	global players_list

	# Verify how many players has the list
	if len(players_list) == 0:
		print "\nSorry, the list of players is empty!\nGo to option 3 - Change Players at the Main Menu."
	elif len(players_list) == 1:
		# Clean the screen
		clean_screen()
		print "\nActual player name: %s" % (players_list[0].player_name)
	else:
		# Clean the screen
		clean_screen()
		print "\nList of actual players:"
		# Loop to read the list
		for index in range(len(players_list)):
			print " #%i - %s" % (index + 1, players_list[index].player_name)

def player_name_exist(player_name):
	'''Check if the name already exist'''
	global players_list

	# Verify if the name is empty
	if len(player_name.strip(" ")) > 0 and len(players_list) > 0:
		# Loop to check the list
		for player_obj in players_list:
			# Compare the names
			if player_obj.player_name == player_name:
				return True #player_obj
				# stop the loop
				break

def add_player(player_name):
	'''Add a new player for the game'''
	global players_list

	# Initialize a new player
	new_obj_game = GeniusGame(player_name = player_name)
	
	# Insert the player on the list
	players_list.append(new_obj_game)
	# Confirm the player was added
	return True

def change_game_players():
	'''Change the players of the game'''
	global players_list
	
	players_menu = create_players_menu()

	while True:
		# Show Menu formatted and centralized
		show_menu(players_menu, empty_top_lines = 6, botton_msg_lines = 1)

		try:
			# Save the user's choice in a variable
			menu_option = int(raw_input("Select an option from Players Menu: "))
		except ValueError:
			# Exception in case of empty choice or invalid number
			print "Invalid option! Please try again."

		# Verify the user options
		if menu_option == 0:
			# Option 0 - Return
			# Stop loop and go back to Main Menu
			break
		elif menu_option == 1:
			# Option 1 - Show Players
			show_list_players()
			# Message to pause the program for the user to read the message
			raw_input("\nPress <Enter> to continue.")
		elif menu_option == 2:
			# Option 2 - Add Player
			player_name = raw_input("\nType the name of the New Player or leave empty to use the default name: ")
			
			# Verify if the name is empty
			if player_name.strip(" ") == "":
				# Define the default name
				player_name = "Player " + str(len(players_list)+1)
				# Add a new player with a default name
				if add_player(player_name):
					print "\nNew player %s added!" % (player_name)
					# Message to pause the program for the user to read the message
					raw_input("\nPress <Enter> to continue.")
			else:
				# Check if the name already exist
				if player_name_exist(player_name) == True:
					print "\nThere is already a user called %s.  Please try another name."
				else:
					# Add a new player using the new name
					if add_player(player_name):
						print "\nNew player %s added!" % (player_name)
						# Message to pause the program for the user to read the message
						raw_input("\nPress <Enter> to continue.")
		elif menu_option == 3:
			# Option 3 - Remove Player
			pass
			# show_list_players()
			
			# player_number = int(raw_input("\nType the number of the PlayersPress <Enter> to continue."))

		elif menu_option == 4:
			# Option 4 - Change Name
			# show_list_players()
			# # Message to pause the program for the user to read the message
			# raw_input("\nType the number of the PlayersPress <Enter> to continue.")
			pass
		else:
			print "\nInvalid number! Please try again."

def main():
	global players_list

	# Initialize a new player
	add_player("Player 1")	

	# Change the color of the screen and text
	change_color(62)

	# Print game info
	show_info_game()

	# Create the main menu
	main_menu = create_main_menu()

	# Loop to keep running the code
	while True:
		# Show Menu formatted and centralized
		show_menu(main_menu, empty_top_lines = 6, botton_msg_lines = 1)

		try:
			# Save the user's choice in a variable
			menu_option = int(raw_input("Select an option from Main Menu: "))
		except ValueError:
			# Exception in case of empty choice or invalid number
			print "\nInvalid option! Please try again."

		# Verify the user options
		if menu_option == 0:
			# Option 0 - Exit
			clean_screen()
			print "\nThank you for playing ** Genius Memory Game **!  See you again soon."
			# Message to pause the program for the user to read the message
			raw_input("\nPress <Enter> to finish the game.")
			# Stop loop and finish the program
			break
		elif menu_option == 1:
			# Option 1 - Start Game
			# Verify if more players were add before
			if len(players_list) > 1:
				keep_players = raw_input("\nWould you like to change the players?" +
					                     "\nType  Y  to change or any other key to start the game: ")
				
				if keep_players.lower() == "y":
					change_game_players(players_list)
			else:
				keep_players = raw_input("\nWould you like to add players?" +
					                     "\nType  Y  to add or any other key to start the game: ")
				
				if keep_players.lower() == "y":
					change_game_players(players_list)

			if len(players_list) == 0:
				print "There are no players to start the game!  Please add players choosing the option 3 - Change Players."
				# Message to pause the program for the user to read the message
				raw_input("\nPress <Enter> to continue.")
			else:
				# Loop to start the game for each player
				for player in players_list:
					# Start the game										
					player.play_game()
		elif menu_option == 2:
			# Option 2 - Show Scores
			print "\nIn construction! Come back soon."
		# 	# Show user score
		# 	print "\nYour last score was:", v_game_score
		elif menu_option == 3:
			# Option 3 - Change Players
			change_game_players()
		elif menu_option == 4:
			# Option 4 - Change Level
			menu_change_level()
		else:
			print "\nInvalid number! Please try again."
	
	# Change back to black and white the color of the screen and text before finish the program
	change_color(7)

if __name__ == '__main__':
	main()