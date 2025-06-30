# Complementing a Strand of DNA

"""
Given: A DNA string s of length at most 1000 bp.
Return: The reverse complement of s.
"""

dataset = input("Type in DNA String:")
dataset = dataset.replace('A', 't').replace('T', 'a').replace('C', 'g').replace('G', 'c').upper()[::-1]
print(dataset)
    