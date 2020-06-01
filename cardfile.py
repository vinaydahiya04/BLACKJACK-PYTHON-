import random

def rules():
    j = open("rules.txt", "r")
    print(j.read())
    j.close()


class Card():         #here value is the blackjack value and num is the number on card
    def __init__(self,color,value,num):
        self.color = color
        self.value = value
        self.num = num
    def __str__(self):
        return str(self.num)  + "\n" + self.color

cardlist = []

for col in [" hearts ", " spades ", " clubs  ", "diamonds"]:
    for i in range(1,14):
        if i>10:
            x = 10
        else:
            x = i
        ca = Card(col,x,i)
        cardlist.append(ca)

random.shuffle(cardlist)




