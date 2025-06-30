# Complementing a Strand of DNA

"""
Given: A DNA string s of length at most 1000 bp.
Return: The reverse complement of s.
"""

dataset = input("Type in DNA String: ")

for char in range(len(dataset)):
    if dataset[char] == "A":
        complement_dataset = dataset.replace('A', 'T')

    if dataset[char] == "T":
        complement_dataset = dataset.replace('T', 'A')

    if dataset[char] == "C":
        complement_dataset = dataset.replace('C', 'G')

    if dataset[char] == "G":
        complement_dataset = dataset.replace('G', 'C')
    
print(complement_dataset)
    