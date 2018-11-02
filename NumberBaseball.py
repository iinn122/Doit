#1 수비수 숫자 고르기
answer = []
import random

while True:
    for i in range(0,3):
        answer.append(random.randint(0,9))
    if answer[0] == answer[1] or answer[0] == answer[2] or answer[1]==answer[2]:
        continue
    else:
        break



#2 공격수 숫자 고르기
tryCount = 0
while True:
    while True:
        guess1= input("공격할 숫자 세 자리를 입력하세요")
        guess2="+".join(guess1)
        guess= guess2.split("+")

        for i in range(0,len(guess1)):
            guess[i] = int(guess[i])

        if len(guess1) != 3:
            print("세 자리로 입력하세요")
            continue
        if guess[0]==guess[1] or guess[0]==guess[2] or guess[1]==guess[2]:
            print("같은 숫자가 없게 입력하세요")
            continue
        else:
            tryCount +=1
            break
   

#3 스트라이크 볼 아웃 계산
    strike = 0
    ball = 0

    for i in range(0,3):
        if guess[i] in answer:
            ball += 1
        if guess[i] == answer[i]:
            strike += 1
            ball -= 1   
        
    print("Strike:", strike)
    print("Ball:", ball)
    out = 3 - (strike + ball)
    print("Out:", out)

    if strike == 3:
        print(tryCount, "번 만에 맞췄드아!")
        break
    
        
    
