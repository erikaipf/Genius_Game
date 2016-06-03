# -*- coding: utf-8 -*-
"""
0 = Black          1 = Blue            2 = Green
3 = Aqua           4 = Red             5 = Purple
6 = Yellow         7 = White           8 = Gray
9 = Light Blue     10 = Light Green    11 = Light Aqua
12 = Light Red     13 = Light Purple   14 = Light Yellow

based on Python Wikipedia Bot
"""
import ctypes, sys

def print_in_color_windows(text, color):
    std_out_handle = ctypes.windll.kernel32.GetStdHandle(-11)

    for i in range(0, len(color)):
        ctypes.windll.kernel32.SetConsoleTextAttribute(std_out_handle, color[i])
        sys.stdout.write(text)
    # default white color 7
    ctypes.windll.kernel32.SetConsoleTextAttribute(std_out_handle, 7)
    
def test():
	text = u"Printing colored text on MS-DOS"
	# Loop to print all colors
	for color_number in range(15):
		print "\nColor:", color_number
		print_in_color_windows(text, [color_number])
		#print_in_color_windows(text, [1,3,9,2,6])

if __name__ == "__main__":
	test()
