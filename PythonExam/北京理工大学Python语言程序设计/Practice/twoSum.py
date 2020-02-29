nums = [2,11,7,15]
target = eval(input())

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if target == nums[i] + nums[j]:
                # return [i, j]
                print(i, j)
            else:
                print('No Result.')

# def twoSum(nums, target):
#     lens = len(nums)
#     j=-1
#     for i in range(1,lens):
#         temp = nums[:i]
#         if (target - nums[i]) in temp:
#             j = temp.index(target - nums[i])
#             break
#     if j>=0:
#         return [j,i]
#         print(i, j)

twoSum(nums,target)
