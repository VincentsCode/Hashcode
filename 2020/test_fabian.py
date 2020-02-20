from random import shuffle

current = "c"

f = open(current + ".in")
content = f.read().split("\n")[:-1]
f.close()

# parse
n_books, n_libraries, n_days = [int(x) for x in content[0].split(" ")]
book_scores = [int(x) for x in content[1].split(" ")]

libs_scanned = 0
book_id_scores = {}

output_string = ""

print("Books:", n_books, "| Libraries:", n_libraries, "| Days:", n_days)
print("Scores:", book_scores)

book_scores_dict = {}

libs = {}

absolute_score = 0

lib_max_scores = {}

for i in range(0, len(book_scores)):
    book_scores_dict[i] = book_scores[i]

lib_id = 0

x = 2
y = .5

for i in range(2, 2 + n_libraries + 1, 2):
    l_n_books, l_n_signup_days, l_n_books_per_day_after_signup = content[i].split(" ")
    l_book_ids = content[i + 1].split(" ")
    print("LBooks:", l_n_books, "| LSignupDays:", l_n_signup_days, "| LBooksPerDayAfterSignup:", l_n_books_per_day_after_signup, "| BookIDs:", l_book_ids)
    maxScore = 0

    s = {}
    for id in l_book_ids:
        s[id] = book_scores_dict[int(id)]
        maxScore = maxScore + book_scores_dict[int(id)]

    s_sorted = {}

    for key, value in sorted(s.items(), key=lambda item: item[1], reverse=True):
        s_sorted[key] = value

    lib_max_scores[x * maxScore * (1 / (int(l_n_signup_days) * y))] = lib_id
    libs[lib_id] = (l_n_signup_days, l_n_books_per_day_after_signup, s_sorted)
    lib_id = lib_id + 1

sortedMaxScores = {}
for key in sorted(lib_max_scores.keys(), reverse=True):
    sortedMaxScores[key] = lib_max_scores[key]

print("sorted scores: ", sortedMaxScores)

day = 0

lines = []
all_scanned = []
for _, v in sortedMaxScores.items():
    signup_time = libs[v][0]
    day += int(signup_time)

    books_day = int(libs[v][1])
    scores = libs[v][2]

    days_left = n_days - day

    if days_left < 0:
        break

    libs_scanned += 1
    books_scanned = 0

    scanned = []

    print("Days left: ", days_left)

    for dy in range(0, days_left):
        for book_per_day in range(0, books_day):
            if len(scores) < 1:
                break
            current_it = 0
            current_book_id = list(scores.keys())[current_it]
            while current_book_id in all_scanned:
                print(v, "DUPLICATE")
                try:
                    current_book_id = list(scores.keys())[current_it]
                except IndexError:
                    break
                current_it += 1
            scanned.append(current_book_id)
            all_scanned.append(current_book_id)
            absolute_score += list(scores.values())[0]
            scores.pop(list(scores.keys())[0])
            books_scanned += 1

    lines.append(str(v) + " " + str(books_scanned))
    book_ids_string = ""

    for book_id in scanned:
        book_ids_string += str(book_id) + " "

    lines.append(book_ids_string)

print("Score: ", absolute_score)

f = open(current + "." + "out", "w")
f.write(str(libs_scanned) + "\n")
for l in lines:
    f.write(str(l) + "\n")
f.close()