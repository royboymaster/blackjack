import unittest
from src.blackjack import *

class TestCard(unittest.TestCase):
    heartsA = Card("A", "HEARTS")
    diamonds4 = Card("4", "DIAMONDS")
    clubsQ = Card("Q", "CLUBS")
    black_heartsA = BlackjackCard("A", "HEARTS")
    black_diamonds4 = BlackjackCard("4", "DIAMONDS")
    black_clubsQ = BlackjackCard("Q", "CLUBS")
    black_spades7 = BlackjackCard("7", "SPADES")
    roy = Player("roy") # class level attribute
    roy.addCardToHand(black_heartsA)
    roy.addCardToHand(black_clubsQ)
    dealer = Dealer() # create dealer instance
    
    def test_repr(self):
        self.assertEqual("Dealer", repr(self.dealer))

    def test_getCardValue(self):
        self.assertEqual(4, self.diamonds4.getValue())
        self.assertEqual(1, self.heartsA.getValue())
        self.assertEqual(12, self.clubsQ.getValue())

    def test_getBlackjackCardValue(self):
        self.assertEqual(4, self.black_diamonds4.getValue())
        self.assertEqual(11, self.black_heartsA.getValue())
        self.assertEqual(10, self.black_clubsQ.getValue())

    def test_numberOfCardsInDeck(self):
        deck = Deck()
        self.assertTrue(52, len(deck.stackOfCards))

    def test_firstCard(self):
        deck = Deck()
        self.assertEqual('(A, SPADES)', deck.stackOfCards[0].__repr__())

    def test_lastCard(self):
        deck = Deck()
        self.assertEqual('(K, HEARTS)', deck.stackOfCards[51].__repr__())

    def test_shuffle(self):
        deck = Deck()
        deck.shuffle()
        self.assertNotEqual('(A, SPADES)', deck.stackOfCards[0].__repr__())
    #    self.assertNotEqual('(K, HEARTS)', deck.stackOfCards[51].__repr__())

    def getRoy(self):
        roy = Player("roy") # local variable within function
        roy.addCardToHand(self.black_heartsA)
        roy.addCardToHand(self.black_clubsQ)
        return roy

    def getJunior(self):
        junior = Player("junior") # local variable within function
        junior.addCardToHand(self.black_heartsA)
        junior.addCardToHand(self.black_clubsQ)
        junior.addCardToHand(self.black_diamonds4)
        return junior

    def test_playerHand(self):
        roy = self.getRoy()
        card = roy.hand[0]
        self.assertEquals(card, self.black_heartsA)
        card = roy.hand[1]
        self.assertEquals(card, self.black_clubsQ)
    
    def test_cleanHand(self):
        self.roy.cleanHand()
        self.assertEquals(0, self.roy.getHandSize())

    def test_showHand(self):
        roy = Player("roy") # local variable within function
        roy.addCardToHand(self.black_heartsA)
        roy.addCardToHand(self.black_clubsQ)
        actual = roy.showHand()
        expected = "roy: [(A, HEARTS), (Q, CLUBS)]:21:0"
        self.assertEqual(expected, actual)

    def test_getHandValue(self):
        roy = self.getRoy()
        actual = roy.getHandValue()
        self.assertEqual(21, actual)

    def test_getHandValueWithAceBust(self):
        junior = self.getJunior()
        actual = junior.getHandValue()
        self.assertEqual(15, actual)

    def testdealerHit(self):
        dealer = Dealer()
        dealer.addCardToHand(self.black_spades7)
        dealer.addCardToHand(self.black_clubsQ)
        self.assertEqual(False, dealer.hit())
        dealer = Dealer()
        dealer.addCardToHand(self.black_heartsA)
        self.assertEqual(True, dealer.hit())

    def testShowHand4Dealer(self):
        dealer = Dealer()
        dealer.addCardToHand(self.black_diamonds4)
        dealer.addCardToHand(self.black_clubsQ) # 8 in hand
        actual = dealer.showHand(False)
        expected = "Dealer: [(4, DIAMONDS), HIDDEN]"
        self.assertEqual(expected, actual)
        actual = dealer.showHand(True)
        expected = "Dealer: [(4, DIAMONDS), (Q, CLUBS)]:14:0"
        self.assertEqual(expected, actual)

    def testShowHandWith2AcesBusted(self):
        junior = Player("Junior")
        junior.addCardToHand(self.black_heartsA)
        junior.addCardToHand(self.black_clubsQ)
        junior.addCardToHand(self.black_heartsA)
        junior.addCardToHand(self.black_clubsQ)
        expected = 22
        actual = junior.getHandValue()
        self.assertEqual(expected, actual)
    
    def testCountAce(self):
        junior = Player("Junior")
        junior.addCardToHand(self.black_heartsA)
        junior.addCardToHand(self.black_clubsQ)
        junior.addCardToHand(self.black_heartsA)
        junior.addCardToHand(self.black_clubsQ)
        expected = 2
        actual = junior.countAce()
        self.assertEqual(expected, actual)
      

    def testThreeAce(self):
        junior = Player("Junior")
        junior.addCardToHand(self.black_heartsA)
        junior.addCardToHand(self.black_clubsQ)
        junior.addCardToHand(self.black_heartsA)
        junior.addCardToHand(self.black_heartsA)
        junior.addCardToHand(self.black_diamonds4)
        expected = 17
        actual = junior.getHandValue()
        self.assertEqual(expected, actual)
    
    def testFourAce(self):
        junior = Player("Junior")
        junior.addCardToHand(self.black_heartsA)
        junior.addCardToHand(self.black_heartsA)
        junior.addCardToHand(self.black_clubsQ)
        junior.addCardToHand(self.black_heartsA)
        junior.addCardToHand(self.black_heartsA)
        junior.addCardToHand(self.black_diamonds4)
        expected = 18
        actual = junior.getHandValue()
        self.assertEqual(expected, actual)    