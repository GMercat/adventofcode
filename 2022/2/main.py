with open("input.txt") as f:
    lines = [line.rstrip() for line in f]

# Part 1
# A Rock
# B Paper
# C Scissors

# X Rock
# Y Paper
# Z Scissors

# X > C
# Y > A
# Z > B

score = 0
for line in lines:
    oponent, me = line.split(" ")
    if me == "X":
        score += 1
        if oponent == "C":
            score += 6
        elif oponent == "A":
            score += 3
    elif me == "Y":
        score += 2
        if oponent == "A":
            score += 6
        elif oponent == "B":
            score += 3
    else:
        score += 3
        if oponent == "B":
            score += 6
        elif oponent == "C":
            score += 3

print(f"Part 1 - Final score: {score}")


# Part 2
# X Lose
# Y Draw
# Z Win

# A Rock
# B Paper
# C Scissors

# Rock = 1
# Paper = 2
# Scissors = 3

score = 0
for line in lines:
    oponent, me = line.split(" ")
    if me == "X":
        score += 0
        if oponent == "A":
            score += 3
        elif oponent == "B":
            score += 1
        elif oponent == "C":
            score += 2
    elif me == "Y":
        score += 3
        if oponent == "A":
            score += 1
        elif oponent == "B":
            score += 2
        elif oponent == "C":
            score += 3
    elif me == "Z":
        score += 6
        if oponent == "A":
            score += 2
        elif oponent == "B":
            score += 3
        elif oponent == "C":
            score += 1

print(f"Part 2 - Final score: {score}")
