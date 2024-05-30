Pyramid Decoder
Overview
Pyramid Decoder is a Python script designed to decode a hidden message from a text file based on a "pyramid" structure of numbers. Each line in the input file contains a number followed by a word. The task is to extract words corresponding to numbers that are positioned at the end of each level of a pyramid structure and form a meaningful message.

How It Works
The script reads the input file, parses each line to extract numbers and corresponding words, and stores them in a dictionary. It then calculates the numbers that appear at the end of each level of a pyramid structure. Finally, it extracts the words associated with these numbers and joins them to form the decoded message.
