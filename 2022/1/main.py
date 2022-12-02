with open("input.txt") as f:
    lines = [line.rstrip() for line in f]

tab = []
tmp = 0
for line in lines:
    if line:
        tmp += int(line)
    else:
        tab.append(tmp)
        tmp = 0

print(f"Max= {max(tab)}")
print(f"Top 3= {sorted(tab)[-3:]}")
print(f"Sum top 3= {sum(sorted(tab)[-3:])}")
