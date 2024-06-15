def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # iterative solution:

        low = 0
        high = len(nums) - 1

        while low <=high:
            
            # compute the middle index
            med = (low + high) // 2

            if nums[med] < target:
                low = med + 1
            elif nums[med] > target:
                high = med - 1
            
            else:
                return med
        return low
    
    
'''
TIME COMPLEXITY:
- Given an input size equal to n
- if target is in the middle index n//2 , then best scenarion takes O(1) comparison
- if target is at index n//4, or (n // 2 + n) // 2 = 3N//4, we neeed 2 comparisons


- think about it as a binary tree, where each node shows the points that can be compared for a given number of comparisons 
(at depth k if i draw a line i have all the node i can reach with k comparisons)

- to find the corrosponding indexes given the father:
for the left  son just divide by 2, to find the right son take the middle point index and sum the fatherindex and divide by 2


- basically given k comparison i get 2 ^ (k-1) elements that i can reach depending on the previous choices
- which is the max number of comparison i get get?
- the number of times n can be divided by 2 so that the result = 1 (n // 2 ^ k = 1 )
- then we get n = 2^l and so logn (basically, the number of comparison to reach the element at index 0)
'''