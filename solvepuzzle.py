import showpuzzle
import collections
import copy

class solvethepuzzle:
    def __init__(self, puzzle, words):
        self.puzzle = puzzle
        self.first = self.get_first(words)
        self.last = self.get_last(words)
        self.directions = [(0, 1), (1, 0), (1, -1), (1, 1)]
        self.strokes = {(0, 1):"-", (1, 0):"|", (1, -1):"/", (1, 1):"\\"}
        self.solve()
        showpuzzle.showpuzzle(self.puzzle)

    def dfs(self, direction, word, puzzle, curr, position, i):
        if curr == word:
            self.puzzle = puzzle
            return
        if len(curr) >= len(word):
            return
        row, col = position
        max_row = len(puzzle)-1
        max_col = len(puzzle[0])-1
        if row < 0 or col < 0 or row > max_row or col > max_col:
            return
        curr_letter = self.puzzle[row][col]
        curr += curr_letter
        if curr != word[:len(curr)] and curr != word[len(curr)+1:]:
            return
        puzzle[row][col] = self.strokes[direction]
        dir_row, dir_col = direction
        new_position = (row + dir_row, col + dir_col)
        self.dfs(direction, word, puzzle, curr, new_position, i)

    def solve(self):
        for row in range(len(self.puzzle)):
            for col in range(len(self.puzzle[row])):
                letter = self.puzzle[row][col]
                position = (row, col)
                if letter in self.first:
                    self.to_dfs(letter, position, "first")
                if letter in self.last:
                    self.to_dfs(letter, position, "last")

    def to_dfs(self, letter, position, method):
        if method == "first":
            words = self.first[letter]
        else:
            words = self.last[letter]
        i = 0
        row, col = position
        temp_puzzle = copy.deepcopy(self.puzzle)
        for word in words:
            for direction in self.directions:
                self.dfs(direction, word, temp_puzzle, "", position, i)
                i+=1

    def get_first(self, words):
        first_letters = collections.defaultdict(list)
        for word in words:
            first = word[0]
            first_letters[first].append(word)
        return first_letters

    def get_last(self, words):
        last_letters = collections.defaultdict(list)
        for word in words:
            last = word[-1]
            last_letters[last].append(word)
        return last_letters
