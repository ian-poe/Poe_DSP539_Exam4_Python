import pytest                                                                            #Import pytest for testing
from predict_genome import (read_genome_file, identify_genomes, count_total_genomes,     #Import Functions to Test
                           next_genomes, count_next_genomes, check_edge_values)

# Sample genome sequence for testing

sample_genome_1 = "ATGTCTGTCTGAA"                                                        #Length 13
sample_genome_2 = "ATGTCTGTCTGAACTGTCT"                                                  #Length 19
sample_genome_3 = "A"                                                                    #Edge Case:Length 1 no output expected
sample_genome_4 = "AT"                                                                   #Edge Case:Length 2 no next genome expected
sample_genome_5 = "ATG"                                                                  #Edge Case:Length 2 genome substrings, 1 next expected
k_2 = 2                                                                                  #Testing Substring Length 2
k_3 = 3                                                                                  #Testing Substring Length 3

def test_read_genome_files():                                                            #Function to test read_genome_files
    """
    Test read_genome_files function.
    
    This Function Test two scenarios where the data is in a file format. 
    The first found in "exam4_example1.txt" has data on a single line.
    The second found in "exam4_textdata2" had data on mutiple Lines.
    
    The expected strings are used to check to ensure the outcomes of the function are the expected results. 
    The Expected outcomes are seen as variables exp_file_1 and exp_file_2. 
    """
    #Expected Result From First DataFile
    exp_file_1 = "ATGTCTGTCTGAA" 
    #Expected Result From Second DataFile
    exp_file_2 = "GAAATTCTCGTAAATTCTCTCAAATTCTCTGAAATTCTCTTAAATTCTGACAAATTCTGAGAAATTCTGATAAATTCTGCCAAATTCTGCGAAATTCTGCTAAATTCTGGCAAATTCTGGGAAATTCTGGTAAATTCTGTCAAATTCTGTTAAGGGCATTCAAGGGCATTGAAGGGCATTTAAGGGCCAATAAGGGCCACCAAGGGCCACGAAGGGCCACTAAGGGCCAGCAAGGGCCAGGAAGGGCCAGTAAGGGCCATCAAGGGCCATGAAGGGCCATTAAGGGCCCACAAGGGCCCATAAGGGGTGTCAAGGGGTGTGAAGGGGTGTTAAGGGGTTACAAGGGGTTAGAAGGGGTTATAAGGGGTTCCAAGGGGTTCGAAGGGGTTCTAAGGGGTTGCAAGGGGTTGGAAGGGGTTGTAAGGGGTTTCAAGGGGTTTGAAGGGGTTTTTGCATATACTTGCATCCACTTGCATCGACTTGCATCTACTTGCATGCACTTGCATGGACTTGCATGTACTTGCATTCACTTGCATTGACTTGCATTTACTTGCCAGCACTTGCCAGGACTTGCCAGTACTTGCCATCACTTGCCATGACTATGGTGATATATGGTTATATATGTCCATATATGTCGATATATGTCTATATATGTGCATATATGTGGATATATGTGTATATATGTTCATATATGTTGATATATGTTTATATATTATCATATATTATGATATATTATTATATATTCCCATATCCCGCAAAGTCCCGGAAAGTCCCGTAAAGTCCCTCAAAGTCCCTGAAAGTCCCTTAAAGTCCGACAAAGTCCGAGAAAGTCCGATAAAGTCCGCCAAAGTCCGCGAAAGTCCGCTAAAGTCCGGCAAAGTCCGGGAAAGTCCGGTAAAGCCCGAGAATACCCGATAATACCCGCCAATACCCGCGAATACCCGCTAATACCCGGCAATACCCGGGAATACCCGGTAATACCCGTCAATACCCGTGAATACCCGTTAATACCCTACAATACCCTAGAATACCCTATAATACCCTCCAATA"
    
    assert read_genome_file("exam4_example1.txt") == exp_file_1 # Test to See if Results For File 1 is the Same
    assert read_genome_file("exam4_textdata2") == exp_file_2    # Test to See if Results For File 2 is the Same
    
    
