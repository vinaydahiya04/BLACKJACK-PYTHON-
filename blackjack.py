import cardfile
import random
import time



def print_cards(pla):
    for i in pla.cards:
        print("----------")
        print("|        |")
        
        print("| {0:4}   |".format(i.num))
        print("|" + i.color + "|")
        print("|        |")
        print("----------")




class Player():
    cards = []
    sum = 0
    possib  = []
    num_ace = 0
    closest = 0
    def __init__(self,name, balance):
        self.name = name
        self.balance = balance
        
    def sumset(self):
        j = 0
        s = 0
        for i in self.cards:
            s += i.value        
            if i.num == 1:
                j += 1
        s += j
        self.sum = s
        self.num_ace = j

    def possibset(self):
        self.possib.clear()
        for i in range(0,2**self.num_ace):
            q = "{0:b}".format(i)
            v = self.sum
            for t in q:
                if t == "1":
                    v += 10
            self.possib.append(v)
    def closestset(self):
        cl = 1000000
        for i in self.possib:
            if(abs(21-i)< cl and (21-i)>=0):
                cl = abs(21-i)
        self.closest = cl
        
            

class Dealer():
    cards = []
    sum = 0
    possib = []
    face_down_card = None
    num_ace = 0
    closest = 0
    def __init__(self):
        pass

    def sumset(self):
        j = 0
        s = 0
        for i in self.cards:
            s += i.value        
            if i.num == 1:
                j += 1
        s += j
        self.sum = s
        self.num_ace = j

    def possibset(self):
        self.possib.clear()
        for i in range(0,2**self.num_ace):
            q = "{0:b}".format(i)
            v = self.sum
            for t in q:
                if t == "1":
                    v += 10
            self.possib.append(v)

    def closestset(self):
        cl = 1000000
        for i in self.possib:
            if(abs(21-i)< cl and (21-i)>=0):
                cl = abs(21-i)
        self.closest = cl


 #**********************************************************************************       

def checker(pla):
    if pla.sum >21:
        return "B"
    if pla.closest == 0:
        return "V"
    return "C"

def bustcheck(dea,pla):
    if dea.sum >21:
        return "B"
    if dea.closest < pla.closest:
        return "D"
    return "C"




s = "WELCOME TO BLACKJACK SUPREME"
print(s.center(140))

rue = input("\t\t\t\t\tpress r if you would like to know the rules of this game, else press c: ")
if rue == "r":
    cardfile.rules()


n = input("enter your name: ")
num = float(input("enter the bank balance: "))
player1  = Player(n,num)
dealer = Dealer()
ns = player1.balance

lis = cardfile.cardlist[0:2]
player1.cards = lis
player1.sumset()
player1.possibset()
player1.closestset()

lis = cardfile.cardlist[2:3]
dealer.cards = lis

dealer.sumset()
dealer.possibset()
dealer.closestset()
ci = 3
ns = player1.balance
nn = player1.name
winnings = 0



while player1.balance >0:
    while True:
        bet  = int(input("PLACE A BET: "))
        while bet> player1.balance:
            print("Invalid bet")
            print("you only have ${} in your bank ".format(player1.balance))
            bet = bet  = int(input("PLACE A BET: "))
        player1.balance -= bet
        print("********************** DISTRIBUTING CARDS **************************\n\n")
        print("*********** YOUR CARDS *********\n")
        print_cards(player1)
        if max(player1.possib) == 21:
            print("CONGRATULATIONS YOU HAVE WON THIS BET ")
            player1.balance += 2.5*bet
            break
        print("*********** DEALERS CARD *********\n")
        print_cards(dealer)

        while True:            
            ch = input("press h if you would like to hit , press s for stay: ")

            if ch != "s" and ch != "h":
                print("invalid entry")
                continue

            if ch == "h":
                player1.cards.append(cardfile.cardlist[ci])
                ci += 1
                print("*********** YOUR CARDS *********\n")
                print_cards(player1)
                player1.possibset()
                player1.sumset()
                br = checker(player1)
                if br == "B":
                    print("YOU HAVE LOST THIS BET ")
                    
                    break
                if br == "V":
                    print(" CONGRATULATIONS YOU HAVE WON THIS BET ")
                    player1.balance += 3*bet
                    break
                continue

            else:
                while True:
                    print("Dealer draws a card ")
                    dealer.cards.append(cardfile.cardlist[ci])
                    ci+=1
                    dealer.sumset()
                    dealer.possibset()
                    dealer.closestset()
                    print("*********** DEALERS CARD *********\n")
                    print_cards(dealer)
                    r = bustcheck(dealer,player1)
                    time.sleep(2.5)
                    if r == "C":
                        continue
                    if r == "B":
                        print(" CONGRATULATIONS YOU HAVE WON THIS BET ")
                        player1.balance += bet*3
                        break
                    print("YOU HAVE LOST THIS BET ")
                    break
                    
            break
        break             

    winnings = player1.balance - ns
    ns = player1.balance
    print("your current bank balance is {} ".format(player1.balance))    
    print("would you like to continue playing : (press 1 for yes and 0 for no) ")
    choice = int(input())
    if choice == 0:
        break
    if(player1.balance == 0.0):
        print(" $$ SORRY YOU HAVE RUN OUT OF MONEY $$ ")
        break
    random.shuffle(cardfile.cardlist)
    
    
    del player1
    del dealer
    player1  = Player(nn,ns)
    dealer = Dealer()

    lis = cardfile.cardlist[0:2]
    player1.cards = lis
    player1.sumset()
    player1.possibset()
    player1.closestset()

    lis = cardfile.cardlist[2:3]
    dealer.cards = lis

    dealer.sumset()
    dealer.possibset()
    dealer.closestset()
    ci = 3

if winnings >0:
    print("\tCONGRATULATIONS YOU WON {}$ ".format(winnings))
else:
    print("\tYOU LOST {} $".format(abs(winnings)))

print("\t\t******* GAME OVER *******")







    










