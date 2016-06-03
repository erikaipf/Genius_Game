'''
Module to print menus
Created by Erika Freiha | May-31-2016
'''
#To Do: For Python 3, use the functions to get the actual size of the screen

def clean_screen():
	# Only at Python 3
	# try:
	#     import os
	#     v_lines = os.get_terminal_size().lines
	# except AttributeError:
	#     v_lines = 130
	#print("\n" * v_lines)
	# Python 2.7.9
	# Default 33 lines, 79 columns at my screen
	print("\n" * 31)

def show_menu(text_menu, screen_lines = 31):
	'''Print the Menu Formatted'''
	# Print the menu
	print (("\n " * ((screen_lines - text_menu.count("\n")) /2)) + 
		   text_menu +
		   ("\n " * ((screen_lines - text_menu.count("\n")) /2 + 1)))

def show_menu_center(text_menu, screen_lines = 31):
	'''Print the Menu Formatted and Centralized'''
	list_menu = text_menu.split("\n")

	list_menu_lines = len(list_menu)

	# Print the menu
	print "\n " * ((screen_lines - list_menu_lines) /2)

	for line in list_menu:
		print line.center(79)

	print "\n " * (((screen_lines - list_menu_lines) /2) + 1)

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