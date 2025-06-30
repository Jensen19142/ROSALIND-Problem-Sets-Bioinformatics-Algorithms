# Transcribing DNA into RNA 

"""
Given: A DNA string t having length at most 1000 nt.
Return: The transcribed RNA string of t.

"""

dataset = input("Type in DNA String: ")

for char in range(len(dataset)):
    if dataset[char] == "T":
        dataset = dataset.replace('T', 'U')

print(dataset)