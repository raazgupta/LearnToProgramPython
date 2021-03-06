def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return get_length(dna1) > get_length(dna2)

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    count = 0
    for n in dna:
        if n in nucleotide:
            count = count + 1

    return count


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return (dna2 in dna1)


def is_valid_sequence(dna):
    validChar = ['A','T','C','G']

    isValid = True
    
    for c in dna:
        if c not in validChar:
            isValid = False

    return isValid

def insert_sequence(dna1,dna2,index):
    return dna1[:index] + dna2 + dna1[index:]


def get_complement(n):
    complement = ''
    if n == 'A':
        complement = 'T'
    elif n == 'T':
        complement = 'A'
    elif n == 'C':
        complement = 'G'
    elif n == 'G':
        complement = 'C'

    return complement

def get_complementary_sequence(dna):
    cdna = ''
    for c in dna:
        cdna = cdna + get_complement(c)
    return cdna



print(get_complementary_sequence(''))


