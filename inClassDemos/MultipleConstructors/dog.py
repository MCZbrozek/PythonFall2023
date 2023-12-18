class calc:

    def __init__(self, *args ):
        
        if len(args) > 1:
            self.sum = sum(args)

        elif isinstance(args[0], str):
            self.sentence = f'Hello, {args[0]}'

        elif isinstance(args[0], int):
            self.double = args[0] * 2
         


ca = calc("Mike")     
print(ca.sentence)