# -*- coding: utf-8 -*-
'''
Module to print text in color for windows
Colors (black background):
0 = Black          1 = Blue            2 = Green
3 = Aqua           4 = Red             5 = Purple
6 = Yellow         7 = White           8 = Gray
9 = Light Blue     10 = Light Green    11 = Light Aqua
12 = Light Red     13 = Light Purple   14 = Light Yellow
15 = Light White
-
(16 to 31) - Blue background   (32 to 47) - Green background ... until 255 - Light White foreground and background
'''
import ctypes, sys

def change_color(color_number):
	std_out_handle = ctypes.windll.kernel32.GetStdHandle(-11)

	# Set the color
	ctypes.windll.kernel32.SetConsoleTextAttribute(std_out_handle, color_number)

def print_one_color(text, color_number):
	std_out_handle = ctypes.windll.kernel32.GetStdHandle(-11)

	# Set the color
	ctypes.windll.kernel32.SetConsoleTextAttribute(std_out_handle, color_number)
	# Print the text using the color
	sys.stdout.write(text)
	# Or
	#print text

	# Set back the white color (7)
	ctypes.windll.kernel32.SetConsoleTextAttribute(std_out_handle, 7)

def print_dif_colors(text, colors_list):
	std_out_handle = ctypes.windll.kernel32.GetStdHandle(-11)

	# Loop to print in different colors
	for i in range(0, len(colors_list)):
		# Set the color
		ctypes.windll.kernel32.SetConsoleTextAttribute(std_out_handle, colors_list[i])
		# Print the text using the color
		sys.stdout.write("\n" + text)
		# Or
		#print "\n" + text

	# Set back the white color (7)
	ctypes.windll.kernel32.SetConsoleTextAttribute(std_out_handle, 7)

def test():
	#text = u"Printing colored text on MS-DOS"
	text = "Printing colored text on MS-DOS"
	
	# Print only one color
	print "\n\nPrint only one color:"
	print_one_color(text, 3)

	print "\n\nPrint all colors:"
	# Loop to print all colors
	for color_number in range(256):
		print "\nColor:", color_number
		print_one_color(text, color_number)
		
	# # or Print a list of colors
	# print "\n\nPrint a list of colors:"
	# print_dif_colors(text, [1,3,9,2,6])

if __name__ == "__main__":
	test()
