import os
import winsound
import itertools
import sys
from datetime import datetime
import builtins
from colorama import Fore, Style
import random


if len(sys.argv) < 2:
	options = ['a', 'b', 'c', 'd', 'e']
else:
	options = sys.argv[1:]

def print(*args):
    print_string = f"[{Fore.CYAN}" + datetime.now().strftime('%H:%M:%S.%f') + f"{Style.RESET_ALL}] " + " ".join(map(str, args)).replace("\n", "")

    if len(args) == 0:
    	print_string = ""

    builtins.print(print_string)

print(f"[{Fore.MAGENTA}*{Style.RESET_ALL}]", "Running for", options)

for chosen in options:
	print(f"[{Fore.MAGENTA}*{Style.RESET_ALL}]", chosen)
	# read
	f = open(chosen + ".in")
	content = f.read().split("\n")
	f.close()

	# parse
	max_slices, num_types = [int(x) for x in content[0].split(" ")]
	content = content[1:-1][0].split(" ")

	pizza_types = {}
	for i in range(num_types):
		pizza_types[i] = int(content[i])

	# print info
	print(f"[{Fore.GREEN}+{Style.RESET_ALL}]", "Theoretical Max.:", max_slices)

	itms = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22, 24, 25, 26, 27, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]

	val_sum = 0
	for itm in itms:
		val = pizza_types[itm]
		print(itm, "->", val)
		val_sum += val
	print("=>", val_sum)
	print(len(itms))
