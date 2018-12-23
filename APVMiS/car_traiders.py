class Car:
    def __init__(self, name, year, price, in_stock, country):
        self.name = name
        self.year = year
        self.price = price
        self.in_stock = in_stock
        self.country = country

    def __repr__(self):
        return ('{name}, {year}, {price}$, {in_stock}, {country}'.format(
                    name=self.name,
                    year=self.year,
                    price=self.price,
                    in_stock=self.in_stock,
                    country=self.country,
                ))


class Person:
    def __init__(self, name, occupation, budget, date_of_birth, gender):
        self.name = name
        self.occupation = occupation
        self.budget = budget
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.can_buy = []
        self.cant_buy = []

    def __repr__(self):
        return ("{gender}.{name}, {date}, {occ}, {budget}$".format(
                    gender=self.gender,
                    name=self.name,
                    date=self.date_of_birth,
                    occ=self.occupation,
                    budget=self.budget,
                ))

    def buying(self, car_seq):
        for car in car_seq:
            if self.budget >= car.price and car.in_stock:
                self.can_buy.append('{}, {}$'.format(car.name, car.price))
            else:
                self.cant_buy.append('{}, {}$'.format(car.name, car.price))


if __name__ == '__main__':
    c1 = Car('Mazda', 2015, 15000, True, 'Japan')
    c2 = Car('Honda', 2010, 11000, True, 'Korea')
    c3 = Car('Volkswagen', 2013, 14000, True, 'Germany')
    c4 = Car('Subaru', 2016, 17000, True, 'Japan')
    c5 = Car('Hyundai', 2014, 15500, True, 'Korea')
    cars = [c1, c2, c3, c4, c5]
    p1 = Person('Smith', 'Doctor', 15000, '13-10-1980', 'Mr')
    p2 = Person('Brown', 'Nurse', 11000, '13-10-1980', 'Mrs')
    p3 = Person('Green', 'Teacher', 10000, '13-10-1980', 'Mrs')
    p4 = Person('Cooper', 'Engineer', 20000, '13-10-1980', 'Mr')
    p5 = Person('Johnson', 'Barber', 17500, '13-10-1980', 'Mr')
    persons = [p1, p2, p3, p4, p5]
    power = {}
    for person in persons:
        person.buying(cars)
        power['{}.{} ({}$) can buy'.format(
                person.gender,
                person.name,
                person.budget
        )] = person.can_buy
        power['{}.{} ({}$) cant buy'.format(
                person.gender,
                person.name,
                person.budget
        )] = person.cant_buy
    for i in power:
        print('{}: {}'.format(i, power[i]))
