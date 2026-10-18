n = int(input())
total_speed = 0
exceeded = False

for _ in range(n):
    speed = int(input())
    total_speed += speed
    if speed > 60:
        exceeded = True

print(f"{total_speed / n:.1f}")
print("Yes" if exceeded else "No")