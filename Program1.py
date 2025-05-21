class Calculator:
    def __init__(self, a, b, op):
        self.a = float(a)
        self.b = float(b)
        self.operation = op.lower()

    def calculate(self):
        if self.op == "add":
            return self.a + self.b
        elif self.op == "subtract":
            return self.a - self.b
        elif self.op == "multiply":
            return self.a * self.b
        elif self.op == "divide":
            return self.a / self.b if self.b != 0 else "Error"
        else:
            return "Invalid Opration"

a = input("Enter operand 1" )
b = input("Enter operand 2")
operation = input("Enter Operation (+,-,x,/)")
calc = Calculator(a, b, operation)
print(calc.calculate())

