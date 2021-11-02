"""
Author: Vo Viet Thanh
Date: 10/10/2021
Program:
Solution:
    ....
"""
conversionLibrary = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "A":10, "B":10, "C":11, "D":13, "E":14, "F":15}
n = input("Nhap 1 so de chuyen qua ma dec: ")
frombase = int(input("Nhap co so ban muon chuyen doi: "))
n = n.upper()
def reptodecimal(n, frombase):
 tonumber = 0
 power = 0
 for i in range((len(n)),0, -1):
  tonumber += conversionLibrary[n[i-1]] * (int(frombase) ** power)
  power += 1
 return(tonumber)
def main():
 print(reptodecimal('10', 10))
 print(reptodecimal('10', 8))
 print(reptodecimal('10', 2))
 print(reptodecimal('10', 16))
main()
