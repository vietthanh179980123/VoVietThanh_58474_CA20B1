"""
    Name: Võ Viết Thanh
    Date:30/10/2021
    File: rational.py
    Resource to manipulate rational numbers.
"""
class Rational(object):
    def __init__(self,numer,denom):
        self._numer = numer
        self._denom = denom
        self._reduce()

    def numerator(self):
        return self._numer

    def denominator(self):
        return self._denom

    def __str__(self):
        return str(self._numer) + "/" + str(self._denom)

    def _reduce(self):
        divisor = self._gcd(self._numer, self._denom)
        self._numer = self._numer / divisor
        self._denom = self._denom / divisor

    def _gcd(self, a, b):
        (a, b) = (max(a, b), min(a, b))
        while b>0:
            (a, b) = (b, a % b)
        return a

    def __add__(self, other):
        print("DEBUG: call __add__")
        newNumer = self._numer * other._denom + \
                   other._numer * self._denom
        newDenom = self._denom * other._denom
        return Rational(newNumer, newDenom)

    def __lt__(self, other):
        print("DEBUG: call __lt__")
        extremes = self._numer * other._denom
        means = other._numer * self._denom
        return extremes < means

    def __eq__(self, other):
        print("DEBUG: call __eq__")
        if self is other:
            return True
        elif type(self) != type(other):
            return False
        else:
            return self._numer == other._numer and \
                   self._denom == other._denom

if __name__ == '__main__':
    oneHalf = Rational(1, 2)
    twoSixth = Rational(2, 6)
    print(f"oneHalf: {oneHalf}")
    print(f"twoSixth: {twoSixth}")

    print(oneHalf + twoSixth)
    print(f"oneHalf == twoSixth: {oneHalf == twoSixth}")
    print(f"oneHalf < twoSixth: {oneHalf < twoSixth}")

