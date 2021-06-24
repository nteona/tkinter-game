import csv
LEADERBOARD = []


def save_leaderboard():
    global LEADERBOARD
    with open("leaderboard.csv", "w", newline="") as leaderboard_file:
        writer = csv.writer(leaderboard_file)
        writer.writerows(LEADERBOARD)


def load_leaderboard():
    global LEADERBOARD
    LEADERBOARD = []
    with open("leaderboard.csv", newline="") as leaderboard_file:
        reader = csv.reader(leaderboard_file)
        for (name, score) in reader:
            LEADERBOARD.append((name, int(score)))
    return sort_leaderboard()


def sort_leaderboard():
    global LEADERBOARD
    print(LEADERBOARD)
    LEADERBOARD = sorted(LEADERBOARD, key=lambda item: item[1], reverse=True)
    print(LEADERBOARD)
    return LEADERBOARD
