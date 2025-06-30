# Counting DNA Nucleotides 

'''
Given: A DNA string s of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.
'''

dataset = input("Type in DNA String: ")

adenine_count = 0
cytosine_count = 0
guanine_count = 0
thymine_count = 0

for char in range(len(dataset)):
    if dataset[char] == "A":
        adenine_count += 1
    if dataset[char] == "C":
        cytosine_count += 1
    if dataset[char] == "G":
        guanine_count += 1
    if dataset[char] == "T":
        thymine_count += 1

print(adenine_count, cytosine_count, guanine_count, thymine_count)
