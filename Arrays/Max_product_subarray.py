n = len(nums)
res = float('-inf')
pref =1 
suff =1 
for i in range(n):
    if pref==0:
        pref=1
    if suff ==0:
        suff=1
    
    pref*=nums[i]
    suff*=nums[n-i-1]
    res = max(res, max(pref,suff))
print(res)
