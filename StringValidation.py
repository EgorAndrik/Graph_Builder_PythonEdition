class CheckFunctions:
    def __init__(self, arithmetic_example: str):
        self._arithmetic_example = arithmetic_example

    def placementOfSigns(self) -> bool:
        alphaSnak = [
                "+*", "*+", "+*+", "-*",
                "*-", "-*-", "+/", "/+",
                "+/+", "-/", "/-", "-/-",
        ]
        for el in alphaSnak:
            if el in self._arithmetic_example:
                return False
        return True

    def brackets(self) -> bool:
        if '(' in self._arithmetic_example or ')' in self._arithmetic_example:
            arithmetic = self._arithmetic_example
            for i in '1234567890./*-+x ':
                arithmetic = arithmetic.replace(i, '')
            for i in ['cos', 'sin', 'abs', 'sqrt', 'tan', 'ctg']:
                arithmetic = arithmetic.replace(i, '')
            bracket = 0
            for i in arithmetic:
                bracket += 1 if i == '(' else -1
                if bracket == -1:
                    return False
            return bracket == 0
        return True

    def availableSymbols(self) -> bool:
        alpha = '1234567890.x+-*/() '
        arithmetic_example = self._arithmetic_example
        for el in alpha:
            arithmetic_example = arithmetic_example.replace(el, '')
        for el in ['cos', 'sin', 'abs', 'sqrt', 'tan', 'ctg']:
            arithmetic_example = arithmetic_example.replace(el, '')
        if len(arithmetic_example) > 0:
            return False
        return True