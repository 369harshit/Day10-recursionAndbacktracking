# Function to check if a string can be segmented into words
def word_break(s, word_dict):
    if s == "":
        return True

    # Iterate through the string and check if each prefix is a valid word
    for i in range(1, len(s) + 1):
        prefix = s[:i]
        if prefix in word_dict and word_break(s[i:], word_dict):
            return True

    return False


# Function to print all possible word break combinations
def print_word_break(s, word_dict):
    if not word_break(s, word_dict):
        print("String cannot be segmented into words.")
        return

    # Helper function to recursively find word break combinations
    def find_word_break_combinations(s, word_dict, result):
        if len(s) == 0:
            # All words have been formed, print the result
            print(' '.join(result))
            return

        # Iterate through the string and check if each prefix is a valid word
        for i in range(1, len(s) + 1):
            prefix = s[:i]
            if prefix in word_dict:
                # Add the prefix to the result and recursively process the remaining substring
                find_word_break_combinations(s[i:], word_dict, result + [prefix])

    # Start the recursion from an empty result and the given string
    find_word_break_combinations(s, word_dict, [])


# Example usage
word_dict = {"apple", "pen", "applepen", "pine", "pineapple"}
string = "pineapplepenapple"

print("All possible word break combinations:")
print_word_break(string, word_dict)
