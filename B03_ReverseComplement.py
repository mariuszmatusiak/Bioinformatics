# 
# ReverseComplement
# For "Finding Hidden Messages in DNA (Bioinformatics I)" by UC San Diego
# Copyright (c) 2024 Mariusz Matusiak
# 
import sys

def replaceLetter(Text):
    textCopy = list(Text)
    for i in range(len(textCopy)):
        if textCopy[i] == 'A':
            textCopy[i] = 'T'
        elif textCopy[i] == 'T':
            textCopy[i] = 'A'
        elif textCopy[i] == 'G':
            textCopy[i] = 'C'
        elif textCopy[i] == 'C':
            textCopy[i] = 'G'
    return "".join(textCopy)

def ReverseComplement(Text):
    complementary = replaceLetter(Text)
    print("Complementary: {}".format(complementary))
    complementaryReversed = complementary[::-1]
    return complementaryReversed

def main():
    file = sys.argv[1] if len(sys.argv) > 1 else "TestData/ReverseComplement/inputs/dataset_30273_2.txt"
    with open (file, "r") as inputFile:
        fileContent = inputFile.readlines()
        Text = fileContent[0].strip()
        # Text = "CCAGATC"
        print("Original: {}".format(Text))
        reversed = ReverseComplement(Text)
        print("Reversed: {}".format(reversed))

if __name__ == "__main__":
    main()
