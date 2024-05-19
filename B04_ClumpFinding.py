# 
# ClumpFinding
# For "Finding Hidden Messages in DNA (Bioinformatics I)" by UC San Diego
# Copyright (c) 2024 Mariusz Matusiak
# 
import sys
from B02_FrequentWords import FrequencyTable

def ClumpFinding(Gen : str, k: int, L: int, t: int):
    Patterns = set()
    for i in range(len(Gen) - L + 1):
        Window = Gen[i:i+L]
        freqMap = FrequencyTable(Window, k)
        for key in freqMap.keys():
            if freqMap.get(key) >= t:
                Patterns.add(key)
    return Patterns

def main():
    file = sys.argv[1] if len(sys.argv) > 1 else "ClumpFinding/inputs/input_1.txt"
    with open (file, "r") as inputFile:
        fileContent = inputFile.readlines()
        Gen = fileContent[0].strip()
        print(Gen)
        k, L, T = fileContent[1].strip().split()
        keys = ClumpFinding(Gen, int(k), int(Gen), int(T))
        print("Clumps:")
        print(" ".join(keys))
        print("Count: {}".format(len(keys)))

if __name__ == "__main__":
    main()