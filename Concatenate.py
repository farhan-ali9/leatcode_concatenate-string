#first solution 
class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums1=nums[:]
        nums.extend(nums1)
        return nums




#second solution


class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums1=nums[:]
        return nums1+nums
