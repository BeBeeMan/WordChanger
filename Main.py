print('input file:')
inFile = input() + '.txt'
print('word:')
y = input()
print('what to put after that word?')
x = input()

with open(inFile, 'r') as myFile:
    lines = myFile.readlines()
    for words in lines:
        a = words.split(' ')

    for n, i in enumerate(a):
        if i == y:
            a[n + 1] = x

with open('output.txt', 'w') as outFile:
    aStr = ' '.join([str(elem) for elem in a])
    print(aStr)
    outFile.write(aStr)
