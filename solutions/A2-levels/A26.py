n = int(input().strip())
scores = [int(input().strip()) for _ in range(n)]

count = {}

for score in scores:
    if score in count:
        count[score] += 1
    else:
        count[score] = 1

max_score = max(scores)

print(max_score)
print(count[max_score])