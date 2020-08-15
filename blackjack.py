import random
suits= ('Hearts','Diamonds','Spades','Clubs')
ranks= ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace') 

values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11}
playing=True

class Card():
    
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]
        
        
    def __str__(self):
        return self.rank +" of "+ self.suit 

class Deck():
    
    def __init__(self):
        self.deck=[]
        
        for suit in suits:
             for rank in ranks:
                    created_card=Card(suit,rank)
                    self.deck.append(created_card)
                    
    def __str__(self):
        deck_comp=''
        for card in self.deck:
            deck_comp+='\n'+card.__str__()
        return f'The deck has: {deck_comp}'
    
                    
    def shuffle(self):
        
        random.shuffle(self.deck)
        
    def deal_one(self):
        single_card=self.deck.pop()
        return single_card

class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        self.value+=values[card.rank]
        if card.rank=='Ace':
            self.aces+=1
    
    def adjust_for_ace(self):
        while self.value>21 and self.aces:
            self.value-=10
            self.aces-=1


class Chips:
    
    def __init__(self,total=100):
        self.total = total  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total+=self.bet
    
    def lose_bet(self):
        self.total-=self.bet

def take_bet(chips):
    
    while True:
        try:
            chips.bet=int(input('How many chips would you like to bet?: '))
        except:
            print("Sorry please provide an integer")
        else:
            if chips.bet>chips.total:
                print(f'Sorry, not enough chips. your total is {chips.total}')
            else:
                break
    
    
def hit(deck,hand):
    card=deck.deal_one()
    hand.add_card(card)
    hand.adjust_for_ace()
    

def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    
    while True:
        choice=input("Enter Hit or Stand: ")
        if(choice=='Hit'):
            hit(deck,hand)
            break
        elif(choice=='Stand'):
            print("Player Stands Dealer's Turn")
            playing=False
        else:
            continue


def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)

def player_busts(player,dealer,chips):
    print('Bust player')
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player wins")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print('Bust dealer')
    chips.lose_bet()
    
def dealer_wins(player,dealer,chips):
    print("Dealer wins")
    chips.win_bet()
    
def push(player,dealer):
    print('Dealer and Player tie! Push')
    
while True:
    # Print an opening statement
    print('Welcome to the Black Jack!!')

    
    # Create & shuffle the deck, deal two cards to each player
    new_deck=Deck()
    new_deck.shuffle()
    
    player_hand=Hand()
    player_hand.add_card(new_deck.deal_one())
    player_hand.add_card(new_deck.deal_one())
    
    dealer_hand=Hand()
    dealer_hand.add_card(new_deck.deal_one())
    dealer_hand.add_card(new_deck.deal_one())
    
    
        
    # Set up the Player's chips
    player_chips=Chips()
       
    
    # Prompt the Player for their bet
    take_bet(player_chips)
    

    
    # Show cards (but keep one dealer card hidden)
    show_some(player_hand,dealer_hand)

    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(new_deck,player_hand)
        
        
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand)
 
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value>21:
            player_busts(player_hand,dealer_hand,player_chips)
            break
        

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value<=21:
        
        while dealer_hand.value<17:
            hit(new_deck,dealer_hand)
            
    
        # Show all cards
        show_all(player_hand,dealer_hand)
    
        # Run different winning scenarios
        if dealer_hand.value>21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value>player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand)
            
        
    
    # Inform Player of their chips total 
    print('\n Player total chips are at {}'.format(player_chips.total))
    
    
    # Ask to play again
    new_game=input("Would you like to play another hand? y/n: ")
    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print('Thank you for playing!')
        break
    
