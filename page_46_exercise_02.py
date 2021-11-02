"""
Author: Võ Viết Thanh
Date: 03/09/2021
Program: Write a string that contains your name and address on separate lines using embedded newline characters. Then write the same string literal without the newline
characters.
Solution:
    ....
"""
#with newline character
name = "Viet Thanh"
address = "Da Nang"
Inthongtin= "Ten cua ban là %s \nDia chi o %s"%(name,address)
print(Inthongtin)
#without newline charater
name = "Viet Thanh"
address = "Da Nang"
Inten="Ten cua ban la: %s"%name
Indiachi="Dia chi cua ban o: %s"%address
print(Inten)
print(Indiachi)

