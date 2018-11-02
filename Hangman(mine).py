word = ["asshole", "motherfucker", "motherless", "homeless", "retard"]

import random

q = random.choice(word)


qq=[]
qLength = len(q)


for i in range(0,qLength):
    qq.append(q[i].lower())
    
show = []


for i in range(0,qLength):
    show.append("_")

print("Guess the fuckn word", show, "자릿수:",qLength)

hangman = [" --------",
           "|       |",
           "|       |",
           "|       0/",
           "|      /|/",
           "|      /",
           "|",
           "|"]

i=0
while True:
    digit = int(input("몇 번째 글자 맞출 거임?: "))-1
    guess = input("The answer is: ").lower()
    if qq[digit] == guess:
        show[digit] = q[digit].lower()
        print(show)
        if show == qq:
            print("Plyaer2 win: You saved his life!! Go kill him by yourself!")
            break      
    else:
        j=0
        while j<=i:
            print(hangman[j])
            j+=1
        if j==7:
            print("Player1 win: Poor hangman's miserable life is over.")
            print("The answer was", q, "asshole")
            break
        i+=1
    

