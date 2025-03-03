# Source: https://www.youtube.com/watch?v=itdnQKDGWIQ&t=48s
# Final Time Complexity: O(m+n)

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []

        for a,b in zip(word1, word2):
            merged.append(a+b)

        merged.append(word1[len(word2):])
        merged.append(word2[len(word2):])

        return "".join(merged)

# GPT Generated main method
def main():
    solution = Solution()

    # Test cases
    test_cases = [
        ("abc", "pqr"),  # Same length
        ("ab", "pqrs"),  # word2 is longer
        ("abcd", "pq"),  # word1 is longer
        ("", "xyz"),  # word1 is empty
        ("abc", ""),  # word2 is empty
        ("a", "b"),  # Single-character words
        ("longword", "short")  # Different lengths
    ]

    for word1, word2 in test_cases:
        result = solution.mergeAlternately(word1, word2)
        print(f'mergeAlternately("{word1}", "{word2}") -> "{result}"')

if __name__ == "__main__":
    main()