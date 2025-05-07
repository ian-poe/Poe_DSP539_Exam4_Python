## Exam 4 - Python
## DSP 539
## Author - Ian Poe


### Exam 4 Results OverView

The function "predict_genome.py" is a combination of seven smaller functions which can be tested individually and one main function which controls the entire program. This document will discuss the format of how the final data is outputted along with how the program was tested to ensure accuracy. There are three main parts that will be discussed in this document. The first is how the data is structured in the final outputted document. The Second is how to ensure the program is handling edge cases properly. The Final thing to be discussed is how the code avoids overcounting or missing context. These three questions will be answered below. 

1. An explanation of the data structures you used to store k-mers and their context

The function "write_output" controls the outputted file and how the content is formatted. It uses the results obtained from both functions "count_next_genomes" and "count_total_genomes" in order to combine the information into the formatted result. The output document is formatted so each row consist of a different unique genome substring. The length of this substring will change with the value of k. Directly next to the substring of interest is the frequency in the full genome string. This is followed by the frequencies of the following genome. The Next Genome is a List of all the genomes which follows the genome of interest respectively. The frequency of these next genomes are printed with it. A row of data for will look like the following for k=3: 

CTT : 246334: {'TTC': 61664, 'TTA': 61520, 'TTG': 61430, 'TTT': 61720}

The first position is the unique genome substring or interest. 

The second position is how many times the unique substring it was seen in the full dataset.

The third position is the next genome substring which follows it and how many times that each of them followed the Unique Genome "CTT".


2. Your thoughts on handling edge cases (e.g., first and last k-mer in a sequence)?

In order to handle the edge cases for the first and last k-mer in a sequence, small test cases and test cases with different lengths of strings were used. In the test code, "exam4_test.py", three different small-scale test strings were used: sample_genome_3 = "A", sample_genome_4 = "AT", sample_genome_5 = "ATG". A string with length 1 was tested. Using k=2 value, the function was tested to ensure that no values were obtained for this genome substring. This is done to ensure that when the substring is out of bounds of the specified length, it is not included in the list of genome substring found. During testing, no output was obtained, which was the expected result. This conforms that the code is only operating for substring of length k. Next, a string of length 2 was tested with k=2 value. This was to ensure that the value appeared on the genome substring list, however since the length is also 2, we expect no value to be obtained for next genome substring. This was tested and found that it identified the original substring so the total count would increase however since no values are after it will not add any value for the next genome substring. This was the expected result. Finally, a string of length 3 was tested with k=2 value to ensure that two genome subsets where found and one next genome subset was obtained. By checking the these three substring, we can ensure that the correct first and last k-mer are correctly identified in the sequence. 

3. An explanation of how your code avoids overcounting or missing context

The code avoids overcounting by testing larger substring against the function. In the test code "exam4_test.py" the strings (sample_genome_1 = "ATGTCTGT CTGAA" and sample_genome_2 = "ATGTCTGTCTGAACTGTCT") was used to test how the code accuracy in counting both the total frequency and the frequency of the text genomes. The total count for each k-mer in the sequence where found and count for the next k-mer was determined by hand. These hand calculations where checked against the results obtained in the function. (Note: The Count of all next k-mer for a specific k-mer are equal to each other unless it is the last k-mer in the sequence then total is one more than the sum of all next k-mer. This was checked for two different string of different length (13 and 19). For each of these strings, it was tested for a k value of 2 and a k value of 3. This ensures that the function can keep count if the length of the original string and the size of the subsets are changed. The test shows that the expected values are observed by the function which shows that the code avoids overcounting and that the missing content (shown by the last k-mer) doesnt affect the results. Additionally the function "test_read_genome_files" is used to import the initial datafiles. This function was tested to ensure that a single continuous string is outputted without spaces or linebreakes. Additionally a test was conducted to see if a space in the the middle of the string was removed correctly. The function treats this space as a mistake and removes it. 

The test code "exam4_test.py"  test six different test and all are passed. Each test is checking multiple outputs.