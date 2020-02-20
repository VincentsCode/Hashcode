import os
import winsound
import sys
from datetime import datetime
import builtins
from colorama import Fore, Style
import time
import random


if len(sys.argv) < 2:
    options = ['a', 'b', 'c', 'd', 'e', 'f']
else:
    options = sys.argv[1:]

reverse_sub_library_sort = bool(random.getrandbits(1))

negative_factor = random.randint(-10, 10)
positive_factor = random.randint(-10, 10)


def print(*args):
    print_string = f"[{Fore.CYAN}" + datetime.now().strftime('%H:%M:%S.%f') + f"{Style.RESET_ALL}] " + " ".join(map(str, args)).replace("\n", "")

    if len(args) == 0:
        print_string = ""

    builtins.print(print_string)


print(f"[{Fore.MAGENTA}*{Style.RESET_ALL}]", "Running for", options)

for chosen in options:
    print(f"[{Fore.MAGENTA}*{Style.RESET_ALL}] ->", chosen)
    builtins.print()

    # read
    f = open(chosen + ".in")
    content = f.read().split("\n")[:-1]
    f.close()

    # result vars
    sub_libraries = []
    sub_libraries_value = {}
    sub_libraries_books = []

    info_libraries_books_per_day = {}
    info_libraries_signup_days = {}

    # parse
    n_books, n_libraries, n_days = [int(x) for x in content[0].split(" ")]
    book_scores = [int(x) for x in content[1].split(" ")]

    # print(f"[{Fore.MAGENTA}*{Style.RESET_ALL}]", "Books:", n_books, "| Libraries:", n_libraries, "| Days:", n_days)
    # print(f"[{Fore.MAGENTA}*{Style.RESET_ALL}]", "Scores:", book_scores)

    for i in range(2, 2 + n_libraries + 1, 2):
        l_n_books, l_n_signup_days, l_n_books_per_day_after_signup = [int(x) for x in content[i].split(" ")]
        l_book_ids = sorted([int(x) for x in content[i+1].split(" ")], key=lambda b_id: book_scores[b_id], reverse=True)

        max_num_books_possible = (n_days - l_n_signup_days) * l_n_books_per_day_after_signup
        if max_num_books_possible > len(l_book_ids):
            max_num_books_possible = len(l_book_ids)
        # print(f"max_num_books_possible ({n_days} - {l_n_signup_days}) * {l_n_books_per_day_after_signup} =", max_num_books_possible)
        book_worth = sum([book_scores[int(l_book_ids[i])] for i in range(max_num_books_possible)])
        book_unique = 1  # TODO
        sub_libraries_value[int(i / 2)-1] = book_worth * book_unique * positive_factor - l_n_signup_days * negative_factor

        info_libraries_books_per_day[int(i / 2)-1] = l_n_books_per_day_after_signup
        info_libraries_signup_days[int(i / 2)-1] = l_n_signup_days

        sub_libraries_books.append(l_book_ids[:max_num_books_possible])
        # print(f"[{Fore.MAGENTA}*{Style.RESET_ALL}]", "LBooks:", l_n_books, "| LSignupDays:", l_n_signup_days, "| LBooksPerDayAfterSignup:", l_n_books_per_day_after_signup, "| BookIDs:", l_book_ids)

    builtins.print()

    # print info
    # print("Library Values:", sub_libraries_value)
    theoretical_max = sum(book_scores)
    sub_libraries = sorted(sub_libraries_value, reverse=reverse_sub_library_sort)

    global_days_left = n_days
    all_book_ids = []

    act_sub_libraries = []
    act_sub_libraries_books = []

    for library_id in sub_libraries:
        if global_days_left == 0:
            break

        if global_days_left - info_libraries_signup_days[library_id] <= 0:
            continue

        # print(f"Processing Library {library_id}: {len(sub_libraries_books[library_id])}")
        days_left = global_days_left - info_libraries_signup_days[library_id]
        global_days_left -= info_libraries_signup_days[library_id]
        # print("days_left", days_left, "| global_days_left", global_days_left)
        avail_book_num = info_libraries_books_per_day[library_id] * days_left
        avail_books_filtered = [b_id for b_id in sub_libraries_books[library_id] if b_id not in all_book_ids]

        # no use -> skip & undo global_days_left modification
        if len(avail_books_filtered) == 0:
            global_days_left += info_libraries_signup_days[library_id]
            continue

        new_book_score = sum([book_scores[int(avail_books_filtered[i])] for i in range(len(avail_books_filtered))])
        # if new_book_score < sub_libraries[sub_libraries.index(library_id) + 10]:
        #     # print("Not worth it anymore")
        #     global_days_left += info_libraries_signup_days[library_id]
        #     continue

        books = avail_books_filtered[:avail_book_num]
        # print("-> books:", avail_book_num, "->", books)
        if len(books) == 0:
            print("ERRROR")
            exit()
        act_sub_libraries.append(library_id)
        act_sub_libraries_books.append(books)
        for book_id in books:
            all_book_ids.append(book_id)

    builtins.print()
    print(f"[{Fore.MAGENTA}*{Style.RESET_ALL}]", "Theoretical Maximum:", theoretical_max)
    current_score = sum([book_scores[book_id] for book_id in set(all_book_ids)])

    builtins.print()
    if current_score != theoretical_max:
        print(f"[{Fore.RED}-{Style.RESET_ALL}]", "Current Score:", current_score, f"(Difference to TMax: {theoretical_max - current_score})")
    else:
        print(f"[{Fore.GREEN}+{Style.RESET_ALL}]", "Current Score == MAX:", current_score, f"(Difference to TMax: {theoretical_max - current_score})")
        winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
        winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
        winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
        winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
        winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
        winsound.PlaySound("SystemHand", winsound.SND_ALIAS)

    lines = []
    lines.append(len(act_sub_libraries))
    for i in range(len(act_sub_libraries)):
        lines.append(str(int(act_sub_libraries[i])) + " " + str(len(act_sub_libraries_books[i])))
        lines.append(' '.join([str(x) for x in act_sub_libraries_books[i]]))

    if not os.path.exists(chosen):
        os.mkdir(chosen)

    current_max = max([int(x.replace(".out", "")) for x in os.listdir(chosen)])
    print(f"[{Fore.MAGENTA}*{Style.RESET_ALL}]", "Current Maximum:", current_max, f"(Difference to TMax: {theoretical_max - current_max})")

    if current_score > current_max:
        print(f"[{Fore.GREEN}+{Style.RESET_ALL}]", "New Maximum:", current_score, f"(Difference to TMax: {theoretical_max - current_score})")
        winsound.PlaySound("SystemHand", winsound.SND_ALIAS)

    # print(f"[{Fore.GREEN}+{Style.RESET_ALL}]", "Submission:")
    f = open(chosen + "/" + str(current_score) + ".out", "w")
    for l in lines:
        # print(f"[{Fore.GREEN}+{Style.RESET_ALL}]", l)
        f.write(str(l) + "\n")
    f.close()
