
def solve(nums,ans,index):
    if index >= len(nums):
        ans.append(nums[:])
        print(ans)
        return
    for j in range(index,len(nums)):
        nums[index],nums[j]=nums[j],nums[index]
        solve(nums,ans,index+1)
        nums[index],nums[j]=nums[j],nums[index]

def permutate():
    ans=[]
    index=0
    solve([1,2,3],ans,index)
    print(ans)
    return ans
    
permutate()