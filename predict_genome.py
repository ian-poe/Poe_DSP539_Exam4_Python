import sys

def read_genome_file(file_path):
    """
    Reads genome sequence data from a file and returns it as a single string.

    The file should contain the genome sequence of a single organism.
    This function removes newline characters and extra spaces to return a clean sequence.

    Arguments:
        file_path : Path to the genome file.

    Returns:
        The genome sequence as a single continuous string.
    """
    with open(file_path, "r") as file:
        return file.read().replace("\n", "").strip()  # Removes newlines & extra spaces

def identify_genomes(s, k):
    """
    Extracts and returns a list of all genome substrings of length k.

    This function takes a string and identifies all possible contiguous substrings of length k. 
    It returns a list of genome substrings from the original genome

    Arguments:
        s : String of the Genome Sequence.
        k : Substring Length.

    Returns:
        A list of all contiguous substrings of length k from the input sequence.
    """
    return [s[i:i + k] for i in range(len(s) - k + 1)]

def count_total_genomes(s, k):
     """
    Extracts and returns a list of unique genome substrings with a count of how many times it was seen.

    This function takes a string and identifies all unique substrings of length k and a count of how many times it was seen. 
    It returns a list of unique genome substrings with a count for occurance for the original genome

    Arguments:
        s : String of the Genome Sequence.
        k : Substring Length.

    Returns:
        A list of unique substrings of length k with count for the input sequence.
    """
    total_counts = {}
    for i in range(len(s) - k + 1):
        original_substring = s[i:i + k]

        if original_substring not in total_counts:
            total_counts[original_substring] = 0  
            
        total_counts[original_substring] += 1 
    return total_counts

def next_genomes(s, k):
    """
        Extracts and returns a list of all next genome substrings of length k.

        This function takes a string and identifies all next genome substrings of length k. 
        It returns a list of next genome substrings for the original genome

        Arguments:
            s : String of the Genome Sequence.
            k : Substring Length.

        Returns:
            A list of all next genomes of length k from the input sequence.
        """
    return [s[i+1:i + k +1] for i in range(len(s) - k)]

def count_next_genomes(s, k):
    """
    Extracts and returns a list of unique genome substrings with the a count of how many times the next genome appears.

    This function takes a string and identifies all unique substrings of length k. 
    A count of how many times the next genome appears for each unique genome is created. 
    It returns a list of unique genome substrings with a frequency for next genome seen 

    Arguments:
        s : String of the Genome Sequence.
        k : Substring Length.

    Returns:
        A list of unique genome substrings with a count for which next genome is seen and how many times
    """
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
     """
    Checks to Ensure the last genome substring is what is expected

    This function is used in pytest to ensure that the final substring is what is expected. 
    It takes two inputs the genome string and the substring length.
    It returns the final substring 

    Arguments:
        s : String of the Genome Sequence.
        k : Substring Length.

    Returns:
        Final Substring of the Data
    """
    return s[-k:]  # Last characters of the sequence that may not form a valid substring

def write_output(output, total_counts, output_file_name):
   """
    Creates and Prints the results in a output file

    This function is used to create a new document containing the results. 
    It takes three inputs the outputs for frequency relative to each unique substring, the total count for each substring, and a name for the output file.
    It returns a text document named through the third input.

    Arguments:
        output : Frequency of Next Genomes for Each Unique Genome in the String 
        total_counts : Total COunt of how many times each unique Genome is Seen in the String
        output_file_name : name of the output file name

    Returns:
        Results in a Text Document
    """
    with open(output_file_name, "w") as out_file:
        for key, value in output.items():
            total_frequency = total_counts[key]
            out_file.write("{} : {}: {}\n".format(key, total_frequency, value))  
            
def main():
    """
    Main function to process genome data and generate predictions of next genomes.

    This function calls the previous function in order to obtain the final results. 
    This is the function that will run when the python code "predict_genome.py" is run. 
    This takes three command line inputs with the first being the file_path to the data, 
    second being the length of the substring, and third being the output file name.
    It returns the formated final results and a printed conformation to conform run/saved location.

    Command-line Arguments:
        file_path : Path to the genome file.
        k : Substring Length.
        output_file_name : Name of the output file to save final results.

    Outputs:
        Writes the results of next genome substrings and their frequencies for each unique genome to the specified output file.

    Prints:
        A confirmation message indicating the program was run and where the data is saved to.
    """
    file_path = sys.argv[1]  
    k = int(sys.argv[2])    
    output_file_name = sys.argv[3]  

    genome_string = read_genome_file(file_path)
    output, total_counts = count_next_genomes(genome_string, k)
    write_output(output, total_counts, output_file_name)

    print("Output saved to {}".format(output_file_name))

if __name__ == "__main__":
    main()