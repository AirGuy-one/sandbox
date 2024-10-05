def house_robber(nums):
    if len(nums) < 3:
        return max(nums)

    nums[2] = max(nums[2] + nums[0], nums[1])

    if len(nums) > 3:
        for i in range(3, len(nums)):
            nums[i] = max(nums[i] + nums[i - 3], nums[i] + nums[i - 2], nums[i - 1])

    return nums[-1]


numbers = [1, 2, 3, 1]
response = house_robber(numbers)

print(response)
