import sys

def predicted_genome(s, k):
    next_genome = {}
    total_counts = {}  # Dictionary to track total occurrences for each substring

    for i in range(len(s) - k):  
        original_substring = s[i:i + k]  
        next_char = s[i + k]  
        new_substring = original_substring[1:] + next_char  

        if original_substring not in next_genome:
            next_genome[original_substring] = {}

        if original_substring not in total_counts:
            total_counts[original_substring] = 0  

        # Count Occurrences of the Next Combination Substring
        next_genome[original_substring][new_substring] = next_genome[original_substring].get(new_substring, 0) + 1
        total_counts[original_substring] += 1  # Increment total count

    return next_genome, total_counts

# Get command-line inputs
file_path = sys.argv[1]  
k = int(sys.argv[2])    
output_file_name = sys.argv[3]  

# Read data as a single string
with open(file_path, "r") as file:
    file_content = file.read().replace("\n", "").strip()  

# Run the function
output, total_counts = predicted_genome(file_content, k)

# Export to a text file
with open(output_file_name, "w") as out_file:
    for key, value in output.items():
        total_frequency = total_counts[key]  # Retrieve total frequency
        out_file.write("{} : {}: {}\n".format(key, total_frequency, value))  

print("Output saved to {}".format(output_file_name))  