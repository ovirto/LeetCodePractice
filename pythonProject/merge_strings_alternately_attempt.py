# Final Time Complexity: O(Max(N,M))

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_string = ""
        i = 0

        if (len(word1) > len(word2)):

            while i < len(word2):
                new_string += str(word1[i])
                new_string += str(word2[i])
                i += 1

            while i < len(word1):
                new_string += str(word1[i])
                i += 1

        elif (len(word1) < len(word2)):

            while i < len(word1):
                new_string += str(word1[i])
                new_string += str(word2[i])
                i += 1

            while i < len(word2):
                new_string += str(word2[i])
                i += 1

        else:
            # same length words
            while i < len(word1):
                new_string += str(word1[i])
                new_string += str(word2[i])
                i += 1

        return new_string

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