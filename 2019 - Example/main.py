from math import sqrt


def divisors(n):
    divs = {1, n}
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            divs.update((i, n//i))
    return divs


class Pizza:
    def __init__(self, input_string):
        self.row_count, self.col_count, self.min_ingredients, self.max_cells = [int(x) for x in input_string.split("\n")[0].split(" ")]
        self.pizza_matrix = []
        for itm in input_string.split("\n")[1:-1]:
            self.pizza_matrix.append([])
            for character in list(itm):
                if character == "M":
                    self.pizza_matrix[-1].append(1)
                elif character == "T":
                    self.pizza_matrix[-1].append(0)

    def get_possible_rectangles(self):
        possible_rectangles = {}
        for max_cells_current in range(2, self.max_cells+1):
            print(max_cells_current)
            xs = list([x for x in divisors(max_cells_current) if x <= self.col_count])
            ys = list()
            for x in xs[::-1]:
                y = max_cells_current / x
                if y <= self.row_count:
                    ys.append(int(y))
                else:
                    xs.remove(x)
            xs = xs[::-1]
            possible_rectangles[max_cells_current] = list()
            for i in range(len(xs)):
                possible_rectangles[max_cells_current].append([xs[i], ys[i]])
        return possible_rectangles

    def slice(self):
        possibilities = []
        rectangles = self.get_possible_rectangles()
        print(rectangles)

        for x in range(self.col_count):
            for y in range(self.row_count):
                pass
                # print(self.pizza_matrix[y][x])

    def __repr__(self):
        ret = "Pizza:\n"
        ret += "  Minimale Anzahl an Zutaten pro Stück:\n"
        ret += "    " + str(self.min_ingredients) + "\n"
        ret += "  Maximale Anzahl an Kästchen pro Stück:\n"
        ret += "    " + str(self.max_cells) + "\n"
        ret += "  Matrix:\n"
        for row in self.pizza_matrix:
            ret += "    " + "  ".join([str(x) for x in row]) + "\n"
        return ret

    def __str__(self):
        return self.__repr__()


with open("c_medium.in") as f:
    input_data = f.read()

p = Pizza(input_data)
print(p)
print(p.slice())
