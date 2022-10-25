import math

class Log:

    __operand = 0
        
    def execute(self):
        return math.log2(self.__operand)
    
    def collect(self, last_value):
        self.__operand = float(input("Please, input first number: ")) if last_value == None else last_value

        return self
