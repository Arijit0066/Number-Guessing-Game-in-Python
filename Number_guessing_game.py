import random

i=0
rando = random.randint(1, 100)


i = int(i)

while True:
    player = input("Guess The Number Between (1-99) : ")
    player = int(player)
    if rando == player:
        print("Finally You Have Guessed The Number")
        i = i+1
        break
    elif player > rando:
        print("Your Number is Greater Then Guessing Number")
        i= i+1
    else:
        print("Your Number is Smaller Then Guessing Number")
        i = i+1
print(f"Attemps : {i}")
print(f"Your Score : {100-i}" )
