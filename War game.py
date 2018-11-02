# 카드
class Card:
    suits = ["spades", 'hearts', 'diamonds', 'clubs']
    values = [None, None, '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

    def __init__(self, v, s):
        self.value = v
        self.suit = s

    def __lt__(self, c2):
        return self.value < c2.value
        if self.value == c2.value:
            return self.suit < c2.suit
                
    def __gt__(self, c2):
        return self.value > c2.value            
        if self.value == c2.value:
            return self.value > c2.suit
  
    def __repr__(self):
        v= self.values[self.value] + " " + "of" + " " + self.suits[self.suit]
        return v

#덱
from random import shuffle

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2,15):
            for j in range(4):
                self.cards.append(Card(i,j))
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()


#플레이어
class Player:
    def __init__(self,name):
        self.wins = 0
        self.card = None
        self.name = name

#게임
class Game:
    def __init__(self):
        name1 = input("p1 name ")
        name2 = input("p2 name ")
        self.deck = Deck() #다른 클래스로부터 객체 만들 때 걍 써도 됨
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def wins(self, winner):
        w = "{} wins this round"
        w = w.format(winner)
        print(w)

    def draw(self, p1n, p1c, p2n, p2c):
        d= "{} drew {} {} drew {}"
        d = d.format(p1n,p1c,p2n,p2c)
        print(d)

    def play_game(self):
        cards = self.deck.cards
        print("Let the war begins!")
        while len(cards) >= 2:
            m = "q to quit. Any key to play:"
            response = input(m)
            if response == 'q':
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n, p1c, p2n, p2c)
            if p1c >p2c:
                self.p1.wins +=1
                self.wins(self.p1.name)
            else:
                self.p2.wins +=1
                self.wins(self.p2.name)

        if self.p1.wins > self.p2.wins: #다른 클래스의 인스턴스 변수 쓰려면 self??
            print("War is over.",p1n, "wins.")
        if self.p1.wins < self.p2.wins:
            print("War is over.",p2n, "wins.")
        if self.p1.wins == self.p2.wins:
            print("It was a tie!")
        
        

game = Game()
game.play_game()
        
