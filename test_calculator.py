# """""""""""""""""""""""""""""""""""""""
#
# Unit tests for the calculator library
#
# """""""""""""""""""""""""""""""""""""""
#
import calculator

class TestCalculator:
    def test_addition(self):
       self.b=0
       self.b = calculator.add(5, 5.5)
       print("b:",self.b)
       a = 10
#       b = 10.5
       if (self.b > a):
           assert self.b/a < 1.10
       elif(self.b < a):
           assert self.b/a > 0.9

    def test_subtraction(self):
        assert 2 == calculator.subtract(4, 2)

    def test_example(self):
#        calculator.add(1,2)
        print("Hello world")

 # calc = TestCalculator()
 # calc.test_addition()
 # print("b:",calc.b)
