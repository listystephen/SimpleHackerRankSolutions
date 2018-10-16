import math

class Complex(object):
    
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __add__(self, no):
        return Complex(self.real+no.real, self.imaginary + no.imaginary) 
    
    def __sub__(self, no):
        return Complex(self.real-no.real, self.imaginary - no.imaginary)
    
    def __mul__(self, no):
        realMul = (self.real*no.real) - (self.imaginary * no.imaginary)
        imgMul = (self.real*no.imaginary) + (self.imaginary * no.real)
        return Complex(realMul,imgMul)
               
    def __div__(self, no):
        divDr = (no.real * no.real) + (no.imaginary * no.imaginary)
        divNrReal = ((self.real*no.real) + (self.imaginary * no.imaginary))
        divNrImg = ((self.imaginary * no.real) - (self.real*no.imaginary))
        return Complex(divNrReal/divDr, divNrImg/divDr)
    
    def mod(self):
        return Complex(math.sqrt(self.real**2 + self.imaginary**2),0)
    def __str__(self):
        
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result
		
if __name__ == '__main__':
    c = map(float, raw_input().split())
    d = map(float, raw_input().split())
    x = Complex(*c)
    y = Complex(*d)
    print '\n'.join(map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]))