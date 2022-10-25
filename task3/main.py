
if __name__ == '__main__':
    import os
    import sys
    import time
    from pick import pick
    
    from calculator import Calculator
    
    calc = Calculator()
    
    while True:
        os.system('cls||clear')
        title = 'Please choose your operation: '
        options = [
            *calc.operations.keys(),
            # Leave these 3 as last options
            'clear', 'view history', 'exit'
        ]
        option, index = pick(options, title, indicator='>>>', default_index=0)
        
        if option in options[-3:]:
            if option == 'exit': sys.exit(0)
            if option == 'clear': 
                calc.clear()
                continue
            if option == "view history": 
                calc.view_history()
                continue
        
        calc.set_op(option).calculate()
        time.sleep(1)
