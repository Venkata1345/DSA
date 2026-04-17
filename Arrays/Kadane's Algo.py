nums = list(map(int, input().split()))
max_tillnow =0
sm=0
for i in range(len(nums)):
    sm+=nums[i]
    if sm>max_tillnow:
        max_tillnow = sm
    if sm<0:
        sm=0
print(max_tillnow)
