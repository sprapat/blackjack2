from blackjack2.src.card import Card

def test_init_card():
    card = Card('A','S')
    assert card is not None
    assert card.value == 'A'
    assert card.suit == 'S'
    card = Card('2','H')
    assert card.value == '2'
    assert card.suit == 'H'

def test_card_equal():
    card1 = Card('A','S')
    card2 = Card('A','S')
    card3 = Card('2','H')
    assert card1 == card2
    assert card1 != card3

def test_card_score():
    assert Card('A','C').score == 11
    assert Card('J','H').score == 10
    assert Card('Q','H').score == 10
    assert Card('K','H').score == 10
    assert Card('5','H').score == 5
    