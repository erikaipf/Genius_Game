'''
Final project Hackbright Academy - by Erika Freiha - 2016
Beta Version

** Genius Memory Game **

The game has four colored numbers, each producing a particular tone when it is used.
A round in the game consists of showing one or more numbers in a random order,
after which the player must reproduce that order by typing the numbers and pressing <Enter>.
As the game progresses, the number of numbers to be typed increases.

More info: https://en.wikipedia.org/wiki/Simon_(game)
'''
# Import functions
import winsound
import random
#import os

# Global variables
g_game_level = 1

# Function to play the sound
def play_sound(p_sound_number, p_sound_time = 1300):
	# The frequency of the sound is 37 thru 32767
	# Print the sound number (comma prints the sound in the same line)
	print p_sound_number,
	
	# Verify the number of the sound to play
	if p_sound_number == 1:
		# Play the sound
		winsound.Beep(390, p_sound_time)
	elif p_sound_number == 2:
		# Play the sound
		winsound.Beep(440, p_sound_time)
	elif p_sound_number == 3:
		# Play the sound
		winsound.Beep(500, p_sound_time)
	elif p_sound_number == 4:
		# Play the sound
		winsound.Beep(600, p_sound_time)

def clear_screen():
	#try:
	#	import os
	#	v_lines = os.get_terminal_size().lines
	#except AttributeError:
	#	v_lines = 130
	v_lines = 31
	print("\n" * v_lines)

def show_info_game():
	# Actual size of my prompt terminal is 33 lines and 80 columns
	v_total_columns = 79
	#v_total_lines = 33
	print "\n" * 10
	print "Welcome to  ** Genius Game **".center(v_total_columns)
	print "\n" * 2
	print "This game is a puzzle game that requires you to use your mind.".center(v_total_columns)
	print "\n"
	print "You have to follow the computer's sequence order.".center(v_total_columns)
	print "\n" * 2
	print "Good Luck!".center(v_total_columns)
	print "\n" * 8
	
	raw_input("Press <Enter> to go to the Main Menu.")

def return_level_name(p_game_level):
	# Show the name of the level
	if p_game_level == 1:
		return "Beginner"
	elif p_game_level == 2:
		return "Intermediate"
	elif p_game_level == 3:
		return "Advanced"

def show_level(p_game_level):
	# Show the level
	if p_game_level in (1,2,3):
		print "\nYou are at Level %i - %s" % (p_game_level, return_level_name(p_game_level))
	else:
		print "\nSome problem with your level!  Please try to change."

def show_level_menu():
	'''Show the level menu formatted'''
	print """
		     +-----------------------+
		     |  **  Genius Game  **  |
		     +-----------------------+
		     |     Level Options     |
		     +-----------------------+
		     |  1 - %s|
		     |  2 - %s|
		     |  3 - %s|
		     +-----------------------+
		     |  0 - Return           |
		     +-----------------------+
		  """ % (return_level_name(1).ljust(17), return_level_name(2).ljust(17), return_level_name(3).ljust(17))

def menu_change_level():
	global g_game_level

	while True:
		# Show the level menu formatted
		show_level_menu()
		# Level Options:
		# 1 - Beginner
		# 2 - Intermediate
		# 3 - Advanced

		try:
			# Change the level of the game
			v_user_level = int(raw_input("\nType the number of the level you would like to play: "))

			# Verify the user choice
			if v_user_level == 0:
				# Stop the loop
				break
			elif v_user_level in (1,2,3):
				# Change the user's level
				g_game_level = v_user_level
				print "\nLevel changed!  Good luck!"
				# Show the new level
				show_level(g_game_level)
				break
			else:
				print "\nInvalid level!  Please try again."
		except ValueError:
			# Exception in case of empty choice or invalid number
			print "Invalid option!  Please try again."

