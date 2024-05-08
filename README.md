---
title: "README - K-mers and Subsequent K-mers"
author: "Arvie Grace Masibag"
date: "2024-05-07"
output: html_document
---

```{r setup, include=FALSE}
knitr::opts_chunk$set(echo = TRUE)
```

# DNA Sequence Analysis Script

This Python script analyzes DNA sequences to identify k-mers and their subsequent k-mers. It also finds the smallest value of k (find_kmers, find_all_kmers, find_smallest_k) .

## Usage

### Prerequisites
- Python 3

### Running the Script
1. Clone this repository to your local machine:
    git clone https://github.com/amasibag/K-mers-and-subsequent-k-mers-.git
    
2. Change into the project directory:

3. Run the script with the following command, providing the path to the file containing DNA sequences:

     python kmer.py -s ATGTCTGTCTGAA -k 2

     python kmer.py -f /path/to/your/sequence-file.fa -k 3


### Command-line Arguments
- `-s` : DNA sequence
- `-f` : Path to the file containing DNA sequences.
- `-k` (optional): Length of the k-mers (default is 2).

### Output
The script will output the identified k-mers and their subsequent k-mers for each sequence in the file, different k-mers length specified, as well as the smallest value of k where every substring has only one possible subsequent substring.


