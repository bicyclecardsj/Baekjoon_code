N = int(input())
reward_list = []

for _ in range(N):
    dice = list(map(int, input().split()))

    if dice[0] == dice[1] == dice[2]:
        reward = 10000 + dice[0] * 1000
    elif dice[0] == dice[1] or dice[0] == dice[2]:
        reward = 1000 + dice[0] * 100
    elif dice[1] == dice[2]:
        reward = 1000 + dice[1] * 100
    else:
        reward = max(dice) * 100
        
    reward_list.append(reward)

print(max(reward_list))