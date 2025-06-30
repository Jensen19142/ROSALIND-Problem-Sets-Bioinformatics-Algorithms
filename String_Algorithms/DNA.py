# Counting DNA Nucleotides 

'''
Given: A DNA string s of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.
'''

dataset = input("Type in DNA String: ")
print(dataset.count("A"),dataset.count("C"),dataset.count("G"),dataset.count("T"))
