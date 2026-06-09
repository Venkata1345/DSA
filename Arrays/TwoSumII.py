nums = [-1,0]
l=0
target = -1
r = len(nums)-1
while l<=r:
    curr_sum = nums[l]++nums[r]
    if curr_sum==target:
        break
    elif curr_sum > target:
        r-=1
    else:
        l+=1
print(l+1,r+1)
