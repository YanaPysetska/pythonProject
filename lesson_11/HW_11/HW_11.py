class Human:
    default_name="Yana"
    default_age=30
    def __init__(self,name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money=0
        self.__house=None

    def info(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Money: {self.__money}')
        print(f'House: {self.__house}')

    @staticmethod
    def default_info():
        print("Static Field 1:", Human.default_name)
        print("Static Field 2:", Human.default_age)
    def __make_deal(self, house, price):
        self.__money -= price
        self.__house = house
    def earn_money(self, amount):
        self.__money += amount

    def buy_house(self, house, discount):
        if self.__money >= house.final_price(discount):
            self.__make_deal(house, house.final_price(discount))
            print("House bought!")
        else:
            print("Not enough money to buy the house!")

class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        return self._price - discount

class SmallHouse(House):
    def __init__(self):
        super().__init__(area=40, price=50000)

Human.default_info()

human = Human()
human.info()

small_house = SmallHouse()
human.buy_house(small_house, 10000)

human.earn_money(40000)
human.buy_house(small_house, 10000)

human.info()