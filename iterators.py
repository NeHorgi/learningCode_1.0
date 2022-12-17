'''
Реализуйте итератор колоды карт (52 штуки) CardDeck
Каждая карта представлена в виде строки типа "2 Пик". При вызове функции next()
Будет возвращаться следующая карта. "3 Пик "...
По окончании перебора всех элементов выводится сообщения "Колода закончилась"
'''


class CardDeck:

    def __init__(self):
        self.card_number = 0
        self.color = ''

    def __next__(self) -> str:
        self.card_number += 1

        if self.card_number == 1:
            self.color = 'Крести'
        elif self.card_number == 14:
            self.color = 'Буби'
        elif self.card_number == 27:
            self.color = 'Черви'
        elif self.card_number == 40:
            self.color = 'Пики'

        if self.card_number in [1, 14, 27, 40]:
            return f'{self.card_number} Туз {self.color}'
        elif self.card_number in [11, 24, 37, 50]:
            return f'{self.card_number} Валет {self.color}'
        elif self.card_number in [12, 25, 38, 51]:
            return f'{self.card_number} Дама {self.color}'
        elif self.card_number in [13, 26, 39, 52]:
            return f'{self.card_number} Король {self.color}'
        else:
            return f'{self.card_number} {self.color}'

    def dealer(self):
        while deck.card_number != 52:
            print(next(deck))
        print(f'Колода закончилась')

    def __iter__(self):
        return self


if __name__ == '__main__':
    deck = CardDeck()
    deck.dealer()

