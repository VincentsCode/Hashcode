import os

options = ['a', 'b', 'c', 'd', 'e', 'f']


while True:
    option_values = []
    for chosen in options:
        current_max = max([int(x.replace(".out", "")) for x in os.listdir(chosen)])
        option_values.append(current_max)
    result = []
    for i in range(len(options)):
        result.append(options[i] + ": " + str(option_values[i]))
    print(' | '.join(result), end="\r")
