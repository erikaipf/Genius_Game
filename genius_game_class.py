'''
Final project Hackbright Academy - by Erika Freiha - 2016
Version 1

** Genius Memory Game **

The game has four colored numbers, each producing a particular tone when it is used.
A round in the game consists of showing one or more numbers in a random order,
after which the player must reproduce that order by typing the numbers and pressing <Enter>.
As the game progresses, the number of numbers to be typed increases.

More info: https://en.wikipedia.org/wiki/Simon_(game)
'''
# Import modules
import random
# Import personal modules
from play_sounds import play_sound
from print_menu import clean_screen
from color_text_screen import change_color

# Initialize the variables
game_level = 1
correct_msg_list = ["Good memory", "Good job", "You are doing great", "Awesome", "Congratulations", "Tree cheers for"]
game_info = ("** Genius Memory Game **" +
			 "\n\n\nLet's use your mind?" +
			 "\n\nThe game has four colored numbers, each producing a particular tone." +
			 "\nA round in the game consists of showing one or more numbers in a random order," +
	         "\nafter which the player must reproduce that order by typing the numbers" +
	         "\nand pressing <Enter>." +
	         "\nAs the game progresses, the number of numbers to be typed increases." +
	         "\n\nGood Luck!")

def correct_seq_message():
	global correct_msg_list

	if len(correct_msg_list) > 0:
		return random.choice(correct_msg_list)
	else:
		return "Congratulations"

def game_level_name(game_level):
	# Return the name of the level
	if game_level == 1:
		return "Beginner"
	elif game_level == 2:
		return "Intermediate"
	elif game_level == 3:
		return "Advanced"

def game_sound_time(game_level):
	# Search the time to play the sound for each level
	if game_level == 2:
		sound_time = 1000
	elif game_level == 3:
		sound_time = 700
	else: # for level 1 or others > 3
		sound_time = 1300

	# Return the sound time
	return sound_time

def change_game_level(new_level):
	global game_level

	# Verify if the new level is valid
	if new_level in (1,2,3):
		game_level = new_level
	else:
		print "\nInvalid new Level!  Please try again."

def actual_level_name():
	# Return the name of the actual level of the game
	global game_level

	if game_level in (1,2,3):
		return game_level_name(game_level)
	else:
		return "Invalid Level!"
	
def actual_level():
	# Return the actual level of the game
	global game_level
	
	if game_level in (1,2,3):
		return "\nYou are at Level %i - %s." % (game_level, game_level_name(game_level))
	else:
		return "\nInvalid Level!"

class GeniusGame(object):
	def __init__(self, player_name = "Player 1", game_color = 62):
		self.player_name = player_name
		#self.game_level = game_level
		#self.sound_time = game_sound_time(game_level)
		self.game_score = 0
		self.game_color = game_color
		self.screen_columns = 79  # TO DO: On Python 3 use the function to take the actual screen size
		#self.screen_lines = 41  # TO DO: On Python 3 use the function to take the actual screen size
	
	def show_wrong_seq(self, message, user_seq_list, game_seq_list, game_score):
		print "\n" + message
		print "\nPlayer sequence:" ,
		
		for seq_user in user_seq_list:
			print str(seq_user),
		
		print "\nGame sequence  :" ,
		
		for seq_game in game_seq_list:
			print str(seq_game),

		print ""
		
		if game_score > 0:
			# Show user score
			print "\nYou memorized %i numbers." % (game_score)

		print "\nGAME OVER %s!\n\n" % (self.player_name)

	def play_game(self):
		# Function to play the game
		global game_level

		# Set the time to play the sound
		sound_time = game_sound_time(game_level)
		
		# Initialize the user score
		game_score = 0
		# Initialize the lists of sounds
		game_seq_list = []
		user_sequence   = []
		# Initialize the validation of the sequence
		valid_sequence = True
		
		# Clean the screen
		clean_screen()
		
		# Show the start message
		print (actual_level() +
			   "\n\n" + self.player_name + 
		       ", memorize and repeat the sequence of numbers." +
		       "\n\nAre you ready?")
		# Message to pause the program for the user to read the message
		raw_input("\nPress <Enter> to start the game.")

		while valid_sequence:
			# Get a random number
			sound_number = random.randint(1, 4)
			# Add the number to the game sequence
			game_seq_list.append(sound_number)
			
			# Clean the screen
			clean_screen()

			# Verify if is the first number
			if len(game_seq_list) == 1:
				print self.player_name + ", memorize the first number:",
			else:
				print self.player_name + ", memorize the sequence of numbers:",

			# Loop to play all the sounds
			for i in range(len(game_seq_list)):
				# Play sound (sound_number, sound_time)
				play_sound(game_seq_list[i], sound_time)

			## Change the game color back because the sounds print in a diferent color
			#change_color(self.game_color)
			# Clean the screen to hide the sequence
			clean_screen()
			
			# Clean user sequence list
			user_seq_list = []

			# Verify if is the first number
			if len(game_seq_list) == 1:
				# Print a new line
				user_sequence = raw_input("\n" + self.player_name + 
					                      ", repeat the first number and press <Enter>: ")
			else:
				# Print a new line
				user_sequence = raw_input("\n" + self.player_name + 
					                      ", repeat the sequence of numbers and press <Enter>: ")
			# Clean the screen
			clean_screen()
			
			# Test if user sequence is right
			if len(user_sequence) < 1:
				# Change the validation
				valid_sequence = False
				# Print the message
				self.show_wrong_seq("Empty sequence!",
					                user_seq_list, game_seq_list, game_score)
			else:
				try:
					# Verify if the user typed space between the numbers
					if " " in user_sequence:
						# Convert the sequence to a list with spaces
						user_seq_list = [int(i) for i in user_sequence.split()]	
					else:
						# Convert the sequence to a list without spaces
						for num_seq in user_sequence:
							user_seq_list += [int(num_seq)]
				except ValueError:
					# Exception in case of invalid number
					# Change the validation
					valid_sequence = False
					# Print the message
					self.show_wrong_seq("Invalid number on the sequence!",
						                user_seq_list, game_seq_list, game_score)

				# Verify if the sequence still valid
				if valid_sequence:
					# Verify if the user typed the same quantity of sounds
					if len(user_seq_list) > len(game_seq_list):
						# Change the validation
						valid_sequence = False
						# Print the message
						self.show_wrong_seq("Wrong sequence!  Sequence typed is bigger than the correct sequence.",
						                    user_seq_list, game_seq_list, game_score)
					elif len(user_seq_list) < len(game_seq_list):
						# Change the validation
						valid_sequence = False
						# Print the message
						self.show_wrong_seq("Wrong sequence!  Sequence typed is smaller than the correct sequence.",
						                    user_seq_list, game_seq_list, game_score)
					else:
						# Verify if the sequence is the same
						if user_seq_list == game_seq_list:
							# Right sequence
							# Increment the score
							game_score = game_score + 1
							# Print the message

							# print ("\n%s %s!  Let's add more numbers."
							#        % (self.player_name, correct_seq_message()))
							# # Message to pause the program for the user to read the message
							# raw_input("\nPress <Enter> to go to the next sequence.")
						else:
							# Change the validation
							valid_sequence = False
							# Print the message
							self.show_wrong_seq("Wrong sequence!", user_seq_list, game_seq_list, game_score)

		# Message to pause the program for the user to read the message
		raw_input("\nPress <Enter> to continue.")