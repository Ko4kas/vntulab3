n = int(input())
lost_card = n * (n + 1) // 2

for _ in range(n - 1):
    card = int(input())
    lost_card -= card

print(lost_card)