def test_identify_genomes():                                    #Test to Check Function identify_genomes()
    """
    Test identify_genomes function.
    
    This Function Test 5 diffrent string.
    The first 2 represent real data to see if the write results are obtained.
    Each is done twice one for k = 2 and one for k=3.
    The use of small string allowed for the diffrent combinations to be found by hand and checked to ensure function is correct
    
    Edge Cases: String 3-5 where tested 
    String 3 (length1) expected result was empty
    String 4 (length2) expected result was "AT"
    String 5 (Length3) expected result was "AT", "TG"
    
    All string expected where found by hand and checked to the function output
    """
    #Expected Output String 1, k=3
    expected_3_1 = ["ATG", "TGT", "GTC", "TCT", "CTG", "TGT", "GTC", "TCT", "CTG", "TGA", "GAA"]
    #Expected Output String 2, k=3
    expected_3_2 = ["ATG", "TGT", "GTC", "TCT", "CTG", "TGT", "GTC", "TCT", "CTG", "TGA", "GAA", "AAC", "ACT", "CTG", "TGT", "GTC", "TCT"]
    #Expected Output String 1, k=2
    expected_2_1 = ["AT", "TG", "GT", "TC", "CT", "TG", "GT", "TC", "CT", "TG", "GA", "AA"]
    #Expected Output String 2, k=2
    expected_2_2 = ["AT", "TG", "GT", "TC", "CT", "TG", "GT", "TC", "CT", "TG", "GA", "AA", "AC", "CT", "TG", "GT", "TC", "CT"]
    #Expected Output String 3, k=3
    expected_3 = []
    #Expected Output String 4, k=2
    expected_4 = ["AT"]
    #Expected Output String 5, k=2
    expected_5 = ["AT", "TG"]
    assert identify_genomes(sample_genome_1, k_2) == expected_2_1     # Test to See if Results For String 1, k=2 is the Same
    assert identify_genomes(sample_genome_1, k_3) == expected_3_1     # Test to See if Results For String 1, k=3 is the Same
    assert identify_genomes(sample_genome_2, k_2) == expected_2_2     # Test to See if Results For String 2, k=2 is the Same
    assert identify_genomes(sample_genome_2, k_3) == expected_3_2     # Test to See if Results For String 2, k=3 is the Same
    assert identify_genomes(sample_genome_3, k_3) == expected_3       # Test to See if Results For String 3, k=3 is the Same
    assert identify_genomes(sample_genome_4, k_2) == expected_4       # Test to See if Results For String 4, k=2 is the Same
    assert identify_genomes(sample_genome_5, k_2) == expected_5       # Test to See if Results For String 5, k=2 is the Same
    
def test_count_total_genomes():
    """
    Test count_total_genomes function.
    
    This Function Test 5 the five diffrent string difined above.
    The first 2 represent real data to see if the write results are obtained.
    Each is done twice one for k = 2 and one for k=3.
    The use of small string allowed for the count of diffrent unique substring to be found by hand and checked to ensure function is correct
    
    Edge Cases: String 3-5 where tested 
    String 3 (length1) expected result was empty
    String 4 (length2) expected result was {"AT":1}
    String 5 (Length3) expected result was {"AT": 1, "TG": 1}
    
    All frequencys where found by hand and checked to the function output
    """
    #Expected Output String 1, k=2
    expected_2_1 = {"AT": 1, "TG": 3, "GT": 2, "TC": 2, "CT": 2, "GA": 1, "AA": 1}
     #Expected Output String 1, k=3
    expected_3_1 = {"ATG": 1, "TGT": 2, "GTC": 2, "TCT": 2, "CTG": 2, "TGA": 1, "GAA": 1}
     #Expected Output String 2, k=2
    expected_2_2 = {"AT": 1, "TG": 4, "GT": 3, "TC": 3, "CT": 4, "GA": 1, "AA": 1, "AC": 1}
     #Expected Output String 2, k=3
    expected_3_2 = {"ATG": 1, "TGT": 3, "GTC": 3, "TCT": 3, "CTG": 3, "TGA": 1, "GAA": 1, "AAC": 1, "ACT": 1}
     #Expected Output String 3, k=3
    expected_3 = {}
     #Expected Output String 4, k=2
    expected_4 = {"AT": 1}
     #Expected Output String 5, k=2
    expected_5 = {"AT": 1, "TG": 1}
    assert count_total_genomes(sample_genome_1, k_2) == expected_2_1  # Test to See if Results For String 1, k=2 is the Same
    assert count_total_genomes(sample_genome_1, k_3) == expected_3_1  # Test to See if Results For String 1, k=3 is the Same
    assert count_total_genomes(sample_genome_2, k_2) == expected_2_2  # Test to See if Results For String 2, k=2 is the Same
    assert count_total_genomes(sample_genome_2, k_3) == expected_3_2  # Test to See if Results For String 2, k=3 is the Same
    assert count_total_genomes(sample_genome_3, k_3) == expected_3    # Test to See if Results For String 3, k=3 is the Same
    assert count_total_genomes(sample_genome_4, k_2) == expected_4    # Test to See if Results For String 4, k=2 is the Same
    assert count_total_genomes(sample_genome_5, k_2) == expected_5    # Test to See if Results For String 5, k=2 is the Same
    
