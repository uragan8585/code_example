import random


class Cards:
    cards_lts = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'] * 4


class Deck:
    player_card = []
    comp_card = []

    for i in range(4):
        current_cars = random.choice(Cards.cards_lts)
        Cards.cards_lts.remove(current_cars)
        if i % 2 == 0:
            player_card.append(current_cars)
        else:
            comp_card.append(current_cars)


class Player(Deck):

    def __init__(self, name, player_card):
        self.name = name
        self.card_hand = player_card


class Comp:

    def __init__(self, name, card_hand):
        self.name = name
        self.card_hand = card_hand


def counting_score(card_hand):
    score = 0
    for i_card, card in enumerate(card_hand):
        if card_hand.count('A') == 2:
            score = True
            return score
        else:
            if card == 'A':
                card_hand[i_card] = 11
                score += card_hand[i_card]
                if score > 21:
                    card_hand[i_card] = 1
            elif isinstance(card, str) and card != 'A':
                card_hand[i_card] = 10
                score += card_hand[i_card]
            elif isinstance(card, int):
                score += card_hand[i_card]
    return score


def add_card(card_hand):
    current_cars = random.choice(Cards.cards_lts)
    print('\nНовая карта:', current_cars)
    Cards.cards_lts.remove(current_cars)
    card_hand.append(current_cars)
    counting_score(card_hand)


def turn_comp():
    print('\n', '-' * 6, 'Играет компьютер', '-' * 6)
    print('Карты в руке компьютера:', *comp.card_hand)
    while True:
        score_comp = counting_score(comp.card_hand)
        if score_comp == True:
            return score_comp
        print('Очки: ', score_comp)
        if score_comp >= 22:
            return 0
        elif score_comp < 17:
            add_card(comp.card_hand)
        else:
            return score_comp

if __name__ == '__main__':
    user = Player('Игрок 1', Deck.player_card)
    comp = Comp('Шуроповёрт', Deck.comp_card)

    print('Выше имя:', user.name)
    print('Карты на руке: ', *user.card_hand)

    while True:
        card_print = list.copy(user.card_hand)
        score_user = counting_score(user.card_hand)
        if score_user == True:
            print('Вы выйграли. Блек Джек.')
            break
        print('Очки: ', score_user)
        if score_user >= 22:
            print('Перебор. Вы проиграли.')
            break

        answer_user = input('Достаточно (да, нет)? ').lower()
        if answer_user == 'нет':
            add_card(user.card_hand)
        elif answer_user == 'да':
            score_comp = turn_comp()
            if score_comp == True:
                print(f'{comp.name} выйграл. Блек Джек.')
                break
            if score_user > score_comp:
                print('Вы выйграли')
            elif score_user < score_comp:
                print(f'{comp.name} выйграл')
            else:
                print('Ничья')
            break
        else:
            print('Неверная команда')
