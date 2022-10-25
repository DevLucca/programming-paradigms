
class Pow:

    __operand = 0
    __power = 0
    
    def __init__(self, power):
        self.__power = power
        
    def execute(self):
        return self.__operand ** self.__power
    
    def collect(self, last_value):
        self.__operand = float(input("Please, input first number: ")) if last_value == None else last_value

        return self
    
    def get_operands(self):
        return f"{self.__operand} ^{self.__power}"
