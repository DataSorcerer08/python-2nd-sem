class Complex:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag
    
    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)
    
    def display(self):
        print(f"Result: {self.real} + {self.imag}i")

c1 = Complex(3, 2)
c2 = Complex(4, 5)
result = c1 + c2
result.display()
