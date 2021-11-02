"""
Author: Vo Viet Thanh
Date: 10/10/2021
Program: Define a function decimalToRep that returns the representation of an integer in a
given base. The two arguments should be the integer and the base. The function
should return a string. It should use a lookup table that associates integers with
digits. Include a main function that tests the conversion function with numbers
in several bases.
Solution:
    ....
"""
def decimaltorep(n,base):
	convertstring = "0123456789ABCDEF"
	if n < base:
		return convertstring[n]
	else :
		return decimaltorep(n//base,base) + convertstring[n%base]
if __name__ == '__main__':
	print(decimaltorep(1453,2))
	print(decimaltorep(1453,3))
	print(decimaltorep(1453,8))
	print(decimaltorep(1453,16))
	print(decimaltorep(2,4))
