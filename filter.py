data = [
    [100, 110, 120],
    [400, 500, 600],
    [170, 180, 190]
]
list = []

for row in data:
    for item in row:
        if item > 190:
            list.append(item)

print(list)