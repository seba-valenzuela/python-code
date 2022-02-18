# This works the SAME WAY with STRINGS as it does LISTS

nums = [1, 2, 3, 4, 5]
string = 'abcde'

print(nums[1:4])     # [2, 3, 4]   (start at 0, stop before 4)
print(string[1:4])   # bcd
nums[2:]      # [3, 4, 5]   (start at 0, stop at end of list)
nums[:3]      # [1, 2, 3]   (start at 0, stop before 3)
nums[1:4:2]   # [2, 4]      (start at 1, stop before 4, every 2nd element)
nums[2::2]    # [3, 5]      (start at 2, stop at end of list, every 2nd element)
nums[:3:2]    # [1, 3]      (start at 0, stop before 3, every 2nd element)
nums[::2]     # [1, 3, 5]   (start at 0, stop at end of list, every 2nd element)
nums[::]      # [1, 2, 3, 4, 5] (start at 0, stop at end of list)

