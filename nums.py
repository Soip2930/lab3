import random
from random import randint

def find_missing_nums(nums):
  norm = [h for h in range(1, len(nums)+1)]
  a = []
  for d in norm:
    if d not in nums:
      a.append(d)
  return a

n = int(input())
nums = [randint(1, n) for i in range(n)]

print(find_missing_nums(nums))