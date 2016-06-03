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
class GeniusGame(object):
	def __init__(self, game_level = 1):
		self.game_level = game_level
		self.screen_columns = 79  # TO DO: On Python 3 use the function to take the actual screen size
		#self.screen_lines = 41  # TO DO: On Python 3 use the function to take the actual screen size
		self.game_info = ("Welcome to  ** Genius Game **\n\n"+
						  "The game has four colored numbers, each producing a particular tone when it is used.\n" +
			              "A round in the game consists of showing one or more numbers in a random order,\n" +
			              "after which the player must reproduce that order by typing the numbers and pressing <Enter>.\n" +
			              "As the game progresses, the number of numbers to be typed increases.\n\n" +
			              "Good Luck!")

	def game_level_name(game_level):
		# Return the name of the level
		if game_level == 1:
			return "Beginner"
		elif game_level == 2:
			return "Intermediate"
		elif game_level == 3:
			return "Advanced"

	def actual_level_name(self):
		# Return the name of the actual level of the game
		if self.game_level in (1,2,3):
			return game_level_name(self.game_level)
		else:
			return "Invalid Level"
	
	def actual_level(self):
		# Return the actual level of the game
		if self.game_level in (1,2,3):
			return "\nYou are at Level %i - %s." % (self.game_level, actual_level_name())
		else:
			return "\nInvalid Level!"
	
	# def change_game_level(self, new_level):
	# 	# Verify if the new level is valid
	# 	if new_level in (1,2,3):
	# 		self.game_level = new_level
	# 	else:
	# 		print "\nInvalid new Level!  Please try again."

	