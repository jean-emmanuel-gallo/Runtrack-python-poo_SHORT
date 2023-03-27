class Operation():
    def __init__(self, number1=0, number2=0):
        self.number1 = number1
        self.number2 = number2

        print(self.number1.__add__(self.number2))

operation = Operation(12, 3)