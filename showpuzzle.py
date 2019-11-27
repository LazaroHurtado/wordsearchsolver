def showpuzzle(puzzle, wordbank):
    wordsearch = ''
    for i in puzzle:
        for p in i:
            wordsearch += ' ' + p
        wordsearch += '\n'
    print(wordsearch + '\n')
    words = ''
    for i in wordbank:
        if i != wordbank[0]:
            words += '   ' + i
        else:
            words += i
    print(words, '\n', '\n')
    
def showsolvedpuzzle(solvedpuzzle, puzzle, wordbank):
    for key, values in solvedpuzzle.items():
        for position in values:
            puzzle[key][position[0]] = position[1]
    showpuzzle(puzzle, wordbank)
    