import math

class Root:

    __operand = 0
    __base = 0
    
    def __init__(self, base):
        self.__base = base
        
    def execute(self):
        return math.exp(math.log(self.__operand)/self.__base)
    
    def collect(self, last_value):
        self.__operand = float(input("Please, input first number: ")) if last_value == None else last_value

        return self

    def get_operands(self):
        return f"{self.__base}√ {self.__operand}"
