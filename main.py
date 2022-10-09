
words = input('Enter the list: ').split()

are = ['a', 'r', 'e']
idxlst = []

# ******************************
# Make your Code
# ******************************

for i in range(len(words)):
    k = 0
    for j in range(len(words[i])):
        if are[k] == words[i][j]:
            k += 1
        if k == len(are):
            break
    if k == len(are):
        idxlst.append(words[i])

print(words)

# print the words that has 'a', 'r', 'e' in sequence

