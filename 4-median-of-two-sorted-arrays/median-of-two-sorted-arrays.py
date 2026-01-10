class Solution( object ):
    #! Use this integer values instead of float("-inf") and float("+inf") because comparing float and integer is slow !#
    MINUS_BIG = -2147483648 #! INT_MIN !#
    PLUS_BIG = +2147483647 #! INT_MAX !#
    def findMedianSortedArrays( self, nums1, nums2 ):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        low = 0
        high = len(nums1)
        half = (high + len(nums2) + 1) // 2
        while low <= high :
            index = (low + high) // 2
            jndex = half - index
            left1 = self.MINUS_BIG if index <= 0 else nums1[index - 1]
            right1 = self.PLUS_BIG if index >= len(nums1) else nums1[index]
            left2 = self.MINUS_BIG if jndex <= 0 else nums2[jndex - 1]
            right2 = self.PLUS_BIG if jndex >= len(nums2) else nums2[jndex]
            if left1 <= right2 and left2 <= right1 :
                if (len(nums1) + len(nums2)) % 2 == 1 :
                    return max(left1, left2)
                return (max(left1, left2) + min(right1, right2)) / 2.0
            elif left1 > right2 :
                high = index - 1
            else :
                low = index + 1
        raise Exception("Unreachable")