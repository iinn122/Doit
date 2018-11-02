class Fuck:
    def __init__(self,s):
        self.shit = s

    def __lt__(self, other):
        return self.shit < other.shit

f1 = Fuck(3)
f2 = Fuck(7)
print(f1.shit)
print(f2.shit)
print(f1.shit < f2.shit)
print(f1 > f2)    
