# Source: https://www.youtube.com/watch?v=CijisxopxqM&t=42s
# Final time complexity: O(log x)
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        reverse = 0
        xcopy = x

        while x > 0:
            reverse = (reverse *10) + (x % 10)
            x //= 10

        return reverse == xcopy

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