daily_distance = float(input())
target = float(input())

total = 0
days = 0

while total <= target:
    total += daily_distance
    days += 1
    daily_distance *= 1.1

print(f"{total:.2f} km, {days} days")