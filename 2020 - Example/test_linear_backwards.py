import os
import winsound

options = ['a', 'b', 'c', 'd', 'e']
for chosen in options:
	print(chosen)
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
	print("Theoretical Max.:", max_slices)
	# print("Num. Types :", num_types)
	# print("Content ({}):".format(len(content)), str(content[0:min(len(content), 10)])[1:-1].replace("'", "") + (", ..." if len(content) > 10 else ""))

	# print("Types ({})  :".format(len(pizza_types)), str(str(pizza_types).replace("{", "").replace("}", "").split(",")[0:10])[1:-1].replace("'", "").replace("  ", " ") + (", ..." if len(pizza_types) > 10 else ""))
	# print()

	# get results
	order_pizza_types = []

	current_slices = 0
	for key in sorted(pizza_types, reverse=True):
		value = pizza_types[key]
		if value <= max_slices - current_slices:
			order_pizza_types.append(key)
			current_slices += value

	order_num_types = len(order_pizza_types)

	result_points = sum([pizza_types[k] for k in order_pizza_types])

	# write results
	if not os.path.exists(chosen):
		os.mkdir(chosen)

	current_max = max([int(x.replace(".out", "")) for x in os.listdir(chosen) if x.endswith(".out")]) if len(os.listdir(chosen)) != 0 else 0
	print("New Score (Current Max): {} ({})".format(result_points, current_max))
	print("Diff to Max: {}".format(max_slices-result_points))

	if result_points > current_max:
		print("NEW HIGHSCORE!")
		winsound.Beep(2500, 200)

	f = open(chosen + "/" + str(result_points) + ".out", "w")
	f.write(str(order_num_types) + "\n")
	f.write(' '.join([str(x) for x in sorted(order_pizza_types)]) + "\n")
	f.close()

	print()