def test_next_genomes():
    """
    Test next_genomes function.
    
    This Function Test 5 the five diffrent string difined above.
    The first 2 represent real data to see if the write results are obtained.
    Each is done twice one for k = 2 and one for k=3.
    The use of small string allowed for the for the list of next substring to be found by hand and checked to ensure function is correct
    
    Edge Cases: String 3-5 where tested 
    String 3 (length1) expected result was empty
    String 4 (length2) expected result was empty
    String 5 (Length3) expected result was "TG"
    
    All frequencys where found by hand and checked to the function output
    """
    #Expected Output String 1, k=2
    expected_2_1 = ["TG", "GT", "TC", "CT", "TG", "GT", "TC", "CT", "TG", "GA", "AA"]
    #Expected Output String 1, k=3
    expected_3_1 = ["TGT", "GTC", "TCT", "CTG", "TGT", "GTC", "TCT", "CTG", "TGA", "GAA"]
    #Expected Output String 2, k=2
    expected_2_2 = ["TG", "GT", "TC", "CT", "TG", "GT", "TC", "CT", "TG", "GA", "AA", "AC", "CT", "TG", "GT", "TC", "CT"]
    #Expected Output String 2, k=3
    expected_3_2 = ["TGT", "GTC", "TCT", "CTG", "TGT", "GTC", "TCT", "CTG", "TGA", "GAA", "AAC", "ACT", "CTG", "TGT", "GTC", "TCT"]
    #Expected Output String 3, k=3
    expected_3 = []
    #Expected Output String 4, k=2
    expected_4 = []
    #Expected Output String 5, k=2
    expected_5 = ["TG"]
    assert next_genomes(sample_genome_1, k_2) == expected_2_1 # Test to See if Results For String 1, k=2 is the Same
    assert next_genomes(sample_genome_1, k_3) == expected_3_1 # Test to See if Results For String 1, k=3 is the Same
    assert next_genomes(sample_genome_2, k_2) == expected_2_2 # Test to See if Results For String 2, k=2 is the Same
    assert next_genomes(sample_genome_2, k_3) == expected_3_2 # Test to See if Results For String 2, k=3 is the Same
    assert next_genomes(sample_genome_3, k_3) == expected_3   # Test to See if Results For String 3, k=3 is the Same
    assert next_genomes(sample_genome_4, k_2) == expected_4   # Test to See if Results For String 4, k=2 is the Same
    assert next_genomes(sample_genome_5, k_2) == expected_5   # Test to See if Results For String 5, k=2 is the Same
    
