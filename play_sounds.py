'''
Module to play the sounds
Created by Erika Freiha | May-31-2016

This module Plays 4 sounds:
Choose between 4 options (number 1, 2, 3, or 4)
Choose the speed in milliseconds (default 1300)
'''
# Import modules
import winsound
# Import personal modules
from color_text_screen import change_color


def play_sound(sound_number, sound_time = 1300, print_num_option = 1):
	''' 
	print_num_option = 1-Prints the numbers on the same line
					   2-Prints the number on different lines
					   3-Doesn't print the number
	'''
	# Verify the print option 
	if print_num_option == 1:
		# 1-Prints the numbers on the same line
		# Print the sound number (comma prints the sound in the same line)
		print sound_number,
	elif print_num_option == 2:
		# 2-Prints the number on different lines
		print sound_number
	#else: 3 or other numbers-Doesn't print the number

	# Verify the number of the sound to play
	# The frequency of the sound is 37 thru 32767
	if sound_number == 1:
		# Play the sound
		winsound.Beep(390, sound_time)
	elif sound_number == 2:
		# Play the sound
		winsound.Beep(440, sound_time)
	elif sound_number == 3:
		# Play the sound
		winsound.Beep(500, sound_time)
	elif sound_number == 4:
		# Play the sound
		winsound.Beep(600, sound_time)


def play_sound_color(sound_number, original_color = 7, new_color = 7, sound_time = 1300):
	# The frequency of the sound is 37 thru 32767
	# Verify if the colors are differnt
	if original_color != new_color:
		# Change to new color
		change_color(new_color)
		# Print the sound number (comma prints the sound in the same line)
		print sound_number,
		# Change back to original color
		change_color(original_color)
	else:
		# Print the sound number (comma prints the sound in the same line)
		print sound_number,
		
	# Verify the number of the sound to play
	if sound_number == 1:
		# Play the sound
		winsound.Beep(390, sound_time)
	elif sound_number == 2:
		# Play the sound
		winsound.Beep(440, sound_time)
	elif sound_number == 3:
		# Play the sound
		winsound.Beep(500, sound_time)
	elif sound_number == 4:
		# Play the sound
		winsound.Beep(600, sound_time)


def test():
	print "This module Plays 4 sounds:"
	for sound_num in range(1,5):
		play_sound(sound_num, print_num_option = 3)

	print "\nThe the 4 sounds in a different speeds and ways:"
	for sound_num in range(1,5):
		print " # ",
		play_sound(sound_num, 1000)

	for sound_num in range(1,5):
		print "\nSound number:"
		play_sound(sound_num, 800, print_num_option = 2)


if __name__ == "__main__":
	test()