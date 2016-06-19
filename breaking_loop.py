from genius_game_class import*
from random import randint
from play_sounds import play_sound

# Option 1 - Wait for <Ctrl> + C
def break_option_1():
	try:
		while True:
			sound_number = randint(1, 4)
			# Play the sound and show the colored number
			play_sound_color(sound_number, game_color, sound_color[sound_number], 1000)
	except KeyboardInterrupt:
	    pass

# Option 2 - Breaks with <Enter> but shows typed strings
import thread

def input_thread(list):
    raw_input()
    list.append(None)

def do_stuff():
    list = []
    thread.start_new_thread(input_thread, (list,))
    while not list:
		sound_number = randint(1, 4)
		# Play the sound and show the colored number
		play_sound_color(sound_number, game_color, sound_color[sound_number], 1000)

def test():
	# Option 1
	break_option_1()
	# # Option 2
	# do_stuff()
	# Option 3
	

test()

print "keep working"