def test_count_next_genomes():
    """
    Test count_next_genomes function.
    
    This Function Test 5 the five diffrent string difined above.
    The first 2 represent real data to see if the write results are obtained.
    Each is done twice one for k = 2 and one for k=3.
    The use of small string allowed for the for the frequency of next substring to be found by hand  for each uniqe genome and checked to ensure     function is correct. This function outputs two outputs the total and next frequencys. Total frequencys where checked above so this function     is only testing the next genomes frequency. This is done by looking at count_next_genomes[0]
    
    Edge Cases: String 3-5 where tested 
    String 3 (length1) expected result was {}
    String 4 (length2) expected result was {}
    String 5 (Length3) expected result was {'AT': {'TG': 1}}
    
    All frequencys where found by hand and checked to the function output
    """
    #Expected Output String 1, k=3
    expected_3_1 = {
     'ATG': {'TGT': 1},
     'TGT': {'GTC': 2},
     'GTC': {'TCT': 2},
     'TCT': {'CTG': 2},
     'CTG': {'TGT': 1, 'TGA': 1},
     'TGA': {'GAA': 1}}
    #Expected Output String 1, k=2
    expected_2_1 = {
      'AT': {'TG': 1},
      'TG': {'GT': 2, 'GA': 1},
      'GT': {'TC': 2},
      'TC': {'CT': 2},
      'CT': {'TG': 2},
      'GA': {'AA': 1}}
    #Expected Output String 2, k=3
    expected_3_2 = {
    'ATG': {'TGT': 1},
    'TGT': {'GTC': 3},
    'GTC': {'TCT': 3},
    'TCT': {'CTG': 2},
    'CTG': {'TGT': 2, 'TGA': 1},
    'TGA': {'GAA': 1},
    'GAA': {'AAC': 1},
    'AAC': {'ACT': 1},
    'ACT': {'CTG': 1}}
    #Expected Output String 2, k=2
    expected_2_2 = {
     'AT': {'TG': 1},
     'TG': {'GT': 3, 'GA': 1},
     'GT': {'TC': 3},
     'TC': {'CT': 3},
     'CT': {'TG': 3},
     'GA': {'AA': 1},
     'AA': {'AC': 1},
     'AC': {'CT': 1}}
    #Expected Output String 3, k=3
    expected_3 = {}
    #Expected Output String 4, k=2
    expected_4 = {}
    #Expected Output String 5, k=3
    expected_5 = {'AT': {'TG': 1}}
    
    assert count_next_genomes(sample_genome_1, k_2)[0] == expected_2_1 # Test to See if Results For String 1, k=2 is the Same
    assert count_next_genomes(sample_genome_1, k_3)[0] == expected_3_1 # Test to See if Results For String 1, k=3 is the Same
    assert count_next_genomes(sample_genome_2, k_2)[0] == expected_2_2 # Test to See if Results For String 2, k=2 is the Same
    assert count_next_genomes(sample_genome_2, k_3)[0] == expected_3_2 # Test to See if Results For String 2, k=3 is the Same
    assert count_next_genomes(sample_genome_3, k_3)[0] == expected_3   # Test to See if Results For String 3, k=3 is the Same
    assert count_next_genomes(sample_genome_4, k_2)[0] == expected_4   # Test to See if Results For String 4, k=2 is the Same
    assert count_next_genomes(sample_genome_5, k_2)[0] == expected_5   # Test to See if Results For String 5, k=2 is the Same
    
def test_check_edge_values():
    """
    Test check_edge_values function.
    
    This function is used to check the last output of the substring to ensure it is doing what is expected.
    The last substring was identified manualy and its values where placed into variables.
    Checking to ensure that even with diffrent lengths of starting string and diffrent k the correct last substring is determined
    """
    #Expected output string 1, k=2
    expected_2_1 = "AA"
    #Expected output string 1, k=3
    expected_3_1 = "GAA"
    #Expected output string 2, k=2
    expected_2_2 = "CT"
    #Expected output string 2, k=3
    expected_3_2 = "TCT"
    assert check_edge_values(sample_genome_1, k_2) == expected_2_1 # Test to See if Results For String 1, k=2 is the Same
    assert check_edge_values(sample_genome_1, k_3) == expected_3_1 # Test to See if Results For String 1, k=3 is the Same
    assert check_edge_values(sample_genome_2, k_2) == expected_2_2 # Test to See if Results For String 2, k=2 is the Same
    assert check_edge_values(sample_genome_2, k_3) == expected_3_2 # Test to See if Results For String 2, k=3 is the Same