exit()

for chosen in options:
    print(f"[{Fore.MAGENTA}*{Style.RESET_ALL}] ->", chosen)
    builtins.print()

    # read
    f = open(chosen + ".in")
    content = f.read().split("\n")[:-1]
    f.close()

    # result vars
    sub_libraries = []
    sub_libraries_value = {}
    sub_libraries_books = []

    info_libraries_books_per_day = {}
    info_libraries_signup_days = {}

    # parse
    n_books, n_libraries, n_days = [int(x) for x in content[0].split(" ")]
    book_scores = [int(x) for x in content[1].split(" ")]

    # print(f"[{Fore.MAGENTA}*{Style.RESET_ALL}]", "Books:", n_books, "| Libraries:", n_libraries, "| Days:", n_days)
    # print(f"[{Fore.MAGENTA}*{Style.RESET_ALL}]", "Scores:", book_scores)

    for i in range(2, 2 + n_libraries + 1, 2):
        l_n_books, l_n_signup_days, l_n_books_per_day_after_signup = [int(x) for x in content[i].split(" ")]
        l_book_ids = sorted([int(x) for x in content[i+1].split(" ")], key=lambda b_id: book_scores[b_id], reverse=True)

        max_num_books_possible = (n_days - l_n_signup_days) * l_n_books_per_day_after_signup
        if max_num_books_possible > len(l_book_ids):
            max_num_books_possible = len(l_book_ids)
        # print(f"max_num_books_possible ({n_days} - {l_n_signup_days}) * {l_n_books_per_day_after_signup} =", max_num_books_possible)
        book_worth = sum([book_scores[int(l_book_ids[i])] for i in range(max_num_books_possible)])
        book_unique = 1  # TODO
        sub_libraries_value[int(i / 2)-1] = book_worth * book_unique * positive_factor - l_n_signup_days * negative_factor

        info_libraries_books_per_day[int(i / 2)-1] = l_n_books_per_day_after_signup
        info_libraries_signup_days[int(i / 2)-1] = l_n_signup_days

        sub_libraries_books.append(l_book_ids[:max_num_books_possible])
        # print(f"[{Fore.MAGENTA}*{Style.RESET_ALL}]", "LBooks:", l_n_books, "| LSignupDays:", l_n_signup_days, "| LBooksPerDayAfterSignup:", l_n_books_per_day_after_signup, "| BookIDs:", l_book_ids)

    builtins.print()

    # print info
    # print("Library Values:", sub_libraries_value)
    theoretical_max = sum(book_scores)
    sub_libraries = sorted(sub_libraries_value, reverse=reverse_sub_library_sort)

    global_days_left = n_days
    all_book_ids = []

    act_sub_libraries = []
    act_sub_libraries_books = []

    while True:
        if len(sub_libraries) == 0:
            break
        library_id = random.choice(sub_libraries)

        if global_days_left == 0:
            break

        if global_days_left <= min([info_libraries_signup_days[l_id] for l_id in sub_libraries]):
            break

        if global_days_left - info_libraries_signup_days[library_id] <= 0:
            continue

        # print(f"Processing Library {library_id}: {len(sub_libraries_books[library_id])}")
        days_left = global_days_left - info_libraries_signup_days[library_id]
        global_days_left -= info_libraries_signup_days[library_id]
        # print("days_left", days_left, "| global_days_left", global_days_left)
        avail_book_num = info_libraries_books_per_day[library_id] * days_left
        avail_books_filtered = [b_id for b_id in sub_libraries_books[library_id] if b_id not in all_book_ids]

        # no use -> skip & undo global_days_left modification
        if len(avail_books_filtered) == 0:
            global_days_left += info_libraries_signup_days[library_id]
            continue

        # new_book_score = sum([book_scores[int(avail_books_filtered[i])] for i in range(len(avail_books_filtered))])
        # try:
        #     if new_book_score < sub_libraries[sub_libraries.index(library_id) + 10]:
        #         print("Not worth it anymore")
        #         global_days_left += info_libraries_signup_days[library_id]
        #         continue
        # except:
        #     pass

        books = avail_books_filtered[:avail_book_num]
        # print("-> books:", avail_book_num, "->", books)
        if len(books) == 0:
            print("ERRROR")
            exit()
        act_sub_libraries.append(library_id)
        act_sub_libraries_books.append(books)
        sub_libraries.remove(library_id)
        for book_id in books:
            all_book_ids.append(book_id)
        if global_days_left % 100 == 0:
            print(global_days_left)

    builtins.print()
    print(f"[{Fore.MAGENTA}*{Style.RESET_ALL}]", "Theoretical Maximum:", theoretical_max)
    current_score = sum([book_scores[book_id] for book_id in set(all_book_ids)])

    builtins.print()
    if current_score != theoretical_max:
        print(f"[{Fore.RED}-{Style.RESET_ALL}]", "Current Score:", current_score, f"(Difference to TMax: {theoretical_max - current_score})")
    else:
        print(f"[{Fore.GREEN}+{Style.RESET_ALL}]", "Current Score == MAX:", current_score, f"(Difference to TMax: {theoretical_max - current_score})")
        winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
        winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
        winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
        winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
        winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
        winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
        winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
        winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
        winsound.PlaySound("SystemHand", winsound.SND_ALIAS)

    lines = []
    lines.append(len(act_sub_libraries))
    for i in range(len(act_sub_libraries)):
        lines.append(str(int(act_sub_libraries[i])) + " " + str(len(act_sub_libraries_books[i])))
        lines.append(' '.join([str(x) for x in act_sub_libraries_books[i]]))

    if not os.path.exists(chosen):
        os.mkdir(chosen)

    current_max = max([int(x.replace(".out", "")) for x in os.listdir(chosen)])
    print(f"[{Fore.MAGENTA}*{Style.RESET_ALL}]", "Current Maximum:", current_max, f"(Difference to TMax: {theoretical_max - current_max})")

    if current_score > current_max:
        print(f"[{Fore.GREEN}+{Style.RESET_ALL}]", "New Maximum:", current_score, f"(Difference to TMax: {theoretical_max - current_score})")
        print(f"[{Fore.GREEN}+{Style.RESET_ALL}] {Fore.RED}HEREHEREHEREHEREHEREHEREHEREHEREHEREHEREHEREHEREHEREHEREHEREHEREHEREHEREHEREHEREHEREHEREHEREHEREHEREHERE{Style.RESET_ALL}")
        winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
        time.sleep(5)

    # print(f"[{Fore.GREEN}+{Style.RESET_ALL}]", "Submission:")
    f = open(chosen + "/" + str(current_score) + ".out", "w")
    for l in lines:
        # print(f"[{Fore.GREEN}+{Style.RESET_ALL}]", l)
        f.write(str(l) + "\n")
    f.close()
