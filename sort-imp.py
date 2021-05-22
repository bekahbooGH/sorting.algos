from random import random
nums = list(range(10))
random.shuffle(nums)

def is_sorted(nums: "list[int]") -> bool:
  for i in range(len(nums)-1):
    if nums[i+1] < nums[i]:
      return False
  return True

is_sorted(nums)

# def merge(nums1: List[int], nums2: List[int]) -> List[int]:
#   ret = []
#   while nums1 and nums2:
#     if nums1[0] < nums2[0]:
#       ret.append(nums1.pop(0))
#     else:
#       ret.append(nums2.pop(0))
#   while nums1 or nums2:
#     if nums1:
#       ret.append(nums1.pop(0))
#     else:
#       ret.append(nums2.pop(0))
#   return ret

# def merge(nums1: List[int], nums2: List[int]) -> List[int]:
#   ret = []
#   while nums1 or nums2:
#     if nums2 and (not nums1 or nums2[0] < nums1[0]):
#       ret.append(nums2.pop(0))
#     else:
#       ret.append(nums1.pop(0))
#   return ret

def merge_recursively(nums1: "list[int]", nums2: "list[int]") -> "list[int]":
  if not nums1:
    return nums2
  if not nums2:
    return nums1
  if nums1[0] > nums2[0]:
    return [nums2[0]] + merge_recursively(nums1, nums2[1:])
  else:
    return [nums1[0]] + merge_recursively(nums1[1:], nums2)

def merge_sort(nums: "list[int]") -> "list[int]":
  if len(nums) <= 1:
    return nums  # base case
  mid = len(nums) // 2
  nums1 = nums[:mid]
  nums2 = nums[mid:]
  nums1_sorted = merge_sort(nums1)  #  -> [2, 3, 4, 5, 7]
  nums2_sorted = merge_sort(nums2)  # -> [0, 1, 6, 8, 9]
  return merge_recursively(nums1_sorted, nums2_sorted)

print(nums)
merge_sort(nums)