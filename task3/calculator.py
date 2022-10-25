import ops  

class Calculator:
    
    operations = {
        '+':    ops.Sum(),
        '-':    ops.Sub(),
        '*':    ops.Mlt(),
        '/':    ops.Div(),
        '^2':   ops.Pow(2),
        '^3':   ops.Pow(3),
        '√2':   ops.Root(2),
        '√3':   ops.Root(3),
        'log':  ops.Log(),
    }
    
    __history: list = []
    __memory = None
    __selected_op = None
    
    def __append_to_history(self, str):
        self.__history.append(str)
      
    def set_op(self, op):
        self.__selected_op = self.operations[op]
        return self

    def calculate(self):
        result = self.__selected_op.collect(self.__memory).execute()
        self.__memory = result
        print(self.__memory)
        self.__append_to_history(f"{self.__selected_op.get_operands()} = {result}")
        input("press enter to resume...")
        return self

    def clear(self):
        self.__memory = None
        self.__append_to_history(f"{'MEMORY CLEARED':=^20}")
        return self
    
    def view_history(self):
        for index, history in enumerate(self.__history):
            print(f"[{index+1}] {history}")
            
        input("press enter to resume...")

