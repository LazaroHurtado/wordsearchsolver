import showpuzzle

class solvethepuzzle:
    def __init__(self, puzzle, words):
        self.puzzle = puzzle
        self.words = words
        self.first = []
        for i in self.words:
            self.first.append(i[0])
        self.position = {}
        for p in range(len(self.puzzle)):
            self.position[p] = []
        self.solvepuzzle()
        
    def solvepuzzle(self):
        for i in range(len(self.puzzle)):
            for p in range(len(self.puzzle[i])):
                if self.puzzle[i][p] in self.first:
                    self.possiblesolve(i, p, [x for x in self.words if x[0] == self.puzzle[i][p]], self.puzzle)
        showpuzzle.showsolvedpuzzle(self.position, self.puzzle, self.words)
        
    def possiblesolve(self, i, p, words, puzzle):
        for word in words:
            top = len(self.puzzle[:i+1]) - len(word)
            topletters = ''
            if top >= 0:
                for letter in range(len(word)):
                    if self.puzzle[i-letter][p] == word[letter]:
                        topletters += word[letter]
                        if topletters == word:
                            for z in range(len(word)):
                                self.position[i-z].append([p, '|'])
                            self.words.remove(word)
                            self.first.remove(word[0])
                             
        
            left = len(self.puzzle[i][:p+1]) - len(word)
            leftletters = ''
            if left >= 0:
                for letter in range(len(word)):
                    if self.puzzle[i][p-letter] == word[letter]:
                        leftletters += word[letter]
                        if leftletters == word:
                            for z in range(len(word)):
                                self.position[i].append([p-z, '-'])
                            self.words.pop(self.words.index(word))
                            self.first.remove(word[0])
                             
        
            right = len(self.puzzle[i][p:]) - len(word)
            rightletters = ''
            if right >= 0:
                for letter in range(len(word)):
                    if self.puzzle[i][p+letter] == word[letter]:
                        rightletters += word[letter]
                        if rightletters == word:
                            for z in range(len(word)):
                                self.position[i].append([p+z, '-'])
                            self.words.pop(self.words.index(word))
                            self.first.remove(word[0])
                            
        
            bottom = len(self.puzzle[i:]) - len(word)
            bottomletters = ''
            if bottom >= 0:
                for letter in range(len(word)):
                    if self.puzzle[i+letter][p] == word[letter]:
                        bottomletters += word[letter]
                        if bottomletters == word:
                            for z in range(len(word)):
                                    self.position[i+z].append([p, '|'])
                            self.words.pop(self.words.index(word))
                            self.first.remove(word[0])
                            
            topleftletters = ''
            if left >= 0 and top >= 0:
                for letter in range(len(word)):
                    if self.puzzle[i-letter][p-letter] == word[letter]:
                        topleftletters += word[letter]
                        if topleftletters == word:
                            for z in range(len(word)):
                                self.position[i-z].append([p-z, '\\'])
                            self.words.pop(self.words.index(word))
                            self.first.remove(word[0])
                        
            toprightletters = ''
            if right >= 0 and top >= 0:
                for letter in range(len(word)):
                    if self.puzzle[i-letter][p+letter] == word[letter]:
                        toprightletters += word[letter]
                        if toprightletters == word:
                            for z in range(len(word)):
                                self.position[i-z].append([p+z, '/'])
                            self.words.pop(self.words.index(word))
                            self.first.remove(word[0])
            
            bottomleftletters = ''
            if left >= 0 and bottom >= 0:
                for letter in range(len(word)):
                    if self.puzzle[i+letter][p-letter] == word[letter]:
                        bottomleftletters += word[letter]
                        if bottomleftletters == word:
                            for z in range(len(word)):
                                self.position[i+z].append([p-z, '/'])
                            self.words.pop(self.words.index(word))
                            self.first.remove(word[0])
            
            bottomrightletters = ''
            if right >= 0 and bottom >= 0:
                for letter in range(len(word)):
                    if self.puzzle[i+letter][p+letter] == word[letter]:
                        bottomrightletters += word[letter]
                        if bottomrightletters == word:
                            for z in range(len(word)):
                                self.position[i+z].append([p+z, '\\'])
                            self.words.pop(self.words.index(word))
                            self.first.remove(word[0])
               
        return
        