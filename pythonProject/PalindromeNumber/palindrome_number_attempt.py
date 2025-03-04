# Final time complexity: O(n)
class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        start = 0
        end = len(str_x) - 1  # last index will start at length - 1

        while start < end:
            if str_x[start] != str_x[end]:  # mismatch found
                return False
            start += 1
            end -= 1

        return True  # loop completed, palindrome


# GPT Generated main method
def main():
    solution = Solution()

    # Test cases
    test_cases = [
        (121, True),  # Palindrome
        (-121, False),  # Negative number, not a palindrome
        (10, False),  # Not a palindrome
        (0, True),  # Single digit, always a palindrome
        (1221, True),  # Even-length palindrome
        (12321, True),  # Odd-length palindrome
        (1001, True),  # Palindrome with zeros
        (123456, False)  # Not a palindrome
    ]

    for x, expected in test_cases:
        result = solution.isPalindrome(x)
        print(f'isPalindrome({x}) -> {result}, Expected: {expected}, {"✅" if result == expected else "❌"}')


if __name__ == "__main__":
    main()