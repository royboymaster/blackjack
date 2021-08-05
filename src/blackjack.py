"""
Blackjack Card Game
"""

import random
import logging

class Card:
    def __init__(self, face, suit):
        self.face = face
        self.suit = suit

    def __repr__(self): # this dunder function returns a string to represent this object(card)
        return f"({self.face}, {self.suit})"

    def getValue(self): # Teast Driving Development
        if self.face.isdigit():
            return int(self.face)
        pictured = {"A":1,"J":11,"Q":12,"K":13}
        return pictured[self.face]

class BlackjackCard(Card):
    def getValue(self):# Override getValue() from Superclass
            if self.face.isdigit():
                return int(self.face)
            pictured = {"A":11, "J":10, "Q":10, "K":10}
            return pictured[self.face]

class Deck:
    FACES = ('A','2','3','4','5','6','7','8','9','10','J','Q','K') # class level attributes
    SUITS=('SPADES','CLUBS','DIAMONDS','HEARTS')
    def __init__(self):
        # more powerful way to generate a stack of cards
        self.stackOfCards = [BlackjackCard(face, suit) for face in Deck.FACES for suit in Deck.SUITS]
        # regular way to generate the stack of cards
        # self.stackOfCards = []
        # for f in Deck.FACES:
        #     for s in Deck.SUITS:
        #         card = BlackjackCard(f,s)
        #         self.stackOfCards.append(card)
        self.currentIndex = 51

    def test_numbersOfCardsInDeck(self):
        deck = Deck()
        self.assertTrue(52, len(deck.stackOfCards))

    def test_firstCard(self):
        deck = Deck()
        self.assertEqual('(A, SPADES)', deck.stackOfCards[0])

    def shuffle(self):
        random.shuffle(self.stackOfCards)

    def nextCard(self):
        card = self.stackOfCards[self.currentIndex]
        self.currentIndex -= 1
        if self.currentIndex == 0:
            self.shuffle()
            self.currentIndex = 51
        return card

class Player:
   
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.winCount = 0 # also add this attribute to dealer
   
    def win(self):
        self.winCount += 1
    
    def __repr__(self):
        return self.name
    
    def addCardToHand(self, card):
        self.hand.append(card)

    def cleanHand(self):
        self.hand.clear()

    def getHandSize(self):
        return len(self.hand)

    def showHand(self):
        return f"{self.name}: {self.hand}:{self.getHandValue()}:{self.winCount}"


    def getHandValue(self): # A , Q, A, Q = 42
        value = 0
        for card in self.hand:
            value += card.getValue()
        count = self.countAce()
        while value>21 and count>0:# A=11
            value -= 10 # change A=1
            count-=1
        return value# 22

    def countAce(self):
        count = 0
        for card in self.hand:
            if card.face == 'A':
                count +=1
        return count # return number of  ace in hand

    def hit(self):
        value = self.getHandValue()
        if value >=21:
            return False
        print()
        anotherCard = input(self.name + " Do you want another card? (y/n)")
        if anotherCard == 'y':
            return True
        return False

class Dealer(Player):
    
    def __init__(self):
        self.hand = []
        self.name = "Dealer"
        self.deck = Deck()
        self.winCount = 0   

    
    def hit(self):
        value = self.getHandValue()
        if value < 17:
            return True
        return False

    def shuffle(self):
        self.deck.shuffle()

    def deal(self):
        return self.deck.nextCard()

    def showHand(self,faceUp,):
        if not faceUp:
            return f"{self.name}: [{self.hand[0]}, HIDDEN]"
        return super().showHand()
        
class Game:
    import logging
    LOG_FORMAT = "%(asctime)s %(levelname)s - %(message)s"
    logging.basicConfig(filename=blackjack.log",level = logging.DEBUG, format=LOG_FORMAT)
    logger = logging.getLogger("Roy Huang")

    def __init__(self,playerList):
        self.logger.debug("__init__()...")
        self.dealer = Dealer()
        self.playerList = playerList
        self.dealer.shuffle()
    
    def dealCards(self):
        self.logger.debug("dealCards()...")
        for player in self.playerList:
            player.addCardToHand(self.dealer.deal())
            self.logger.info(f"{player.showHand()}")
        self.dealer.addCardToHand(self.dealer.deal())
        self.logger.info(f"{player.showHand()}")
        for player in self.playerList:
            player.addCardToHand(self.dealer.deal())
            self.logger.info(f"{player.showHand()}")
            print(player.showHand())
        self.dealer.addCardToHand(self.dealer.deal())
        self.logger.info(f"{self.dealer.showHand(True)}")
        print(self.dealer.showHand(False))

    def showResult(self):
        print("here is the result:")
        for player in self.playerList:
            print(player.msg)
            print(player.showHand())
        print(self.dealer.showHand(True))
        print()

    def cleanHand(self):
        for player in self.playerList:
            player.cleanHand()
        self.dealer.cleanHand()
        print() 

    def hit(self):
            for player in self.playerList:
                while player.hit():
                    player.addCardToHand(self.dealer.deal())
                    for p in self.playerList:
                        print(p.showHand())
            while self.dealer.hit():
                self.dealer.addCardToHand(self.dealer.deal())


    def play(self, winner):
        while True:
            self.dealCards()
            self.hit()
            for player in self.playerList:
                winner(self.dealer, player)
            self.showResult()
            anotherGame = input("\ndo you want to play another game? (y/n)")
            print()
            print()
            if anotherGame == 'n':
                break
            self.cleanHand()
        print("Game Over!")

def winner(dealer, player):


    """
    this function takes two positional arguments, dealer and player.
    It will increase winning count on dealer or player if he wins.
    """


    dealer.total = dealer.getHandValue()
    player.total = player.getHandValue()
    if player.total > 21:
        player.msg = f"Dealer wins! \n {player.name} is busted!"
        return dealer.win()
    return dealerBusted(dealer, player)

def dealerBusted(dealer, player):
    if dealer.total > 21:
        player.msg = f"{player.name} wins!\nthe dealer is busted"
        return player.win()
    return tied(dealer, player)

def tied(dealer, player):
    if dealer.total == player.total:
        player.msg = ("It's a tie! \nNothing happens!")
        return


    return playerLarge(dealer ,player)

def playerLarge(dealer, player):
    if player.total>dealer.total:
        player.msg = f"{player.name} wins \ndealer loses"
        return player.win()
    player.msg = f"Dealer wins \n{player.name} loses "
    return dealer.win()

def determineWinner(dealer,player):
    dealerTotal = dealer.getHandValue()
    playerTotal = player.getHandValue()
    if playerTotal>21:
        dealer.win()
    elif dealerTotal>21:
        player.win()
    elif playerTotal==dealerTotal:
        pass
    elif playerTotal > dealerTotal:
        player.win
    else:
        dealer.win()

def buildPLayerList():
    playerList = []
    while True:
        morePlayer = input("Player(y/n)")
        if morePlayer=='n':
            break
        elif morePlayer =='y': 
            pass


        while True:
            name = input("enter a name:")
            if contains(name, playerList):
                print(f"The name '{name}' is already taken")
            else:
                break
        player = Player(name)
        playerList.append(player)
    return playerList

def contains(name,playerList):
    for player in playerList:
        if name == player.name:
            return True 
    return False

if __name__ == '__main__':
        
    game = Game(buildPLayerList()) 
    game.play(winner) # pass function to play function

