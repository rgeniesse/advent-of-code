from itertools import takewhile

lines = ["68878   98739", "24519   87903", "87903   24519"]

x = next(
    (sum(abs(a - b) for a, b in zip(l, r)))
    for l, r in [
        map(sorted, zip(*map(lambda line: map(int, line.split("   ")), lines)))
    ]
)

test = map(sorted, zip(*map(lambda line: map(int, line.split("   ")), lines)))

print(list(test))

test2 = zip(*map(lambda line: map(int, line.split("   ")), lines))

print(list(test2))


test2 = lambda line: map(int, line.split("   "))

test3 = zip(*map(test2, lines))

print(list(test3))

print(*map(lambda line: map(int, line.split("   ")), lines))
print(map(lambda line: map(int, line.split("   ")), lines))
