

class Calculator():
    def sum(self, num1, num2):
        return num1 + num2

    def diff(self, num1, num2):
        return num1 - num2

    def divide(self, num1, num2):
        return num1 / num2

    def multiply(self, num1, num2):
        return num1 * num2


c1 = Calculator()
result = c1.sum(19, 16)
print(result)



diffresult = c1.diff(12, 16)
print(diffresult )

multiresult = c1.multiply(12, 16)
print(multiresult )

divresult = c1.divide(12, 16)
print(divresult )