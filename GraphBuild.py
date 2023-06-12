import matplotlib.pyplot as plt
import numpy as np
from sympy import *


class GraphBuilder:
    def _handler(self, arifmEx: str) -> str:
        arifmEx = arifmEx.replace(' ', '')
        if '^' in arifmEx:
            arifmEx = arifmEx.replace('^', '**')
        if len(arifmEx[:arifmEx.find('x**')]) == 0:
            arifmEx = "1*" + arifmEx
        return arifmEx

    def _check(self, arifmEx: str) -> bool:
        varsFunc = ['sin', 'cos', 'sqrt']
        return any([i in arifmEx for i in varsFunc])

    def buildG(self, arithmetic_example: str):
        function = arithmetic_example
        function = self._handler(function)
        fig, ax = plt.subplots()
        ax.set_title('Graph function')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        plt.grid(True)
        if not self._check(function):
            n = []

            if '/' in function:
                arifmEx = function.split('/')
                x = symbols('x', real=True)
                n = solve(Eq(eval(arifmEx[0]), 0), x) + solve(Eq(eval(arifmEx[1]), 0), x)

            if '/' not in function:
                x = symbols('x', real=True)
                n = solve(Eq(eval(function), 0), x)

                if len(n) == 0 and 'x**2' in function and 'x' in function[function.find('x**') + 1:]:
                    terms = list(map(lambda x: x.replace('**2', '').replace('*', ''), function.split('x')))
                    a = float(terms[0])
                    b = float(terms[1])
                    n.append(-b / (2 * a))

            if len(n) == 0:
                n = [0]

            elif len(n) > 0 and \
                    any(([
                        str(type(i)) in ["<class 'sympy.core.numbers.NegativeOne'>", "<class 'sympy.core.add.Add'>"]
                        for i in n])):
                n = [0]

            X_min = float(min(n) - 4.0)
            X_max = float(max(n) + 4.0)

            x = np.linspace(X_min, X_max, 100)
            y = eval(function)
            ax.plot(x, y)

            fig.savefig(f'Images/Graph.png')

        else:
            if 'cos' in function or 'sin' in function:
                function = '1*' + function

                x = np.linspace(0, 4 * np.pi, 100)
                y = eval(function[:function.find('sin') - 1]) * \
                    np.sin(eval(function[function.find('sin') + 4:function.find(')')])) if 'sin' in function \
                    else eval(function[:function.find('cos') - 1]) * \
                         np.cos(eval(function[function.find('cos') + 4:function.find(')')]))
                ax.plot(x, y)

                fig.savefig(f'Images/Graph.png')
            else:
                functioSqrt = function[function.index('sqrt') + 5:function.find(')')]

                x = np.linspace(0, 9, 100)
                y = eval(functioSqrt) ** 0.5
                ax.plot(x, y)

                fig.savefig(f'Images/Graph.png')
