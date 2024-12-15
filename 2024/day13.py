from openData import getData
import re

class Equation:

    def __init__(self, a, b, c, d, e, f, part2 = False) -> None:
        self.a = int(a)
        self.b = int(b)
        self.c = int(c) + 10000000000000 if part2 else 0
        self.d = int(d)
        self.e = int(e)
        self.f = int(f) + 10000000000000 if part2 else 0
        self.x = 0
        self.y = 0
        self.getX()
        self.getY()

    def getX(self) -> int:
        self.x = ((self.e*self.c) - (self.b*self.f)) / ((self.e*self.a) - (self.b*self.d))
        return self.x
    
    def getY(self) -> int:
        self.y = (self.f-(self.d*self.x))/self.e
        return self.y
    
    def isValid(self) -> bool:
        return self.y == int(self.y) and self.x == int(self.x)
    
    def tokens(self) -> int:
        return (self.y * 1) + (self.x * 3)
    

if __name__ == "__main__":
    input = getData("13", False)
    part2 = True
    tokens = 0

    for i in range(0, len(input), 4):
        a, d = re.findall("\d{1,5}", input[i])
        b, e = re.findall("\d{1,5}", input[i+1])
        c, f = re.findall("\d{1,5}", input[i+2])
        
        eq = Equation(a, b, c, d, e, f, part2)
        tokens += eq.tokens() if eq.isValid() else 0    

    print("Result part1: ", tokens)