Problem: Given an integer numRows, return the first numRows of Pascal's triangle.


Solution>Python3
class Solution:
  def generate(self, n: int) -> List[List[int]]:
    return list(accumulate([[1]]*n, lambda a,b: [x+y for x,y in zip(a+[0],[0]+a)]))
  
