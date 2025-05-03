import sys
def predicted_genome(s, k):
    next_genome = {}
    for i in range(len(s) - k):  # Ensure there is a Next Genome for the Value Specified
        original_substring = s[i:i + k]  # Original Genome Substring
        next_char = s[i + k]  # Genome Next Term
        new_substring = original_substring[1:] + next_char  # Remove first character and adds next character

        # For Every Genome Combination Not Already Seen, a New Dictionary is Created
        if original_substring not in next_genome:
            next_genome[original_substring] = {}

        # Count Occurrences of the Next Combination Substring
        next_genome[original_substring][new_substring] = next_genome[original_substring].get(new_substring, 0) + 1

    return next_genome

# Get command-line inputs
file_path = sys.argv[1]  # Input 1: File name
k = int(sys.argv[2])     # Input 2: Convert to integer

# Read the file and clean the input
with open(file_path, "r") as file:
    file_content = file.read().strip()  # Removes extra whitespace/newlines

# Run the function and print results
print(predicted_genome(file_content, k))