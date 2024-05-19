# 
# PatternCount
# For "Finding Hidden Messages in DNA (Bioinformatics I)" by UC San Diego
# Copyright (c) 2024 Mariusz Matusiak
# 
import sys

def PatternCountAndPosition(Text, Pattern):
    #return Text.count(Pattern) #<- doesn't work as it does not count overlaps
    count = 0
    pos = 0
    positions = []
    while pos < len(Text):
        nextOccurence = Text.find(Pattern, pos)
        if nextOccurence != -1:
            positions.append(str(nextOccurence))
            count = count+1
            pos = nextOccurence + 1
        else:
            break
    return (count, positions)

def main():
    file = sys.argv[1] if len(sys.argv) > 1 else "TestData/PatternMatching/inputs/Vibrio_cholerae.txt"
    with open (file, "r") as inputFile:
        fileContent = inputFile.readlines()
        Text = fileContent[0].strip()
        # Text = "ATGACTTCGCTGTTACGCGC"
        print(Text)
        Pattern = fileContent[1].strip()
        # Pattern = "CGC"
        print(Pattern)
        count, positions = PatternCountAndPosition(Text, Pattern)
        print("Occurences: {}".format(count))
        print("Positions: {}".format(" ".join(positions)))

if __name__ == "__main__":
    main()