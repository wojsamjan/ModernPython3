from pyfiglet import figlet_format as ff
from termcolor import colored


def print_art(msg, color):
	valid_colors = ("red", "green", "yellow", "blue", "magenta", "cyan", "white")

	if color not in valid_colors:
		color = "magenta"

	ascii_art = ff(msg)
	colored_ascii = colored(ascii_art, color=color)
	print(colored_ascii)


msg = input("What would you like to print? ")
color = input("What color? ").lower()
print_art(msg, color)
