import os
import winsound
import itertools
import sys
from datetime import datetime
import builtins
from colorama import Fore, Style

if len(sys.argv) < 2:
	options = ['a', 'b', 'c', 'd', 'e']
else:
	options = sys.argv[1:]

# noinspection PyShadowingBuiltins
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

	# get results
	def get_results():
		print(f"[{Fore.GREEN}+{Style.RESET_ALL}]", "Generating options")
		order_pizza_types = []
		current_max = 0
		for L in range(0, len(pizza_types.keys())+1):
			for itm in itertools.combinations(pizza_types.keys(), L):
				res_sum = 0
				for key in itm:
					res_sum += pizza_types[key]

				# print(res_sum, itm)

				if res_sum == max_slices:
					print(f"[{Fore.GREEN}+{Style.RESET_ALL}]", "NEW GLOBAL MAX:", L, "/", len(pizza_types.keys())+100, "|", res_sum, itm)
					return itm
				elif res_sum <= max_slices and res_sum >= current_max:
					order_pizza_types = itm
					current_max = res_sum
					print("[ ] New local max:", L, "/", len(pizza_types.keys())+100, "|", res_sum, itm)

		return order_pizza_types


	order_pizza_types = get_results()
	order_num_types = len(order_pizza_types)
	result_points = sum([pizza_types[k] for k in order_pizza_types])

	# write results
	if not os.path.exists(chosen):
		os.mkdir(chosen)

	current_max = max([int(x.replace(".out", "")) for x in os.listdir(chosen) if x.endswith(".out")]) if len(os.listdir(chosen)) != 0 else 0
	print(f"[{Fore.GREEN}+{Style.RESET_ALL}]", "New Score (Current Max): {} ({})".format(result_points, current_max))

	if max_slices-result_points == 0:
		print(f"[{Fore.GREEN}+{Style.RESET_ALL}]", "Perfect Score (Diff = 0)")
	else:
		print(f"[{Fore.RED}-{Style.RESET_ALL}]", "Diff to Max: {}".format(max_slices-result_points))

	if result_points > current_max:
		print(f"[{Fore.GREEN}+{Style.RESET_ALL}]", "NEW HIGHSCORE!")
		winsound.Beep(2500, 200)

	f = open(chosen + "/" + str(result_points) + ".out", "w")
	f.write(str(order_num_types) + "\n")
	f.write(' '.join([str(x) for x in sorted(order_pizza_types)]) + "\n")
	f.close()

	print()