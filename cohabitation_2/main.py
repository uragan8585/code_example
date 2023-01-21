import random


class House:
    """
    Класс Дом. Описывает дом: тумбочку с деньгами. Холодильник с едой (для людей, кошек) и грязь в доме.

    Args:
        qty_money (int): количество денег
        food_hums (int): еда для людей
        food_cat (int): еда для кота
        qty_dirt (int): количество грязи
    """

    def __init__(self):
        self.qty_money = 100
        self.food_hums = 50
        self.food_cat = 60
        self.qty_dirt = 0

    def __str__(self):
        """ Возвращает информацию о состояние дома"""

        return f'''Информация о состояние дома
Колчиство деньги: {self.qty_money}
Еды в холодильнике: {self.food_hums}
Еда для кота: {self.food_cat}
Грязи: {self.qty_dirt}
'''

    def litter(self):
        """Метод добавляет грязь в доме (+5)"""

        self.qty_dirt += 5


class Character:
    """
    Базовый класс Персонаж. Описывающий человека

    Args:
        name (str): передаётся имя человека
        hunger (int): передаётся уровень голода человека
        happy (int): передаётся уровень счастья человека
        house (class): передаётся привязанный класс Дома
        __total_to_eat (int): общее количество съеденной еды (человеком)
    """

    def __init__(self, name, hunger, happy, house=None):
        self.name = name
        self.hunger = hunger
        self.happy = happy
        self.house = house
        self.__total_to_eat = 0

    def to_eat(self):
        """
        Метод Питания персонажа. При обращении к методу проверяется количество еды из
        привязанного класса Дом- еды для людей. Если еды > 30, то у персонажа прибавляется уровень сытости +30, а
        из привязанного класса Дом (еды для людей) - 30. И к общему значению съеденное еды (человеком) +30
        Иначе если недостаточно еды, выводится сообщение 'В холодильнике мыш повесилась.'.
        """

        if house_1.food_hums > 30:
            print(f'{self.name} поел')
            self.house.food_hums -= 30
            self.hunger += 30
            self.__total_to_eat += 30
        else:
            print('В холодильнике мыш повесилась.')

    def action(self):
        """
        Метод Действие. При обращении к методу у персонажа снижается уровень голода -10
        """

        self.hunger -= 10

    def petting_cat(self):
        """
        Метод поглаживания кото. При обращении к методу вызывается метод Действие
        и у персонажа повышается уровень счастья +5
        """

        print(f'{self.name} гладит кота')
        self.action()
        self.happy += 5

    def get_total_to_eat(self):
        """
        Геттер для получения общего значения съеденной еды (человеком)

        :return: __total_to_eat
        :rtype: int
        """

        return self.__total_to_eat

    def __str__(self):
        """ Возвращает информацию о персонаже"""

        return f'''Информация о персонаже
Имя: {self.name}
Голод: {self.hunger}
Счастье: {self.happy}
'''


class Husband(Character):
    """
    Класс Муж. Родитель: Character

    Args:
        name (str): передаётся имя человека
        hunger (int): передаётся уровень голода человека
        happy (int): передаётся уровень счастья человека
        house (class): передаётся привязанный класс Дома
        __total_money_earned (int): общее количество заработанных денег
    """

    def __init__(self, name, hunger, happy, house):
        super().__init__(name, hunger, happy, house)
        self.__total_money_earned = 0

    def play(self):
        """
        Метод Играть. При обращении к методу вызывается метод Действие из родительского класса
        и у мужа повышается уровень счастья +20
        """

        print(f'{self.name} играет в компьютер.')
        super(Husband, self).action()
        self.happy += 20

    def goto_work(self):
        """
        Метод Идти на работу. При обращении к методу вызывается метод Действие из родительского класса.
        Прибавляется количество денег в привязанный класс- Дом.
        Прибавляется общее количество заработанных денег.
        """

        print(f'{self.name} пошёл на работу.')
        super(Husband, self).action()
        self.house.qty_money += 150
        self.__total_money_earned += 150

    def get_money_earned(self):
        """
        Геттер для получения общего количество заработанных денег.

        :return: __total_money_earned
        :rtype: int
        """

        return self.__total_money_earned


