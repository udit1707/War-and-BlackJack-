import random
suits= ('Hearts','Diamonds','Spades','Clubs')
ranks= ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace') 

values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':11,'Queen':12,'King':13,'Ace':14}

class Card():
    
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]
        
        
    def __str__(self):
        return self.rank +" of "+ self.suit 

class Deck():
    
    def __init__(self):
        self.all_cards=[]
        
        for suit in suits:
             for rank in ranks:
                    created_card=Card(suit,rank)
                    self.all_cards.append(created_card)
                    
    def shuffle(self):
        
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        return self.all_cards.pop()

new_deck=Deck()
new_deck.shuffle()

class Player():
    
    def __init__(self,name):
        
        self.name=name
        self.all_cards=[]
        
    def remove_one(self):
        return self.all_cards.pop(0)
        
    def add_cards(self,new_cards):
        if type(new_cards)==type([]):
            #For multiple card objects
            return self.all_cards.extend(new_cards)
        else:
            #For single card object
            return self.all_cards.append(new_cards)
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'

player1=Player('Udit')

player2=Player('PC')

player1.add_cards([new_deck.all_cards[card] for card in range(0,26)])
player2.add_cards([new_deck.all_cards[card] for card in range(26,52)])



# AACTUAL GAME LOGIC

game_on=True

round_num=0
while game_on:
    round_num+=1
    print(f'Current on Round {round_num}')
    if len(player1.all_cards)==0:
        print('Player 1, out of Cards \nPlayer 2 wins')
        game_on=False
        break
    if len(player2.all_cards)==0:
        print('Player 2, out of Cards \nPlayer 1 wins')
        game_on=False
        break
        
    card1=[]
    card2=[]
    c1=player1.remove_one()
    c2=player2.remove_one()
    card1.append(c1)
    card2.append(c2)
    war_on=True
        
    while war_on:
        
       
        if c1.value>c2.value:
            player1.add_cards(card1)
            player1.add_cards(card2)
            war_on=False
        elif c2.value>c1.value:
            player2.add_cards(card2) 
            player2.add_cards(card1) 
            war_on=False
        else:
            print('W@r!')
            if len(player1.all_cards) <5:
                print("Player 1 unable to declare war")
                print("Player 2 wins")
                game_on=False
                break
            elif len(player2.all_cards) <5:
                print("Player 2 unable to declare war")
                print("Player 1 wins")
                game_on=False
                break
            else:
                for num in range(5):
                    c1=player1.remove_one()
                    c2=player2.remove_one()
                    card1.append(c1)
                    card2.append(c2)
                    
            
             

    