points = 0
level = 1
levels = {1: 0, 2: 5, 3: 20, 4: 65, 5: 155, 6: 515, 7: 2015, 8: 8015, 9: 33015}

while True:
    action = input(
        "Do you want to 'post'(p) or 'comment'(c)? or 'quit'(q)")

    if action == 'q':
        print(
            f"Your final points are {points} and your current level is {level}.")
        break

    elif action == 'p':
        content = input("What do you want to post? ")
        points += 1

    elif action == 'c':
        content = input("What do you want to comment? ")
        points += 1

    if points >= levels[level+1]:
        level += 1
        print(f"Congratulations! You just reached level {level}!")

    continue_or_quit = input("Do you want to 'continue'(c) or 'quit'(q)? ")

    if continue_or_quit == 'q':
        print(
            f"Your final points are {points} and your current level is {level}.")
        break
