pattern = input('Enter Pattern: ')
text = input()


def positions_pattern(pattern, text):
    positions = []
    for i in range(len(text)-len(pattern)+1):
        if text[i:i+len(pattern)] == pattern:
            positions.append(i)
            print(i, end=" ")
    print()
    return positions


positions_pattern(pattern, text)
"""
if __name__ == "__main__":
    with open("data/rosalind_ba1d.txt", "r") as f:
       
    
"""
