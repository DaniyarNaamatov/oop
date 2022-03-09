#Создать класс Person c атрибутами first_name, last_name
#2) Создать доп.класс Jack и наследовать его от Person , добавив при этом дополнительные атрибуты phone_number , balance
#3) Создать еще один класс Vito, который будет наследоваться от класса Jack :
#         у последнего класса должен быть дополнительный 1 метод:
#                 первый метод,который минусует от balance Jack n-число и плюсует это число к  Vito.balance

#Отправить дз через GitHub

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name



class Jack(Person):
    def __init__(self, first_name, last_name,phone_number,balance):
        super().__init__(first_name, last_name)
        self.phone_number = phone_number
        self.balance = balance


class Vito(Jack):
    def __init__(self, first_name, last_name, phone_number, balance, number):
        super().__init__(first_name, last_name, phone_number, balance)
        self.number = number

    def dobavka(self):
        print(f"Jack баланс: {jack.balance - self.number}\n Vito баланс: {vito.balance + self.number}")

jack = Jack('Jack','Di','0700710500', 1000)
vito = Vito('Vito','Scaletta', '0700100400', 500, 100)
vito.dobavka()