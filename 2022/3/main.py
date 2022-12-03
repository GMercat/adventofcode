with open("input.txt") as f:
    lines = [line.rstrip() for line in f]

priorities = {}
for i in range(97, 97 + 26):
    priorities[chr(i)] = i - 96
for i in range(65, 65 + 26):
    priorities[chr(i)] = i - 64 + 26

sum = 0
for line in lines:
    half_size = int(len(line) / 2)
    item = list(set(line[:half_size]) & set(line[half_size:]))[0]
    sum += priorities[item]

print(f"Part 1 - Sum of priorities: {sum}")

sum = 0
for i in range(int(len(lines) / 3)):
    first = lines[i * 3]
    second = lines[i * 3 + 1]
    third = lines[i * 3 + 2]
    item = list(set(first) & set(second) & set(third))[0]
    sum += priorities[item]

print(f"Part 2 - Sum of priorities: {sum}")
