# 
# FrequentWords
# For "Finding Hidden Messages in DNA (Bioinformatics I)" by UC San Diego
# Copyright (c) 2024 Mariusz Matusiak
# 
import sys

def FrequencyTable(Text, k):
    words = dict()
    for i in range(len(Text)-k+1):
        sliced = Text[i:i+k]
        if sliced in words:
            words[sliced] += 1
        else:
            words[sliced] = 1
    return words

def FrequentWords(Text, k):
    words = FrequencyTable(Text, k)
    # return max keys
    max_value = max(words.values())
    max_keys = [key for key, value in words.items() if value == max_value]
    return (max_keys, max_value)

def main():
    file = sys.argv[1] if len(sys.argv) > 1 else "TestData/FrequentWords/inputs/dataset_30272_13.txt"
    with open (file, "r") as inputFile:
        fileContent = inputFile.readlines()
        Text = fileContent[0].strip()
        # Text = "CGCCTAAATAGCCTCGCGGAGCCTTATGTCATACTCGTCCT"
        print(Text)
        k = int(fileContent[1].strip())
        # k = 3
        keys, value = FrequentWords(Text, k)
        print(" ".join(keys))
        print("Count: {}".format(value))

if __name__ == "__main__":
    main()
