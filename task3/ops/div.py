
class Div:

    __first_operand = 0
    __second_operand = 0
    
    def execute(self):
        return self.__first_operand / self.__second_operand
    
    def collect(self, last_value):
        self.__first_operand = float(input("Please, input first number: ")) if last_value == None else last_value
        self.__second_operand = float(input("Please, input second operand: "))

        return self

    def get_operands(self):
        return f"{self.__first_operand} / {self.__second_operand}"
