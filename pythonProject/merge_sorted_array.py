# Source: https://www.youtube.com/watch?v=TTWKBqG-6IU&t=27s

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do no return anything, modify nums1 in-place instead.
        """
        midx = m - 1
        nidx = n - 1
        right = m + n - 1

        while nidx >= 0:
            if midx >= 0 and nums1[midx] > nums2[nidx]:
                nums1[right] = nums1[midx]
                midx -= 1
            else:
                nums1[right] = nums2[nidx]
                nidx -= 1

            right -= 1


# GPT  Generated main class for testing
class Main:
    @staticmethod
    def test_solution():
        solution = Solution()

        # Test case 1
        nums1 = [1, 2, 3, 0, 0, 0]
        m = 3
        nums2 = [2, 5, 6]
        n = 3
        solution.merge(nums1, m, nums2, n)
        assert nums1 == [1, 2, 2, 3, 5, 6], f"Test case 1 failed: {nums1}"

        # Test case 2
        nums1 = [1]
        m = 1
        nums2 = []
        n = 0
        solution.merge(nums1, m, nums2, n)
        assert nums1 == [1], f"Test case 2 failed: {nums1}"

        # Test case 3
        nums1 = [0]
        m = 0
        nums2 = [1]
        n = 1
        solution.merge(nums1, m, nums2, n)
        assert nums1 == [1], f"Test case 3 failed: {nums1}"

        print("All test cases passed!")


if __name__ == "__main__":
    Main.test_solution()
