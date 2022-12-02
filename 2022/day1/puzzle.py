with open("input", "r") as f:
    lines = f.readlines()

calories = []
temp_calorie = 0
for i, line in enumerate(lines):
    if line.strip() == "":
        calories.append(temp_calorie)
        temp_calorie = 0
    else:
        temp_calorie += int(line)

print("first solution:", max(calories))
print("second solution:", sum(sorted(calories)[-3:]))
