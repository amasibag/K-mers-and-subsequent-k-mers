#!/usr/bin/env python 3

import argparse

#Define a function find_kmers that takes a DNA sequence sequence and an integer k as input 
#and returns a dictionary where keys are substrings of length k and values are sets of subsequent substrings.
def find_kmers(sequence, k):
    """
    Identify all substrings of size k and their subsequent substrings for a single sequence.

    Args:
    - sequence (str): The DNA sequence.
    - k (int): The size of the substrings.

    Returns:
    - dict: A dictionary where keys are substrings and values are sets of subsequent substrings.
    """
    if len(sequence) < k: 
         raise ValueError("Sequence length is shorter than k.")  #Raise a ValueError if the sequence is shorter than k.

    kmers = {}  # Initialize an empty dictionary to store the k-mers and their subsequent k-mers.
    for i in range(len(sequence) - k):  # Iterate over the sequence, up to the length minus k.
        kmer = sequence[i:i + k]  # Extract a substring of length k starting at position i.
        next_kmer = sequence[i + 1:i + k + 1]  # Extract the subsequent k-mer.
        if kmer not in kmers:  # Check if the k-mer is already in the dictionary.
            kmers[kmer] = set()  # If the k-mer is not in the dictionary, add it as a key with an empty set as its value.
        if len(next_kmer) == k:  # Check if the length of the next k-mer is k.
            kmers[kmer].add(next_kmer)  # Add the subsequent k-mer to the set of subsequent k-mers for the current k-mer.
    return kmers  # Return the dictionary containing all k-mers and their subsequent k-mers.
  
#Define a function find_all_kmers that takes a filename and an integer k as input and 
#returns a dictionary where keys are sequence numbers and values are dictionaries of k-mers and their subsequent k-mers 
#for each sequence.
def find_all_kmers(filename, k): 
    """
    Identify all possible substrings and their subsequent substrings for all sequences read from a file.

    Args:
    - filename (str): The path to the file containing DNA sequences.
    - k (int): The size of the substrings.

    Returns:
    - dict: A dictionary where keys are sequences and values are dictionaries of substrings and their subsequent substrings.
    """
    sequences = {} #Initialize an empty dictionary to store sequences and their k-mers.
    try:
      with open(filename, 'r') as file: #Open the file specified by filename in read mode.
        for seq_num, line in enumerate(file, start=1): #Iterate over each line in the file, using enumerate to get both the line and its line number (starting from 1).
            sequence = line.strip() #Remove leading and trailing whitespaces from the line to get the DNA sequence.
            sequences[seq_num] = find_kmers(sequence, k) #Call the find_kmers function to find all k-mers and their subsequent k-mers for the current sequence, and store the result in the sequences dictionary.
    except FileNotFoundError:
        raise FileNotFoundError("File not found.")  # Raise a FileNotFoundError if the file specified by filename is not found.
    return sequences #Return the dictionary containing all sequences and their k-mers.


##Define a function find_smallest_k that takes a filename as input and 
#returns the smallest value of k where every substring has only one possible subsequent substring.
def find_smallest_k(filename):
    """
    Identify the smallest value of k where every substring has only one possible subsequent substring.

    Args:
    - filename (str): The path to the file containing DNA sequences.

    Returns:
    - int: The smallest value of k.
    """
    smallest_k = 1 #Initialize the smallest value of k to 1.
    try:
      with open(filename, 'r') as file:
        for line in file: #Iterate over each line in the file.
            sequence = line.strip() #Remove leading and trailing whitespaces from the line to get the DNA sequence.
            k = 1 #Initialize k to 1.
            while True: #Start an infinite loop.
                kmers = find_kmers(sequence, k) #Call the find_kmers function to find all k-mers and their subsequent k-mers for the current sequence and value of k.
                if all(len(subseq) == 1 for subseq in kmers.values()): #Check if every k-mer in the sequence has only one subsequent k-mer.
                    smallest_k = k #If all k-mers have only one subsequent k-mer, update the smallest value of k.
                    break #Exit the loop.
                k += 1 #Increment k to check the next value.
    except FileNotFoundError:
        raise FileNotFoundError("File not found.")
    return smallest_k  #Return the smallest value of k.

if __name__ == "__main__": #checks if the script is being run directly as the main program.
    #Creates an argument parser object parser with a description for the program.
    parser = argparse.ArgumentParser(description='Identify k-mers and their subsequent k-mers from DNA sequences')
    #Adds an argument -s or --sequence to specify a single DNA sequence.
    parser.add_argument('-s', '--sequence', type=str, help='DNA sequence')
    #Adds an argument -f or --filename to specify a file containing DNA sequences.
    parser.add_argument('-f', '--filename', type=str, help='Path to the file containing DNA sequences')
    #Adds an argument -k to specify the length of k-mers, with a default value of 2.
    parser.add_argument('-k', type=int, default=2, help='Length of the k-mers (default is 2)')
    #Parses the command-line arguments provided by the user.
    args = parser.parse_args()

    if not args.sequence and not args.filename: #Checks if neither a sequence nor a filename was provided.
        print("Please provide either a DNA sequence (-s) or a filename (-f).")
    elif args.sequence: #Checks if a sequence was provided.
        kmers = find_kmers(args.sequence, args.k) #Calls the find_kmers function to find k-mers in the provided sequence.
        for kmer, subsequent_kmers in kmers.items(): #Iterates over the dictionary of k-mers and their subsequent k-mers.
            print(f"{kmer}: {subsequent_kmers}")
    elif args.filename: #Checks if a filename was provided.
        sequences = find_all_kmers(args.filename, args.k)
        for seq_num, kmers in sequences.items():
            print(f"Sequence {seq_num}:")
            for kmer, subsequent_kmers in kmers.items():
                print(f"  {kmer}: {subsequent_kmers}")

        smallest_k = find_smallest_k(args.filename) 
        print(f"The smallest value of k is: {smallest_k}")
