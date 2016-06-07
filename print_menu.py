'''
Module to print menus
Created by Erika Freiha | May-31-2016
'''
#To Do: For Python 3, use the functions to get the actual size of the screen

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

def show_info(text_info, screen_lines = 31, center_info = True, after_message_lines = 0):
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
		print text_info

	print "\n " * (empty_lines - after_message_lines)

def show_menu(text_menu, screen_lines = 31, empty_top_lines = 0, botton_msg_lines = 0):
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

def show_msg_clean_screen(message, screen_lines = 31):
	'''Clean the screen and print the screen'''
	# Print the text
	print (("\n " * (screen_lines - message.count("\n"))) + 
		   message + "\n")

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

	show_menu_center(menu)

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
	show_menu(menu)

	raw_input("The Menu looks great! :)  Press <Enter> to finish:")

if __name__ == "__main__":
	clean_screen()
	raw_input("The Screen is clean now! :)  Press <Enter> to contine:")

	test_original()
	test_center()