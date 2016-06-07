'''
Module to play the sounds
Created by Erika Freiha | May-31-2016

This module Plays 4 sounds:
Choose between 4 options (number 1, 2, 3, or 4)
Choose the speed in milliseconds (default 1300)
'''
import winsound

def play_sound(sound_number, sound_time = 1300):
	# The frequency of the sound is 37 thru 32767
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
	for sound_num in range(5):
		print "\nSound number %i:" % (sound_num)
		play_sound(sound_num)

	print "\nThe same sounds in a diferent speed:"
	for sound_num in range(5):
		print "\nSound number %i:" % (sound_num)
		play_sound(sound_num, 1000)

	for sound_num in range(5):
		print "\nSound number %i:" % (sound_num)
		play_sound(sound_num, 800)

if __name__ == "__main__":
	test()