class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        def reverse_array(arr):
            left, right = 0, len(arr) - 1
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1

        n=len(matrix)

        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

        for i in range(n):
            reverse_array(matrix[i])


        
        