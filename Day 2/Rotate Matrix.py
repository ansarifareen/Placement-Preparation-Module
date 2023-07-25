Problem : ROTATE MATRIX 
Statement:  You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Solution in Python3:

import numpy as np
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix[:] = np.fliplr(np.transpose(matrix))



# Time Complexity: O(n^2)
# Space Complexity: O(1)
 
