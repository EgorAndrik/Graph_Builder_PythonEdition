import matplotlib.pyplot as plt
import numpy as np
from sympy import *
from math import *


#       _______           _____        ____________  _          _
#      /   __  \         / ___ \       | ________ | | |        | |
#     /  /   \  \       / /   \ \      | |      | | | |        | |
#    /  /     |__|     / /_____\ \     | |______| | | |________| |
#   |  |    ______    /  _______  \    |  ________| |  ________  |
#    \  \  |__    |  / /         \ \   | |          | |        | |
#     \  \____|  /  / /           \ \  | |          | |        | |
#      \________/  /_/             \_\ |_|          |_|        |_|


class GraphBuilder:
    def _handler(self, arifmEx: str) -> str:
        arifmEx = arifmEx.replace(' ', '')
        arifmEx = arifmEx.lower()
        if '^' in arifmEx:
            arifmEx = arifmEx.replace('^', '**')
        if len(arifmEx[:arifmEx.find('x**')]) == 0:
            arifmEx = "1*" + arifmEx
        return arifmEx

    def _check(self, arifmEx: str) -> bool:
        varsFunc = ['cos', 'sin', 'abs', 'sqrt', 'tan', 'ctg']
        return any([i in arifmEx for i in varsFunc])

    def buildG(self, arithmetic_example: str):
        function = arithmetic_example
        function = self._handler(function)
        fig, ax = plt.subplots()
        ax.set_title('Graph function')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        plt.grid(True)
        if not self._check(function):
            roots = []

            if '/' in function:
                arifmEx = function.split('/')
                x = symbols('x', real=True)
                roots = solve(Eq(eval(arifmEx[0]), 0), x) + solve(Eq(eval(arifmEx[1]), 0), x)

            if '/' not in function:
                x = symbols('x', real=True)
                roots = solve(Eq(eval(function), 0), x)

                if len(roots) == 0 and 'x**2' in function and 'x' in function[function.find('x**') + 1:]:
                    terms = list(map(lambda x: x.replace('**2', '').replace('*', ''), function.split('x')))
                    a = float(terms[0])
                    b = float(terms[1])
                    roots.append(-b / (2 * a))

            if len(roots) == 0:
                roots = [0]

            elif len(roots) > 0 and \
                    any(([
                        str(type(i)) in ["<class 'sympy.core.numbers.NegativeOne'>", "<class 'sympy.core.add.Add'>",
                                         "<class 'sympy.core.power.Pow'>", "<class 'sympy.core.mul.Mul'>",
                                         "<class 'sympy.core.numbers.Rational'>"]
                        for i in roots])):
                roots = [0]

            X_min = float(min(roots) - 4.0)
            X_max = float(max(roots) + 4.0)

            x = np.linspace(X_min, X_max, 100)
            y = eval(function)
            ax.plot(x, y)

            fig.savefig(f'Images/Graph.png')

        else:
            function = eval(f"lambda x: {function}")
            x = np.linspace(0, 4 * np.pi, 100)
            y = [function(i) for i in x]
            ax.plot(x, y)

            fig.savefig(f'Images/Graph.png')
