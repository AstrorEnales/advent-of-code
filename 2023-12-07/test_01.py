import functools
import collections
from functools import cmp_to_key

card_labels = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
card_types = ['five_of_a_kind', 'four_of_a_kind', 'full_house', 'three_of_a_kind', 'two_pair', 'one_pair', 'high_card']


def get_card_type(hand: str) -> str:
    cards = collections.Counter(hand)
    if len(cards) == 1:
        return 'five_of_a_kind'
    values = list(cards.values())
    if len(cards) == 2:
        if values[0] == 4 or values[1] == 4:
            return 'four_of_a_kind'
        if values[0] == 3 or values[1] == 3:
            return 'full_house'
    if len(cards) == 3:
        if values[0] == 3 or values[1] == 3 or values[2] == 3:
            return 'three_of_a_kind'
        if values[0] == 2 or values[1] == 2 or values[2] == 2:
            return 'two_pair'
    if len(cards) == 5:
        return 'high_card'
    return 'one_pair'


def compare_cards_same_type(hand1: str, hand2: str) -> int:
    for i in range(0, len(hand1)):
        if hand1[i] != hand2[i]:
            card_label_index1 = card_labels.index(hand1[i])
            card_label_index2 = card_labels.index(hand2[i])
            return -1 if card_label_index1 < card_label_index2 else 1
    return 0


def compare_cards(hand1: str, hand2: str) -> int:
    card_type1 = get_card_type(hand1)
    card_type2 = get_card_type(hand2)
    if card_type1 == card_type2:
        return compare_cards_same_type(hand1, hand2)
    card_type_index1 = card_types.index(card_type1)
    card_type_index2 = card_types.index(card_type2)
    return -1 if card_type_index1 < card_type_index2 else 1


def compare_players(player1, player2) -> int:
    return compare_cards(player1[1], player2[1])


def rank_players(players):
    ranked_players = [(i, players[i][0], players[i][1]) for i in range(0, len(players))]
    ranked_players = sorted(ranked_players, key=cmp_to_key(compare_players))
    print(sum([ranked_players[i][2] * (len(ranked_players) - i) for i in range(0, len(ranked_players))]))


print(get_card_type('AAAAA'))
print(get_card_type('AA8AA'))
print(get_card_type('23332'))
print(get_card_type('TTT98'))
print(get_card_type('23432'))
print(get_card_type('A23A4'))
print(get_card_type('23456'))
print()
print(compare_cards('33332', '2AAAA'))
print(compare_cards('77888', '77788'))

test_hands = [
    ('32T3K', 765),
    ('T55J5', 684),
    ('KK677', 28),
    ('KTJJT', 220),
    ('QQQJA', 483)
]
rank_players(test_hands)

with open('input_01.txt', 'r', encoding='utf-8') as f:
    lines = [x.strip() for x in f.readlines()]
    hands = [(x[0:5], int(x[6::])) for x in lines if x != '']
    rank_players(hands)
