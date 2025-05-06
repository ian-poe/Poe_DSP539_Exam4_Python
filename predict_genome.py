import sys

def read_genome_file(file_path):
    """
    Reads genome data from a file and returns it as a single string.
    File Sould Consist of A single Genome of A Organism
    """
    with open(file_path, "r") as file:
        return file.read().replace("\n", "").strip()  # Removes newlines & extra spaces

def identify_genomes(s, k):
    """Identifies and returns a list of all genome substrings of length k."""
    return [s[i:i + k] for i in range(len(s) - k + 1)]

def count_total_genomes(s, k):
    """Creates a dictionary tracking frequencies of next genome substrings."""
    total_counts = {}
    for i in range(len(s) - k + 1):
        original_substring = s[i:i + k]

        if original_substring not in total_counts:
            total_counts[original_substring] = 0  
            
        total_counts[original_substring] += 1 
    return total_counts

def next_genomes(s, k):
    """Identifys the List of Next Genom Subset"""
    return [s[i+1:i + k +1] for i in range(len(s) - k)]

def count_next_genomes(s, k):
    """Creates a dictionary tracking frequencies of next genome substrings."""
    next_genome = {}
    total_counts = count_total_genomes(s, k)  

    for i in range(len(s) - k):
        original_substring = s[i:i + k]
        next_char = s[i + k]
        new_substring = original_substring[1:] + next_char

        if original_substring not in next_genome:
            next_genome[original_substring] = {}

        next_genome[original_substring][new_substring] = next_genome[original_substring].get(new_substring, 0) + 1

    return next_genome, total_counts 

def check_edge_values(s, k):
    """Checks edge cases where sequences may not align properly."""
    return s[-k:]  # Last characters of the sequence that may not form a valid substring

def write_output(output, total_counts, output_file_name):
    """Writes genome substring predictions and frequencies to an output file."""
    with open(output_file_name, "w") as out_file:
        for key, value in output.items():
            total_frequency = total_counts[key]
            out_file.write("{} : {}: {}\n".format(key, total_frequency, value))  
            
def main():
    """Main function to run the genome prediction."""
    file_path = sys.argv[1]  
    k = int(sys.argv[2])    
    output_file_name = sys.argv[3]  

    genome_string = read_genome_file(file_path)
    output, total_counts = count_next_genomes(genome_string, k)
    write_output(output, total_counts, output_file_name)

    print("Output saved to {}".format(output_file_name))

if __name__ == "__main__":
    main()