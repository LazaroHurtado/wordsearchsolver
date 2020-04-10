import show_puzzle
import solve_puzzle

puzzle = [ ['D','E','Y','E','S','H','A','D','O','W','N','N','B','H'],
           ['T','U','C','R','I','A','H','O','H','D','M','A','L','P'],
           ['G','A','B','M','O','C','T','O','A','T','O','S','O','E'],
           ['O','P','E','R','F','U','M','E','I','R','U','P','W','O'],
           ['A','N','S','Y','I','O','B','T','R','O','S','A','D','W'],
           ['T','O','S','O','I','T','E','K','S','T','T','R','R','A'],
           ['E','P','A','S','D','E','A','B','T','M','A','S','Y','X'],
           ['E','A','R','A','Z','O','R','Y','Y','A','C','H','E','I'],
           ['R','A','N','U','A','S','D','A','L','K','H','A','R','N'],
           ['B','A','I','B','R','U','S','H','E','E','E','M','A','G'],
           ['S','T','Y','L','I','S','T','R','E','U','U','P','N','P'],
           ['T','H','D','M','I','R','T','N','S','P','N','O','Y','M'],
           ['C','P','E','R','M','A','N','E','N','T','I','O','S','P'],
           ['A','I','C','U','R','L','I','N','G','I','R','O','N','T']
          ]

wordbank = ['PERFUME','HAIRSTYLE','CURLINGIRON','MOUSTACHE', 'BEARD','EYESHADOW','SAUNA','STYLIST','BRUSH','PERMANENT','SHAMPOO','WAXING','GOATEE','BLOWDRYER','MAKEUP','TRIM','RAZOR','HAIRCUT','COMB','SPA']

puzzle2 = [ ['Y','H','Y','A','H'],
            ['A','Z','E','Z','G'],
            ['T','C','Y','Y','W']
          ]

wordbank2 = ['YAT','HEY','YEY']

puzzle3 = [ ['D','G','O','O','D','D','O','D','G','O','O','D','D','O'],
            ['O','D','O','O','G','G','G','D','O','D','G','O','G','G'],
            ['O','G','O','G','D','O','O','D','G','O','O','D','D','D'],
            ['D','G','D','O','O','O','G','G','O','O','G','D','G','O'],
            ['O','G','D','G','O','G','D','G','O','G','G','O','G','D'],
            ['D','D','D','G','D','D','O','D','O','O','G','D','O','O'],
            ['O','D','G','O','G','G','D','O','O','G','G','O','O','D']
          ]

wordbank3 =['DOG']

if __name__ == '__main__':
    show_puzzle.show_puzzle(puzzle, wordbank)
    solve_puzzle.solve_puzzle(puzzle, wordbank)
