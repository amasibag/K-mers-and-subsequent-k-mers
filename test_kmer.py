import pytest
from kmer import find_kmers, find_all_kmers, find_smallest_k

# Test find_kmers function
def test_find_kmers():

    # Test case: long sequence
    sequence = "ATGTCTGTCTGAA"
    k = 10
    try:
        find_kmers(sequence, k)
    except ValueError as e:
        assert str(e) == "Sequence length is shorter than k."
  
    # Test case: Short sequence
    sequence = "AT"
    k = 3
    try:
        find_kmers(sequence, k)
    except ValueError as e:
        assert str(e) == "Sequence length is shorter than k."

# Test find_all_kmers function

def test_find_all_kmers_short_sequence():
    # Test case: Short sequence
    filename = "test_sequences.txt"  # Replace with the actual filename
    k = 5
    try:
        find_all_kmers(filename, k)
    except ValueError as e:
        assert str(e) == "Sequence length is shorter than k."

def test_find_all_kmers_missing_file():
    # Test case: File not found
    filename = "nonexistent_file.txt"  # Replace with a non-existent filename
    try:
        find_all_kmers(filename, 2)
    except FileNotFoundError as e:
        assert str(e) == "File not found."


# Test find_smallest_k function
def test_find_smallest_k_valid_file():
    # Test case: Valid input file
    filename = "test_sequences.txt"  # Replace with the actual filename
    expected_result = 1  # Replace with the expected smallest value of k
    assert find_smallest_k(filename) == expected_result

def test_find_smallest_k_short_sequence():
    # Test case: Short sequence
    filename = "test_sequences.txt"  # Replace with the actual filename
    try:
        find_smallest_k(filename)
    except ValueError as e:
        assert str(e) == "Sequence length is shorter than k."

def test_find_smallest_k_missing_file():
    # Test case: File not found
    filename = "nonexistent_file.txt"  # Replace with a non-existent filename
    try:
        find_smallest_k(filename)
    except FileNotFoundError as e:
        assert str(e) == "File not found."


if __name__ == "__main__":
    pytest.main()

