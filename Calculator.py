from abc import ABC, abstractmethod
import logging

logging.basicConfig(filename='calculator.log', level=logging.INFO, format='%(asctime)s - %(message)s')

class Calculating(ABC):
    @abstractmethod
    def sum(self, arg):
        pass

    @abstractmethod
    def sub(self, arg):
        pass

    @abstractmethod
    def multi(self, arg):
        pass

    @abstractmethod
    def div(self, arg):
        pass

    @abstractmethod
    def get_result(self):
        pass

class Calculator(Calculating):
    def __init__(self, primary_arg):
        self.primary_arg = primary_arg
        logging.info(f'Начальный аргумент: {primary_arg}')

    def sum(self, arg):
        self.primary_arg += arg
        logging.info(f'Сложение с {arg}. Текущий результат: {self.primary_arg}')
        return self

    def sub(self, arg):
        self.primary_arg -= arg
        logging.info(f'Вычитание на {arg}. Текущий результат: {self.primary_arg}')
        return self

    def multi(self, arg):
        self.primary_arg *= arg
        logging.info(f'Умножение на {arg}. Текущий результат: {self.primary_arg}')
        return self

    def div(self, arg):
        self.primary_arg /= arg
        logging.info(f'Деление на {arg}. Текущий результат: {self.primary_arg}')
        return self

    def get_result(self):
        logging.info(f'Получен результат: {self.primary_arg}')
        return self.primary_arg

class CalculatingFactory:
    @staticmethod
    def create(primary_arg):
        return Calculator(primary_arg)

class ViewCalculator:
    def __init__(self, calculating_factory):
        self.calculating_factory = calculating_factory

    def run(self):
        while True:
            primary_arg = self.prompt_int("Введите первый аргумент: ")
            calculator = self.calculating_factory.create(primary_arg)
            while True:
                cmd = self.prompt("Подтвердите действие(+,-,*,/,=) : ")
                if cmd == "*":
                    arg = self.prompt_int("Введите второй аргумент: ")
                    calculator.multi(arg)
                    continue
                if cmd == "/":
                    arg = self.prompt_int("Введите второй аргумент: ")
                    calculator.div(arg)
                    continue
                if cmd == "+":
                    arg = self.prompt_int("Введите второй аргумент: ")
                    calculator.sum(arg)
                    continue
                if cmd == "-":
                    arg = self.prompt_int("Введите второй аргумент: ")
                    calculator.sub(arg)
                    continue
                if cmd == "=":
                    result = calculator.get_result()
                    print(f"Результат {result}")
                    break
            cmd = self.prompt("Продолжить(Y/N)?")
            if cmd != "Y":
                break

    def prompt(self, message):
        return input(message).upper()

    def prompt_int(self, message):
        return int(input(message))

if __name__ == "__main__":
    calculating_factory1 = CalculatingFactory()
    view = ViewCalculator(calculating_factory1)
    view.run()
