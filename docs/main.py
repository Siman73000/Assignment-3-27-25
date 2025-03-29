import sympy as sp

class Derivative:
    def __init__(self, function_expr, variable='x'):
        self.x = sp.symbols(variable)
        self.function = sp.sympify(function_expr)
    
    def first_derivative(self):
        return sp.diff(self.function, self.x)
    
    def second_derivative(self):
        return sp.diff(self.first_derivative(), self.x)
    
    def third_derivative(self):
        return sp.diff(self.second_derivative(), self.x)
    
    def evaluate_derivative(self, derivative_order, value):
        derivative = sp.diff(self.function, self.x, derivative_order)
        return derivative.subs(self.x, value)