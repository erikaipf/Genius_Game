'''
Module to print menus
Created by Erika Freiha | May-31-2016
'''
#To Do: For Python 3, use the functions to get the actual size of the screen
# Create global string
pause_message = "Press <Enter> to continue."

def clean_screen(screen_lines = 31):
	# Only at Python 3
	# try:
	#     import os
	#     v_lines = os.get_terminal_size().lines
	# except AttributeError:
	#     v_lines = 130
	#print("\n" * v_lines)
	# Python 2.7.9
	# Default 33 lines, 79 columns at my screen
	print "\n" * screen_lines


def show_pause_message(pause_frase = pause_message,
					   clean_screen_after = False):
	'''Show the message to pause the program for the user to read the message.
	   Adicional option to clean the screen after'''
	# Show the pause message
	raw_input("\n" + pause_frase)

	# Verify if needs to clean the screen
	if clean_screen_after == True:
		# Clean the screen
		clean_screen()


def show_message_with_pause(message,
							pause_frase = pause_message,
							clean_screen_after = False):
	'''Show the message and a raw_input message after to pause before clean the screen'''
	if len(message) > 0:
		# Show the message
		print "\n" + message
		
	# Show the message to pause the program for the user to read the message
	show_pause_message(pause_frase, clean_screen_after)


def show_info(text_info,
			  screen_lines = 31,
			  center_info = True,
			  after_message_lines = 1,
			  pause_frase = pause_message,
			  pause_screen = True):
	'''Print the Info Centralized on the screen'''
	# Count how many empty lines need to be printed
	empty_lines = ((screen_lines - text_info.count("\n")) / 2)

	# Print empty lines before info
	print "\n " * empty_lines

	# Verify if is to center the info
	if center_info:
		list_info = text_info.split("\n")
		# Print the info centralized
		for line in list_info:
			print line.center(79)
	else:
		# Print info
		print text_info

	# Print empty lines after info
	print "\n " * (empty_lines - after_message_lines)

	if pause_screen:
		# Show a pause message for the user to read the message
		show_pause_message(pause_frase, False)


def show_menu(text_menu,
			  screen_lines = 31,
			  empty_top_lines = 0,
			  botton_msg_lines = 0):
	'''
	Print the Menu Centralized on the screen
	Parameters:
	text_menu: Text of the Menu, will be splitted by the end of line "\\n"
	screen_lines: Number of lines of your screen
    empty_top_lines: Define how many empty lines want to be printed before the menu
    botton_msg_lines: Use this option print the menu in the middle of screen
                      counting with the lines of messages after the menu
	'''
	list_menu = text_menu.split("\n")
	printed_lines = 0
	# Verify if the menu need to be printed after a number of empty lines
	if empty_top_lines > 0:
		# Print the empty lines before the menu
		print "\n" * empty_top_lines
		printed_lines = empty_top_lines
	else:
		printed_lines = ((screen_lines - len(list_menu))/2)
		# Print the empty lines before the menu
		print "\n" * printed_lines
	
	# Print the Menu
	for line in list_menu:
		print line.center(79)

	# Print the empty lines after the menu
	print "\n" * (screen_lines - len(list_menu) - printed_lines - botton_msg_lines)


def show_menu_original(text_menu,
					   screen_lines = 31,
					   empty_top_lines = 0,
					   botton_msg_lines = 0):
	'''
	Print the Menu as Original on the screen
	Parameters:
	text_menu: Text of the Menu, will be splitted by the end of line "\\n"
	screen_lines: Number of lines of your screen
    empty_top_lines: Define how many empty lines want to be printed before the menu
    botton_msg_lines: Use this option print the menu in the middle of screen
                      counting with the lines of messages after the menu
	'''
	printed_lines = 0
	#Count how many lines the menu has
	lines_menu = len(text_menu.split("\n"))
	
	# Verify if the menu need to be printed after a number of empty lines
	if empty_top_lines > 0:
		# Print the empty lines before the menu
		print "\n" * empty_top_lines
		printed_lines = empty_top_lines
	else:
		printed_lines = ((screen_lines - lines_menu)/2)
		# Print the empty lines before the menu
		print "\n" * printed_lines
	
	# Print the Menu
	print text_menu

	# Print the empty lines after the menu
	print "\n" * (screen_lines - lines_menu - printed_lines - botton_msg_lines)


def show_msg_clean_screen(message, screen_lines = 31):
	'''Show a message in a clean screen'''
	# Print the text
	print (("\n " * (screen_lines - message.count("\n"))) + 
		   message + "\n")

	# Show a pause message for the user to read the message
	show_pause_message(pause_message, False)


def test_center():
	menu = ("\n+------------------------+" +
		    "\n|   ** Program Name **   |" +
		    "\n+------------------------+" +
		    "\n| Centralized  Main Menu |" +
		    "\n+------------------------+" +
		    "\n|  1 - Option 1          |" +
		    "\n|  2 - Option 2          |" +
		    "\n|  3 - Option 2          |" +
		    "\n+------------------------+" +
		    "\n|  0 - Exit              |" +
		    "\n+------------------------+")

	#Function to print: show_menu(text_menu, screen_lines = 31, empty_top_lines = 0, botton_msg_lines = 0)
	show_menu(menu)

	raw_input("The Menu looks great! :)  Press <Enter> to finish:")


def test_original():
	menu = """
			 +------------------------+
			 |   ** Program  Name **  |
			 +------------------------+
			 |   Original Main Menu   |
			 +------------------------+
			 |  1 - Option 1          |
			 |  2 - Option 2          |
			 |  3 - Option 2          |
			 +------------------------+
			 |  0 - Exit              |
			 +------------------------+
		   """
	#Function to print: (text_menu, screen_lines = 31, empty_top_lines = 0, botton_msg_lines = 0):
	show_menu_original(menu)

	raw_input("The Menu looks great! :)  Press <Enter> to finish:")


if __name__ == "__main__":
	# show_message_with_pause(message, pause_frase = pause_message, clean_screen_after = False)
	show_message_with_pause("This is a message with a pause.")
	show_message_with_pause("This is a message with a pause and clean the screen after.",
	                        clean_screen_after = True)
	
	# show_info(text_info, screen_lines = 31, center_info = True, after_message_lines = 0)
	show_info("Showing some info...")

	clean_screen()
	print "The Screen is clean now! :)"
	# pause_message(pause_frase = pause_message, clean_screen_after = False)
	show_pause_message()
	
	# testing menus
	test_original()
	test_center()