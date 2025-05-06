import pytest
from predict_genome import (read_genome_file, identify_genomes, count_total_genomes, 
                           next_genomes, count_next_genomes, check_edge_values)

# Sample genome sequence for testing
sample_genome_1 = "ATGTCTGTCTGAA"  #Length 13
sample_genome_2 = "ATGTCTGTCTGAACTGTCT" #Length 19
k_2 = 2
k_3 = 3
def test_identify_genomes():
    """Test identify_genomes function."""
    expected_3_1 = ["ATG", "TGT", "GTC", "TCT", "CTG", "TGT", "GTC", "TCT", "CTG", "TGA", "GAA"]
    expected_3_2 = ["ATG", "TGT", "GTC", "TCT", "CTG", "TGT", "GTC", "TCT", "CTG", "TGA", "GAA", "AAC", "ACT", "CTG", "TGT", "GTC", "TCT"]
    expected_2_1 = ["AT", "TG", "GT", "TC", "CT", "TG", "GT", "TC", "CT", "TG", "GA", "AA"]
    expected_2_2 = ["AT", "TG", "GT", "TC", "CT", "TG", "GT", "TC", "CT", "TG", "GA", "AA", "AC", "CT", "TG", "GT", "TC", "CT"]
    assert identify_genomes(sample_genome_1, k_2) == expected_2_1
    assert identify_genomes(sample_genome_1, k_3) == expected_3_1   
    assert identify_genomes(sample_genome_2, k_2) == expected_2_2
    assert identify_genomes(sample_genome_2, k_3) == expected_3_2
        
def test_count_total_genomes():
    """Test count_total_genomes function."""
    expected_2_1 = {"AT": 1, "TG": 3, "GT": 2, "TC": 2, "CT": 2, "GA": 1, "AA": 1}
    expected_3_1 = {"ATG": 1, "TGT": 2, "GTC": 2, "TCT": 2, "CTG": 2, "TGA": 1, "GAA": 1}
    expected_2_2 = {"AT": 1, "TG": 4, "GT": 3, "TC": 3, "CT": 4, "GA": 1, "AA": 1, "AC": 1}
    expected_3_2 = {"ATG": 1, "TGT": 3, "GTC": 3, "TCT": 3, "CTG": 3, "TGA": 1, "GAA": 1, "AAC": 1, "ACT": 1}

    assert count_total_genomes(sample_genome_1, k_2) == expected_2_1
    assert count_total_genomes(sample_genome_1, k_3) == expected_3_1
    assert count_total_genomes(sample_genome_2, k_2) == expected_2_2
    assert count_total_genomes(sample_genome_2, k_3) == expected_3_2

def test_next_genomes():
    """Test next_genomes function."""
    expected_2_1 = ["TG", "GT", "TC", "CT", "TG", "GT", "TC", "CT", "TG", "GA", "AA"]
    expected_3_1 = ["TGT", "GTC", "TCT", "CTG", "TGT", "GTC", "TCT", "CTG", "TGA", "GAA"]
    expected_2_2 = ["TG", "GT", "TC", "CT", "TG", "GT", "TC", "CT", "TG", "GA", "AA", "AC", "CT", "TG", "GT", "TC", "CT"]
    expected_3_2 = ["TGT", "GTC", "TCT", "CTG", "TGT", "GTC", "TCT", "CTG", "TGA", "GAA", "AAC", "ACT", "CTG", "TGT", "GTC", "TCT"]
    assert next_genomes(sample_genome_1, k_2) == expected_2_1
    assert next_genomes(sample_genome_1, k_3) == expected_3_1
    assert next_genomes(sample_genome_2, k_2) == expected_2_2
    assert next_genomes(sample_genome_2, k_3) == expected_3_2

def test_count_next_genomes():
    """Test count_next_genomes function."""
    expected_3_1 = {
     'ATG': {'TGT': 1},
     'TGT': {'GTC': 2},
     'GTC': {'TCT': 2},
     'TCT': {'CTG': 2},
     'CTG': {'TGT': 1, 'TGA': 1},
     'TGA': {'GAA': 1}}
    expected_2_1 = {
      'AT': {'TG': 1},
      'TG': {'GT': 2, 'GA': 1},
      'GT': {'TC': 2},
      'TC': {'CT': 2},
      'CT': {'TG': 2},
      'GA': {'AA': 1}}
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
    expected_2_2 = {
     'AT': {'TG': 1},
     'TG': {'GT': 3, 'GA': 1},
     'GT': {'TC': 3},
     'TC': {'CT': 3},
     'CT': {'TG': 3},
     'GA': {'AA': 1},
     'AA': {'AC': 1},
     'AC': {'CT': 1}}
    
    assert count_next_genomes(sample_genome_1, k_2)[0] == expected_2_1
    assert count_next_genomes(sample_genome_1, k_3)[0] == expected_3_1
    assert count_next_genomes(sample_genome_2, k_2)[0] == expected_2_2
    assert count_next_genomes(sample_genome_2, k_3)[0] == expected_3_2

def test_check_edge_values():
    """Test check_edge_values function."""
    expected_2_1 = "AA"
    expected_3_1 = "GAA"
    expected_2_2 = "CT"
    expected_3_2 = "TCT"
    assert check_edge_values(sample_genome_1, k_2) == expected_2_1
    assert check_edge_values(sample_genome_1, k_3) == expected_3_1
    assert check_edge_values(sample_genome_2, k_2) == expected_2_2
    assert check_edge_values(sample_genome_2, k_3) == expected_3_2