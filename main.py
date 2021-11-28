import re
import chess
import chess.pgn

class MoveNotation: 
    def __init__(self, line: str) -> None:
        sectors = line.split(" { ")
        self.move = sectors[0]
        sectors = sectors[1].split(' ')
        self.date = sectors[0]
        self.clock = sectors[1]

class GameNotation:
    def __init__(self, line: str) -> None:
        sectors = line.split("]")
        self.game_nr = 0
        self.variant = 0
        
        rounds = re.split(r"\d\. ", sectors[-1])
        
        first_p = []
        secont_p = []
        third_p = []
        fourth_p = []

        for r in rounds:
            temp = r.split(' .. ')            
            print(r)
            print(15*"|")
            print(temp)
            
def readLines():    #this code it's for pytest
    with open(r'C:\Users\radoe\Desktop\Work\data\solo.txt', 'r') as f:
        x = f.readline()
        # end = re.split(r'\[[^\]]*\]\[Variant "FFA"]\[RuleVariants "PromoteTo=D"]',x)
        GameNotation(x)

