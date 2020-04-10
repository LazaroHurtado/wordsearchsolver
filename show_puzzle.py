def show_puzzle(puzzle, wordbank=None):
    display = ''
    for row in range(len(puzzle)):
        display += '\n'
        for col in range(len(puzzle[row])):
            display += ' ' + puzzle[row][col]
    print(display)

    words = '\n'
    if wordbank:
        for word in wordbank:
            words += word + '    '
    print(words)