def play_game(p_game_level = 1):
	# Function to play the game
	# Set the time to play the sound
	if p_game_level == 2:
		v_sound_time = 1000
	elif p_game_level == 3:
		v_sound_time = 700
	else: # for level 1 or others > 3
		v_sound_time = 1300
	
	# Initialize the user score
	v_game_score = 0
	# Initialize the lists of sounds
	l_sequence_sounds = []
	l_user_sequence   = []
	# Initialize the validation of the sequence
	v_valid_sequence = True
	
	# Show the new level
	show_level(p_game_level)

	raw_input("\nRepeat the sequence of numbers that is showing!  Are you ready?\nPress <Enter> to begin the game.")

	while v_valid_sequence:
		# Get a random number
		v_sound_number = random.randint(1, 4)
		# Add the number to the game sequence
		l_sequence_sounds.append(v_sound_number)
		print "\nSequence:",
		# Loop to play all the sounds
		for i in range(len(l_sequence_sounds)):
			# Play sound (p_sound_number, p_sound_time)
			play_sound(l_sequence_sounds[i], v_sound_time)

		# Clear the screen to hide the sequence
		clear_screen()
		# Clean user sequence list
		l_user_sequence = []
		# Print a new line
		v_user_sequence = raw_input("\nRepeat the sequence of numbers: ")
		# Test if user sequence is right
		if len(v_user_sequence) < 1:
			# Change the validation
			v_valid_sequence = False
			# Print the message
			print "\nEmpty sequence!\nGAME OVER!"
		else:
			try:
				# Verify if the user typed space between the numbers
				if " " in v_user_sequence:
					# Convert the sequence to a list with spaces
					l_user_sequence = [int(i) for i in v_user_sequence.split()]	
				else:
					# Convert the sequence to a list without spaces
					for v_seq in v_user_sequence:
						l_user_sequence = l_user_sequence + [int(v_seq)]
			except ValueError:
				# Exception in case of invalid number
				# Change the validation
				v_valid_sequence = False
				# Print the message
				print "\nInvalid number on the sequence (%s)!\nGAME OVER!" %(v_seq)	
			
			# Verify if the sequence still valid
			if v_valid_sequence:
				# Verify if the user typed the same quantity of sounds
				if len(l_user_sequence) > len(l_sequence_sounds):
					# Change the validation
					v_valid_sequence = False
					# Print the message
					print "\nWrong sequence!  Sequence typed is bigger than the correct sequence."
					print "User sequence:", l_user_sequence
					print "Game sequence:", l_sequence_sounds, "\nGAME OVER!"
				elif len(l_user_sequence) < len(l_sequence_sounds):
					# Change the validation
					v_valid_sequence = False
					# Print the message
					print "\nWrong sequence!  Sequence typed is smaller than the correct sequence."
					print "User sequence:", l_user_sequence
					print "Game sequence:", l_sequence_sounds, "\nGAME OVER!"
				else:
					# Verify if the sequence is the same
					if l_user_sequence == l_sequence_sounds:
						# Right sequence
						# Increment the score
						v_game_score = v_game_score + 1
						# Print the message
						print "\nGood memory!  Let's add one more number."
					else:
						# Change the validation
						v_valid_sequence = False
						# Print the message
						print "\nWrong sequence!"
						print "User sequence:", l_user_sequence
						print "Game sequence:", l_sequence_sounds, "\nGAME OVER!"
					# old code	
					# # Start the index number
					# v_index_number = 0
					# # Loop to check the user sequence
					# for v_seq_number in l_user_sequence:
					# 	# Verify if is a valid number
					# 	if v_seq_number in ["1","2","3","4"]:
					# 		# Validate the sequence number
					# 		if l_sequence_sounds[v_index_number] == int(v_seq_number):
					# 			# Increment the index
					# 			v_index_number = v_index_number + 1
					# 		else:
					# 			# Change the validation
					# 			v_valid_sequence = False
					# 			# Print the message
					# 			print "\nWrong sequence!"
					# 			print " User sequence: [",
					# 			for i in v_user_sequence:
					# 				print i + ",",
					# 			print "]\n Game sequence:", l_sequence_sounds, "\nGAME OVER!"
								
					# 			# Exit of the loop
					# 			break
					# 	else:
					# 		# Change the validation
					# 		v_valid_sequence = False
					# 		print "\nInvalid number (%s) on the sequence!\nGAME OVER!" % (j)
					# 		# Exit of the loop
					# 		break
					#
					#if v_valid_sequence:
					#	v_game_score = v_game_score + 1
	
	if v_game_score > 0:
		# Show user score
		print "\nThe max number sequence you memorized was:", v_game_score

def main():
	# Clear the screen
	#clear_screen()
	
	# Print game info
	show_info_game()
	
	# Loop to keep running the code
	while True:
		# Menu
		print """
			  "+-----------------------+
			  "|  **  Genius Game  **  |"
			  "+-----------------------+"
			  "|       Main Menu       |"
			  "+-----------------------+"
			  "|  1 - Start Game       |"
			  "|  2 - Change Level     |"
			  "|                       |"
			  "+-----------------------+"
			  "|  0 - Exit             |"
			  "+-----------------------+"
			  \n\n\n"""
			  #"|  2 - Show Score       |"
		try:
			# Save the user's choice in a variable
			v_menu_option = int(raw_input("Select one option: "))
		except ValueError:
			# Exception in case of empty choice or invalid number
			v_menu_option = None

		# Verify the user options
		if v_menu_option == 1:
			# Option 1 - Start Game
			play_game(g_game_level)
		elif v_menu_option == 2:
			# Option 2 - Change Level
			menu_change_level()
		# elif v_menu_option == 2:
		# 	# Option 2 - Show Score
		# 	# Show user score
		# 	print "\nYour last score was:", v_game_score
		elif v_menu_option == 0:
			# Option 0 - Exit
			# Stop loop and finish the program
			break
		else:
			print "Invalid option! Please try again."

if __name__ == '__main__':
	main()