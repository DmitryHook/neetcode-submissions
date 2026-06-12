class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        len1, len2 = len(nums1), len(nums2)
        half_len = (len1 + len2 + 1) // 2

        left, right = 0, len1

        while left <= right:
            mid1 = (left + right) // 2
            mid2 = half_len - mid1

            left_max1 = nums1[mid1 - 1] if mid1 > 0 else -float('inf')
            right_min1 = nums1[mid1] if mid1 < len1 else float('inf')

            left_max2 = nums2[mid2 - 1] if mid2 > 0 else -float('inf')
            right_min2 = nums2[mid2] if mid2 < len2 else float('inf')

            if left_max1 <= right_min2 and left_max2 <= right_min1:
                if (len1 + len2) % 2 == 1:
                    return float(max(left_max1, left_max2))
                else:
                    return (max(left_max1, left_max2) + min(right_min1, right_min2)) / 2.0

            elif left_max1 > right_min2:
                right = mid1 - 1
            else:
                left = mid1 + 1

        return 0.0