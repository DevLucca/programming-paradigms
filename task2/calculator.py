from pick import pick
import math

class Calculator:
    
    __history: list = []
    __mem_storage: int = 0
    
    def __add_to_history(self, str):
        self.__history.append(str)
        
    def sum(self, num1, num2):
        op_to_do = f"{num1} + {num2}"
        print(op_to_do)
        self.__add_to_history(op_to_do)
        self.__mem_storage = num1 + num2
        
    def sub(self, num1, num2):
        op_to_do = f"{num1} - {num2}"
        print(op_to_do)
        self.__add_to_history(op_to_do)
        self.__mem_storage = num1 - num2
    
    def mult(self, num1, num2):
        op_to_do = f"{num1} * {num2}"
        print(op_to_do)
        self.__add_to_history(op_to_do)
        self.__mem_storage = num1 * num2
    
    def div(self, num1, num2):
        op_to_do = f"{num1} / {num2}"
        print(op_to_do)
        self.__add_to_history(op_to_do)
        self.__mem_storage = num1 / num2
    
    def pow(self, num, pow_num):
        op_to_do = f"{num}^{pow_num}"
        print(op_to_do)
        self.__add_to_history(op_to_do)
        self.__mem_storage = math.pow(num, pow_num)
        
    def root(self, num, root_base):
        op_to_do = f"root {num} {root_base}"
        print(op_to_do)
        self.__add_to_history(op_to_do)
        self.__mem_storage = math.root(num, root_base)
    
    def log(self, num):
        op_to_do = f"log {num}"
        print(op_to_do)
        self.__add_to_history(op_to_do)
        self.__mem_storage = math.log(num)
        
    def view_history(self):
        for index, history in enumerate(self.__history):
            print(f"[{index+1}] {history}")

    def use_memory(self):
        option, _ = pick(["yes", "no"], "Use memory? ", indicator='>>', default_index=0)
        if option == "yes":
            return self.__mem_storage
        return float(input("Please, input first number: "))

if __name__ == "__main__":
    calc = Calculator()
    
    while True:
        title = 'Please choose your operation: '
        options = ['+', '-', '*', '/', '^2', '^3', 'root2', 'root3', 'log', 'view history', 'exit']
        option, index = pick(options, title, indicator='>>', default_index=0)
        
        if option == "+":
            calc.sum(calc.use_memory(), float(input("Please, input second number: ")))
        if option == "-":
            calc.sub(calc.use_memory(), float(input("Please, input second number: ")))
        if option == "*":
            calc.mult(calc.use_memory(), float(input("Please, input second number: ")))
        if option == "/":
            calc.div(calc.use_memory(), float(input("Please, input second number: ")))
            
        if option == "^2":
            calc.pow(calc.use_memory(), 2)
        if option == "^3":
            calc.pow(calc.use_memory(), 3)
        if option == "roo2":
            calc.root(calc.use_memory(), 2)
        if option == "root3":
            calc.root(calc.use_memory(), 3)
        if option == "log":
            calc.log(calc.use_memory())
            
        if option == "view history":
            calc.view_history()
        
        if option == "exit":
            import sys
            sys.exit(0)

        input("press any enter to resume...")