class Wife(Character):
    """
    Класс Жена. Родитель: Character

    Args:
        name (str): передаётся имя человека
        hunger (int): передаётся уровень голода человека
        happy (int): передаётся уровень счастья человека
        house (class): передаётся привязанный класс Дома
        __fur_coat (int): количество купленных шуб
    """

    def __init__(self, name, hunger, happy, house):
        super().__init__(name, hunger, happy, house)
        self.__fur_coat = 0

    def goto_shop_food(self):
        """
        Метод Сходить в магаз за едой. При обращении к методу вызывается метод Действие из родительского класса.
        Убавляется количество денег в привязанном классе- Дом. -72
        Прибавляется еда (для человека) в привязанный класс- Дом. +60
        Прибавляется еда (для кота) в привязанный класс- Дом. +12
        """

        print(f'{self.name} пошла в магазин.')
        super(Wife, self).action()
        self.house.qty_money -= 72
        self.house.food_hums += 60
        self.house.food_cat += 12

    def buy_fur_coat(self):
        """
        Метод купить шубу. При обращении к методу вызывается метод Действие из родительского класса.
        Если при проверке количества денег в привязанном классе- Дом > 400,
        то убавляется количество денег в привязанном классе- Дом. -350,
        повышается уровень счастья персонажа +60,
        прибавляется в общему значению (количество купленных шуб) +1
        """

        super(Wife, self).action()
        if self.house.qty_money > 400:
            self.house.qty_money -= 350
            self.happy += 60
            self.__fur_coat += 1
            print(f'{self.name} купила шубу.')

    def clean_up(self):
        """
        Метод Уборка. При обращении к методу вызывается метод Действие из родительского класса.
        Если при проверке количество грязи в привязанном классе- Дом <100,
        то значение количество грязи обнуляется.
        Иначе значение количество грязи - 100
        """

        super(Wife, self).action()
        print(f'{self.name} занялась уборкой.')

        if self.house.qty_dirt < 100:
            self.house.qty_dirt = 0
        else:
            self.house.qty_dirt -= 100

    def get_qty_fur_coat(self):
        """
        Геттер для получения общего значения купленных шуб.

        :return: __fur_coat
        """

        return self.__fur_coat


class Cat(Character):
    """
    Класс Кот. Родитель: Character

    Args:
        name (str): передаётся имя человека
        hunger (int): передаётся уровень голода человека
        happy (int): передаётся уровень счастья человека
        house (class): передаётся привязанный класс Дома
        __total_to_eat_cat (int): общее количество съеденной еды (для кошек)
    """

    def __init__(self, name, hunger, happy, house):
        super().__init__(name, hunger, happy, house)
        self.__total_to_eat_cat = 0

    def to_eat(self):
        """
        Метод Питания персонажа. При обращении к методу проверяется количество еды из
        привязанного класса Дом- еды для кошек. Если еды > 10, то у персонажа прибавляется уровень сытости +20, а
        из привязанного класса Дом (еды для людей) - 10. И к общему значению съеденное еды (питомцем) +10
        Иначе если недостаточно еды, выводится сообщение 'Нет еды. Иди мышей лови.'.
        """

        if house_1.food_cat > 10:
            self.house.food_cat -= 10
            self.hunger += 20
            self.__total_to_eat_cat += 10
            print(f'{self.name} поел')
        else:
            print('Нет еды. Иди мышей лови.')

    def harm(self):
        """
        Метод Обдирания обоев. При обращении к методу вызывается метод Действие из родительского класса.
        Счастье персонажа увеличивается на +10
        Количество грязи в привязанном классе- Дом +5.
        """

        super(Cat, self).action()
        self.happy += 10
        self.house.qty_dirt += 5
        print(f'{self.name} дерёт обои.')

    def sleep(self):
        """
        Метод Сна. При обращении к методу вызывается метод Действие из родительского класса.
        """

        super(Cat, self).action()
        print(f'{self.name} спит.')

    def get_total_to_eat_cat(self):
        """
        Геттер для получения общего значения съеденной еды (для кошек).

        :return: __total_to_eat_cat
        """

        return self.__total_to_eat_cat

if __name__ == '__main__':
    house_1 = House()
    husband = Husband(name='Жора', hunger=30, happy=100, house=house_1)
    wife = Wife(name='Люда', hunger=30, happy=100, house=house_1)
    cat = Cat(name='Кот "Крендель"', hunger=30, happy=100, house=house_1)

    game_over = False

    for dayZ in range(1, 366):
        print(f'\n{"-" * 5} {dayZ} день {"-" * 5}')
        for person in (husband, wife, cat):
            if person.hunger <= 0:
                print(f'К сожалению, {person.name} помер с голоду ')
                game_over = True
            if person.happy <= 10 and not isinstance(person, Cat):
                print(f'К сожалению, {person.name} умер от депрессии ')
                game_over = True
        if game_over:
            break

        if house_1.qty_dirt > 90:
            husband.happy -= 10
            wife.happy -= 10

        house_1.litter()

        if husband.hunger < 30:
            husband.to_eat()
        elif husband.happy < 50:
            husband.play()
        else:
            husband.goto_work()

        if wife.hunger < 30:
            wife.to_eat()
        elif wife.happy < 50:
            wife.buy_fur_coat()
        else:
            wife.goto_shop_food()

        if house_1.qty_dirt > 100:
            wife.clean_up()

        choise = random.randint(1, 5)
        if choise in range(1, 3):
            cat.to_eat()
        elif choise == 4:
            cat.harm()
        elif choise == 5:
            cat.sleep()

    print(f'''
Заработано денег: {husband.get_money_earned()}.
Съедено еды: {husband.get_total_to_eat()}.
Съели кошки еды: {cat.get_total_to_eat_cat()}.
Куплено шуб: {wife.get_qty_fur_coat()}.''')

    print('\nВсе выжили.' if dayZ == 365 else '\nБеда в доме.')
