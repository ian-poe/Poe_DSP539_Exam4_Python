import sys

def read_genome_file(file_path):                                                                #Function to Convert a Genome in a File Format to a String to Evaluate
    """
    Reads genome sequence data from a file and returns it as a single string.

    The file should contain the genome sequence of a single organism.
    This function removes newline characters and extra spaces to return a clean sequence.

    Arguments:
        file_path : Path to the genome file.

    Returns:
        The genome sequence as a single continuous string.
    """
    with open(file_path, "r") as file:                                                         #Opens File in Read Mode
        return file.read().replace("\n", "").strip()                                           #Reads File and Removes newlines any extra spaces

def identify_genomes(s, k):                                                                    #Function to Idenfity the List of Genome Substrings of Length k
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
    return [s[i:i + k] for i in range(len(s) - k + 1)]                                        #Generates the List of Genome Substring and ensure all entrys are length K

def count_total_genomes(s, k):                                                                #Function for Frequency of Genomes in the List
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
    total_counts = {}                                                                        #Empty dictionary to Store Total Count or Each Unique Genome Substring
    for i in range(len(s) - k + 1):                                                          #For Loop to cycle through each genome substring of length k
        original_substring = s[i:i + k]                                                      #Identifys Spicific substring for the loop

        if original_substring not in total_counts:                                           #If Substring Not in the dictionary "total_counts"             
            total_counts[original_substring] = 0                                             #It is added with a value of 0
            
        total_counts[original_substring] += 1                                                #1 is added to the substring count for the specific substring
    return total_counts                                                                      #Returns the Dictionary after the string is completed

def next_genomes(s, k):                                                                      #Function to create a list of next genomes seen
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

    return [s[i+1:i + k +1] for i in range(len(s) - k)]                                     #Generates the List of Next Genome Substring and ensure all entrys are length K

def count_next_genomes(s, k):                                                               # Function for Frequency of Next Genomes seen for each unique genome
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
    next_genome = {}                                                            #Empty Dictionary For Frequency of Next Genomes
    total_counts = count_total_genomes(s, k)                                    #Saved Total Count Dictionary as a Variable from the Previous Function
    for i in range(len(s) - k):                                                 #For Loop to cycle through each genome substring of length k not including final subset
        original_substring = s[i:i + k]
        next_char = s[i + k]                                                    #Identify the Character Which Follows the Subset
        new_substring = original_substring[1:] + next_char                      #Creates a New Substring be removing the first value in the original and adding the next character

        if original_substring not in next_genome:                               #If original substring not in dictionary "next_genome" 
            next_genome[original_substring] = {}                                #Substring Added with an Empty Dictionary

        next_genome[original_substring][new_substring] = next_genome[original_substring].get(new_substring, 0) + 1 #Tracks the Frequency of Next Genome for Each Unique Genome Subset from the string
    return next_genome, total_counts                                            #Returns both Dictionarys for Frequency Total and Frequency Next Genome

def check_edge_values(s, k):                                                    #Used in pytest to ensure last substring is as expected only consisting of the last k values
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
    return s[-k:]                                                                                #Last substring of the sequence

def write_output(output, total_counts, output_file_name):                                        #Function to Write The Results to A Document
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
    with open(output_file_name, "w") as out_file:                                             #Open a New File in Write Mode
        for key, value in output.items():                                                     #Loop through each unique genome substring
            total_frequency = total_counts[key]                                               #Identify the total frequency which corresponds
            out_file.write("{} : {}: {}\n".format(key, total_frequency, value))               #Format Final Result by Genome SUbstring: Total Occurance : Freqencys of Next Genome
            
def main():                                                                                   #Main Code for the "predict_genome.py" file to run all functions
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
    file_path = sys.argv[1]                                                                  #Command-Line Input 1: Path to Genome Data
    k = int(sys.argv[2])                                                                     #Command-Line Input 2: Length of subsets
    output_file_name = sys.argv[3]                                                           #Command-Line Input 3: Name of Output File

    genome_string = read_genome_file(file_path)                                              #Use "read_genome_file" to convert file into a string
    output, total_counts = count_next_genomes(genome_string, k)                              #Use count_next_genomes and count_total_genomes to obtain total and next frequencys
    write_output(output, total_counts, output_file_name)                                     #Use "write_output" to generated a formated document of the results

    print("Output saved to {}".format(output_file_name))                                     #Prints a conformation statement to know program ran and where data is saved

if __name__ == "__main__":                                                                   #Identifys this Function to python as the Main Function for the code
    main()