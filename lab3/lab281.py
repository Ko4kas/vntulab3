n = int(input())

previous = 0
current = 1
position = 1

while current < n:
    previous, current = current, previous + current
    position += 1

if current == n:
    print(position)
else:
    print(-1)