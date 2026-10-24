
class Solution:
    def mergeArrays(self, nums1: list[list[int]], nums2: list[list[int]]) -> list[list[int]]:
        result = []
        first_index = 0
        second_index = 0

        while first_index < len(nums1) and second_index < len(nums2):
            first_id, first_value = nums1[first_index]
            second_id, second_value = nums2[second_index]

            if first_id == second_id:
                result.append([first_id, first_value + second_value])
                first_index += 1
                second_index += 1

            elif first_id < second_id:
                result.append([first_id, first_value])
                first_index += 1

            else:
                result.append([second_id, second_value])
                second_index += 1

        result.extend(nums1[first_index:])
        result.extend(nums2[second_index:])

        return result
