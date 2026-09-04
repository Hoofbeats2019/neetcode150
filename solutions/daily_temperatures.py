"""Daily Temperatures."""
from typing import List
class Solution:
 def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
  result=[0]*len(temperatures); stack=[]
  for day,temp in enumerate(temperatures):
   while stack and temperatures[stack[-1]]<temp:
    previous=stack.pop(); result[previous]=day-previous
   stack.append(day)
  return result
