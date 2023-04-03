# skool_points

## Skool points

- Todo : 

    [X]  Make a pseudocode.

    [X]  Write program in python based on the pseudocode

### Specs. :

- Points

  You earn points when other members like your posts or comments.

  1 like = 1 point.

  This encourages users to produce quality content and interact with other members in their community.


- Levels :

  As you gain points, you level up. Your level is shown at the bottom right of your avatar.

  The number of points required to get to the next level is shown under your avatar on your profile page.

  Level 1 - 0 points
  Level 2 - 5 points
  Level 3 - 20 points
  Level 4 - 65 points
  Level 5 - 155 points
  Level 6 - 515 points
  Level 7 - 2,015 points
  Level 8 - 8,015 points
  Level 9 - 33,015 points

---

### The Pseudocode <em>(use ‘while’ loop)</em> :

```markdown
Create a variable called points and set it to 0
Create a variable called level and set it to 1
Create a dictionary called levels with keys as level numbers and values as points required to reach that level
Create a loop that will continue until the user decides to quit
    Ask the user if they want to post or comment
    If they choose to post,
        Ask for the content of their post
        Add 1 point to their points variable
    If they choose to comment,
        Ask for the content of their comment
        Add 1 point to their points variable
    Check if the user has reached the next level by comparing their points with the value in the levels dictionary for their current level.
    If they have,
        Increase their level by 1.
        Print out a message notifying them of their new level.
    Ask the user if they want to continue or quit.
Print out the final points and level of the user.
```

### The code :

```python

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

```